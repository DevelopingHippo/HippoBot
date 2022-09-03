import os

import discord
from discord.ext import commands
import pictureGrabber


HippoBot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@HippoBot.event
async def on_ready():
    print('HippoBot is booting up')

@HippoBot.command()
async def ping(ctx):
    await ctx.channel.send("pinged me")

@HippoBot.command()
async def background(ctx):
    await ctx.channel.send("Sending cool picture...")
    allPages = pictureGrabber.findAllHtmlPages("https://4kwallpapers.com/random-wallpapers/")
    os.chdir(os.path.expanduser('../Pictures'))
    for page in allPages:
        url = page['href']
        pictureGrabber.photoDowloader(url, "https://4kwallpapers.com", 1)
        break
    await ctx.channel.send(file=discord.File('../Pictures/1-Blob-Background-iOS-.jpg'))



@HippoBot.event
async def on_message(message):
    await HippoBot.process_commands(message)

    if message.author == HippoBot.user:
        return

    if message.content == 'command':
        await message.channel.send('non-command was triggered')





HippoBot.run("MTAxNTM3NjUxNzMwNTQ2Njg5MA.GT72A9.ETmcUt5TOnyty4x7MRvzgoAoDSjcNr3cwIUKBM")
