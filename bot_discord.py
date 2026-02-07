import os
import discord
from discord.ext import commands
import requests

# Récupère le token depuis une variable d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")

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
async def helllo(ctx):
    await ctx.send("Salut, je suis ton bot hébergé sur PythonAnywhere !")

@bot.command()
async def meteo(ctx):
    await ctx.send("La météo est bien !")
    
bot.run(TOKEN)


def get_weather(ville):
    # Exemple avec l'API Open-Meteo (Coordonnées de Paris par défaut)
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current_weather=true"
    response = requests.get(url)
    data = response.json()
    
    temp = data['current_weather']['temperature']
    return f"Il fait actuellement {temp}°C à Paris."

print(get_weather("Paris"))
