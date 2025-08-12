import discord
from discord.ext import commands
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# === CONFIGURATION ===
CHANNEL_ID = 718948680467742783  # replace with your channel ID
MESSAGE = "Hello from Railway bot!"  # your message
TOKEN = os.environ["TOKEN"]  # Token from Railway environment variables

# === BOT SETUP ===
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

scheduler = AsyncIOScheduler()

async def send_scheduled_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(MESSAGE)
    else:
        print("⚠ Channel not found!")

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    scheduler.start()

# Example schedule: send message at 10:00 and 22:00 every day
TIMES = [
    (2, 50),
    (3, 0)
    (3, 10)
    (4, 0)
    (5, 0)
    (10, 0)
]
for hour, minute in TIMES:
    scheduler.add_job(send_scheduled_message, "cron", hour=hour, minute=minute)

bot.run(TOKEN)
