"""Sets commands for the bot"""

from aiogram import Dispatcher
from aiogram.types import BotCommand

from tgbot.middlewares.localization import i18n


_ = i18n.gettext  # Alias for gettext method


async def set_default_commands(dp: Dispatcher) -> None:
    """Sets bot commands for all available locales"""
    for lang_code in i18n.available_locales:
        await dp.bot.set_my_commands(
            commands=[
                BotCommand(command="start", description="▶️ " + _("Set weather forecast", locale=lang_code)),
                BotCommand(command="about", description="ℹ️ " + _("Bot info", locale=lang_code)),
                BotCommand(command="stop", description="⏹ " + _("Stop bot and delete data", locale=lang_code)),
                BotCommand(command="get", description="⏹ get weather"),
            ],
            language_code=lang_code,
        )
