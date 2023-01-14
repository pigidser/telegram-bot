import logging
import os
from clickhouse_driver import Client
import pandas as pd
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO
)

APP_TOKEN = os.environ.get("APP_TOKEN")

bot = Bot(token=APP_TOKEN)
dp = Dispatcher(bot)

connection = Client(
    host="localhost",
    user="default",
    password="",
    port=9000,
    database="todo"
)

@dp.message_handler(commands="all")
async def all_tasks(payload: types.Message):
    ch_all_data = connection.execute("SELECT text, status FROM todo.todo")

    await payload.reply(
        f"```{pd.DataFrame(ch_all_data, columns=['text','status']).to_markdown()}```",
        parse_mode="Markdown"
    )

@dp.message_handler(commands="add")
async def all_task(payload: types.Message):
    text = payload.get_args().strip()

    connection.execute(
        "INSERT INTO todo.todo (text, status) VALUES (%(text)s, %(status)s)",
        {"text": text, "status": "active"}
    )

    logging.info(f"Added task to table - {text}")
    await payload.reply(f"Added task: *{text}*", parse_mode="Markdown")

@dp.message_handler(commands="done")
async def all_task(payload: types.Message):
    text = payload.get_args().strip()
    connection.execute(
        "ALTER TABLE todo.todo UPDATE status = 'complete' WHERE text = %(text)s",
        {"text": text}
    )

    logging.info(f"Task is completed - {text}")
    await payload.reply(f"Completed: *{text}*", parse_mode="Markdown")

if __name__ == "__main__":
    executor.start_polling(dp)
