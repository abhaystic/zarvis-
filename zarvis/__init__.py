from telethon import TelegramClient
import logging
import time
openai_key="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"


api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="6022512207:AAElOxRdzAoeXwBukMMCV1QJ9kq7quYLaLE"

bot=TelegramClient("zarvis_bot",api_id,api_hash).start(bot_token=bot_token)