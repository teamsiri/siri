from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import (BANNED_USERS, lyrical, YAFA_NAME,
                    YAFA_CHANNEL, CHANNEL_SUDO)
from AnonXMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
                [InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="help_callback hb11",
                )],
                [InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb10",
                ),InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb12",
                )
            ],[InlineKeyboardButton(
                text=f'{YAFA_NAME}',
                url=f"https://t.me/{CHANNEL_SUDO}",
            )],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
