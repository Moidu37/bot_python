import os
import discord
from discord.ext import commands

# Récupère le token depuis une variable d'environnement
TOKEN = "MTQ2OTQxOTY4MDc5NDkzNTU0MQ.GHmc72.x11X82IuUh-cBdevvG50PDETcmgl-I4H4vwTdk"

# Définir les intents (permissions du bot)
intents = discord.Intents.default()
intents.message_content = True

# Créer le bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

@bot.command()
async def salut(ctx):
    await ctx.send("Salut, je suis ton bot hébergé sur PythonAnywhere !")
    
bot.run(TOKEN)
