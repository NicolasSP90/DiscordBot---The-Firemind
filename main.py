# Importing Discord Library
import aiohttp
import discord
from discord.ext import commands

# Import Scripts
from authentication import AuthFiremind

# Setting the Discord Bot
intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)


# Discord Bot is Ready
@client.event
async def on_ready():
    print("The Firemind has connected to your Discord Channel")


# Discord Bot Firemind Command
@client.command(name='Firemind', help='The Firemind Answer')
async def gpt(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt": "Answer as if you where a temperamental, genius, arrogant and ancient dragon "
                      "named Niv-Mizzet. The answer must be within 500 characters: " + prompt,
            "max_tokens": 500,
            # "presence_penalty": 0,
            # "best_of": 1,
        }
        headers = {"Authorization": f"Bearer {AuthFiremind.auth_openai()}"}
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            embed = discord.Embed(title="The Firemind says: ", description=response["choices"][0]["text"])
            await ctx.reply(embed=embed)


# Discord Bot GPT Command
@client.command(name='GPT', help='Regular Chat GPT Answer')
async def gpt(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt": "The answer must be within 500 characters: " + prompt,
            "max_tokens": 500,
        }
        headers = {"Authorization": f"Bearer {AuthFiremind.auth_openai()}"}
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            embed = discord.Embed(title="The Firemind says: ", description=response["choices"][0]["text"])
            await ctx.reply(embed=embed)

client.run(AuthFiremind.auth_discord())
