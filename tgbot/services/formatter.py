"""格式化天气数据为所需的视图"""
import hashlib
from datetime import datetime
from math import log
from random import random
import requests
from deep_translator import GoogleTranslator

from tgbot.middlewares.localization import i18n
from tgbot.services.classes import CurrentWeatherData


_ = i18n.gettext  # gettext方法的别名



class FormatWeather:
    """用于格式化天气数据的类"""

    @staticmethod
    async def correct_user_input(city_name: str) -> str:
        """从城市名称中删除除字母、空格和连字符以外的所有内容"""
        processed_string: str = ""
        # 将城市名称截断至72个字符，因为这是城市名称的最大长度
        for char in city_name[:72]:
            if char.isalpha() or char == "-":
                processed_string += char
            elif char.isspace() and (not processed_string or not processed_string[-1].isspace()):
                processed_string += char
        return processed_string

    @staticmethod
    async def _get_weather_emoji(weather: int) -> str:
        """根据OpenWeatherMap的天气代码返回表情符号"""
        if weather in (800,):  # 晴朗
            weather_emoji: str = "☀"
        elif weather in (801,):  # 少云
            weather_emoji = "🌤"
        elif weather in (803, 804):  # 多云
            weather_emoji = "🌥"
        elif weather in (802,):  # 零散的云
            weather_emoji = "☁"
        elif weather in (500, 501, 502, 503, 504):  # 雨
            weather_emoji = "🌦"
        elif weather in (300, 301, 302, 310, 311, 312, 313, 314, 321, 520, 521, 522, 531):  # 毛毛雨
            weather_emoji = "🌧"
        elif weather in (200, 201, 202, 210, 211, 212, 221, 230, 231, 232):  # 雷雨
            weather_emoji = "⛈"
        elif weather in (511, 600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622):  # 雪
            weather_emoji = "🌨"
        elif weather in (701, 711, 721, 731, 741, 751, 761, 762, 771, 781):  # 大气
            weather_emoji = "🌫"
        else:  # 默认
            weather_emoji = "🌀"
        return weather_emoji

    @staticmethod
    def format_time(time_str: str) -> str:
        """将时间字符串转换为中文格式"""
        # 假设输入的time_str格式为 "16 Aug 11:14"
        dt = datetime.strptime(time_str, "%d %b %H:%M")
        return dt.strftime("%m月%d日 %H:%M")


    @staticmethod
    async def _calculate_dew_point(temp: int, humidity: int) -> int:
        """计算发生凝结的表面温度（露点）"""
        const_a: float = 17.27
        const_b: float = 237.7

        def func():  # type: ignore
            return (const_a * temp) / (const_b + temp) + log(humidity / 100)

        return round((const_b * func()) / (const_a - func()))  # type: ignore

    async def format_current_weather(
        self, weather_data: CurrentWeatherData, units: str, city: str, lang_code: str
    ) -> str:
        """以所需形式返回当前天气数据"""
        emoji = await self._get_weather_emoji(weather=weather_data.weather_code)
        temp_units: str = "°C" if units == "metric" else "°F"
        wind_units: str = "米/秒" if units == "metric" else "英里/小时"
        dew_point: int = await self._calculate_dew_point(temp=weather_data.temp, humidity=weather_data.humidity)

        if weather_data.precipitation:
            precipitation: str = (
                f", <b>{weather_data.precipitation} 毫米</b>" + _("一小时内的降水量", locale=lang_code) + ""
            )
        else:
            precipitation = ""
        if weather_data.gust:
            wind_gust: str = ", " + _("阵风可达", locale=lang_code) + f": <b>{weather_data.gust} {wind_units}</b>"
        else:
            wind_gust = ""
        time_zh = self.format_time(weather_data.time)

        precipitation = precipitation.lstrip(", ").strip()
        current_weather: str = (
            f"<b>{city}  {time_zh}</b>\n"
            + f"{emoji} {weather_data.weather_description}\n\n"
            + f"🌡 <b>{weather_data.temp}{temp_units}</b>, "
            + _("体感温度", locale=lang_code)
            + f" <b>{weather_data.feels_like}{temp_units}</b>\n\n"
            + "💦 "
            + _("湿度", locale=lang_code)
            + f": <b>{weather_data.humidity}%</b>, "
            + _("露点", locale=lang_code)
            + f": <b>{dew_point}{temp_units}</b>\n"
            + "💨 "
            + _("风速", locale=lang_code)
            + f": <b>{weather_data.wind_speed} {wind_units}</b>{wind_gust}\n"
            + "🌡 "
            + _("气压", locale=lang_code)
            + f": <b>{weather_data.pressure} 百帕</b>\n"
            + "🌫️ "
            + _("能见度", locale=lang_code)
            + f": <b>{weather_data.visibility} 公里</b>\n\n"
            + "🌅 "
            + _("日出", locale=lang_code)
            + f": <b>{weather_data.sunrise}</b>  🌇 "
            + _("日落", locale=lang_code)
            + f": <b>{weather_data.sunset}</b>"
        )
        return current_weather