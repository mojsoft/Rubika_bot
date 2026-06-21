from rubka import Robot
from rubka.context import Message
import os

bot = Robot(token=os.getenv("BCFCAI0HWIZGCAWHUGMRDCUOQLQTCQBDOAGALUQQQXISVAQPFVHHUNDTZEBMOWAY"))

@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):
    await message.reply("سلام! ربات روشن شد! ✅")

bot.run()