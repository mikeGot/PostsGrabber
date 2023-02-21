from __future__ import annotations

import json
from datetime import datetime

from loguru import logger
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

from core.configuration import settings
from db_helper import insert_to_db
from models import Post

client = TelegramClient(settings.username, settings.api_id, settings.api_hash)
client.start()

post_count = 10


async def dump_all_messages(channel) -> list[Post]:
    """Записывает json-файл с информацией о всех сообщениях канала/чата"""
    offset_msg = 0  # номер записи, с которой начинается считывание

    all_messages = []

    history = await client(
        GetHistoryRequest(
            peer=channel,
            offset_id=offset_msg,
            offset_date=None,
            add_offset=0,
            limit=post_count,
            max_id=0,
            min_id=0,
            hash=0,
        )
    )
    if history.messages:
        messages = history.messages
        for message in messages:
            all_messages.append(Post(**message.to_dict()))

    return all_messages


async def main():
    for name, url in settings.sites.items():
        channel = await client.get_entity(url)
        res = await dump_all_messages(channel)
        insert_to_db(name, res)
        logger.info(f"Записи из канала {name} успешно добавлены")


with client:
    client.loop.run_until_complete(main())
