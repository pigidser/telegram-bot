# Telegram bot with accessing to database

- Run clickhouse in container
```bash
docker run --rm -d -p 8123:8123 -p 9000:9000 --name ch_db yandex/clickhouse-server
```
- Create virtual environment and install required libraries
```bash
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
```
- Create our database and table
```bash
python ddl.py
```
- Set token
```bash
export APP_TOKEN=<_telegram_token_>
```
- Run bot
```bash
python tg-bot.py
```
- Create docker image
```bash
docker build -t tg-bot-ch .
```
- Run bot in container
```bash
docker run --rm --name tg-bot -e APP_TOKEN=$APP_TOKEN tg-bot-ch
```

