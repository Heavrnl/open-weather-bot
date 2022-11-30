<p align="center">
    <img src="https://repository-images.githubusercontent.com/559574279/ac1f8317-c07c-4c0f-a4e4-c49ae01237cd" alt="Open Weather Bot" width="640">
</p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3108/">
        <img src="https://img.shields.io/badge/python-v3.10-informational" alt="python version">
    </a>
    <a href="https://pypi.org/project/aiogram/2.23.1/">
        <img src="https://img.shields.io/badge/aiogram-v2.23.1-informational" alt="aiogram version">
    </a>
    <a href="https://pypi.org/project/aiohttp/3.8.3/">
        <img src="https://img.shields.io/badge/aiohttp-v3.8.3-informational" alt="aiohttp version">
    </a>
    <a href="https://pypi.org/project/aiosqlite/0.17.0/">
        <img src="https://img.shields.io/badge/aiosqlite-v0.17.0-informational" alt="aiosqlite version">
    </a>
    <a href="https://pypi.org/project/APScheduler/3.9.1.post1/">
        <img src="https://img.shields.io/badge/APScheduler-v3.9.1.post1-informational" alt="APScheduler version">
    </a>
    <a href="https://pypi.org/project/environs/9.5.0/">
        <img src="https://img.shields.io/badge/environs-v9.5.0-informational" alt="environs version">
    </a>
    <a href="https://pypi.org/project/Pillow/9.3.0/">
        <img src="https://img.shields.io/badge/Pillow-v9.3.0-informational" alt="Pillow version">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg">
    </a>
    <a href="https://github.com/rin-gil/OpenWeatherBot/actions/workflows/tests.yml">
        <img src="https://github.com/rin-gil/OpenWeatherBot/actions/workflows/tests.yml/badge.svg" alt="Code tests">
    </a>
    <a href="https://github.com/rin-gil/OpenWeatherBot/actions/workflows/codeql.yml">
        <img src="https://github.com/rin-gil/OpenWeatherBot/actions/workflows/codeql.yml/badge.svg" alt="Code tests">
    </a>
    <a href="https://github.com/rin-gil/OpenWeatherBot/blob/master/LICENCE">
        <img src="https://img.shields.io/badge/licence-MIT-success" alt="MIT licence">
    </a>
</p>

<p align="right">
    <a href="https://github.com/rin-gil/OpenWeatherBot/blob/master/README.md">
        <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/icons/flags/united-kingdom_24x24.png" alt="En"></a>
    <a href="https://github.com/rin-gil/OpenWeatherBot/blob/master/README.ru.md">
        <img src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/icons/flags/russia_24x24.png" alt="Ru">
    </a>
</p>

## Open Weather Bot

Телеграм-бот, який показує прогноз погоди.
Робоча версія доступна за посиланням [https://t.me/OpenWeatherSmartBot](https://t.me/OpenWeatherSmartBot)

### Можливості

* Пошук міста за назвою або координатами
* Показ поточної погоди та прогнозу на 24 години
* Оновлення прогнозу погоди кожні 3 години

### Установлення

```
git clone https://github.com/rin-gil/OpenWeatherBot.git
cd OpenWeatherBot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv .env.dist .env
```

<img align="right" width="300" src="https://raw.githubusercontent.com/rin-gil/rin-gil/main/assets/img/projects/OpenWeatherBot/screenshot_ua.png" alt="Головний екран OpenWeatherBot">

### Налаштування та запуск

* Зареєструйте нового бота у [@BotFather](https://t.me/BotFather) і скопіюйте отриманий токен
* Вставте токен бота у файл .env
* Зареєструйте обліковий запис на сайті [OpenWeatherMap](https://home.openweathermap.org/users/sign_in)
* Створіть [API ключ](https://home.openweathermap.org/api_keys) і скопіюйте його у файл .env
* Вставте свій id Телеграм у файл .env
* Дізнатися свій id можна, наприклад, написавши боту [@getmyid_bot](https://t.me/getmyid_bot)
* Запуск бота через файл bot.py `python bot.py`

### Локалізація

* З версії 1.1.0 у бот додано локалізацію для англійської, української та російської мови
* Для додавання перекладу на свою мову, зробіть наступне:
  1. перейдіть у папку з ботом
  2. активуйте віртуальне оточення:

     `source venv/bin/activate`
  3. створіть файл перекладу на вашу мову, де **{language}** - код мови за стандартом [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

     `pybabel init --input-file=tgbot/locales/tgbot.pot --output-dir=tgbot/locales --domain=tgbot --locale={language}`
  4. перекладіть рядки у файлі **locales/{language}/LC_MESSAGES/tgbot.po**
  5. скомпілюйте переклад командою:

     `pybabel compile --directory=tgbot/locales --domain=tgbot`
  6. перезапустіть бота
* При змінах рядків для перекладу в коді, вам потрібно буде повністю перестворити і скомпілювати файли 
  перекладу для всіх локалізацій:
  1. витягти рядки для перекладу з коду:

     `pybabel extract --input-dirs=./tgbot --output-file=tgbot/locales/tgbot.pot --sort-by-file --project=YoutubeMusicDownloadBot`
  2. створити файли перекладу для всіх локалізацій:

     `pybabel init --input-file=tgbot/locales/tgbot.pot --output-dir=tgbot/locales --domain=tgbot --locale={language}`
  3. скомпілювати переклади:

     `pybabel compile --directory=tgbot/locales --domain=tgbot`
* Детальніше про це можна прочитати в прикладі з документації [aiogram](https://docs.aiogram.dev/en/latest/examples/i18n_example.html)

### Розробники

* [Ringil](https://github.com/rin-gil)

### Ліцензії

* Вихідний код **Open Weather Bot** доступний за ліцензією [MIT](https://github.com/rin-gil/OpenWeatherBot/blob/master/LICENCE)
* Дані про прогноз погоди надані сервісом [OpenWeather](https://openweathermap.org/)
* Іконки погоди від [www.wishforge.games](https://freeicons.io/profile/2257) c [freeicons.io](https://freeicons.io/)
