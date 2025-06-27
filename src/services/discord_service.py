import discord

DISCORD_TOKEN = "your-discord-bot-token"
client = discord.Client()

async def send_discord_message(channel_id: int, text: str):
    channel = client.get_channel(channel_id)
    await channel.send(text)
