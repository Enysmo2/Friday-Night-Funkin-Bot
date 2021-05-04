token = 'your token.'
import discord
from discord.ext import commands
import os
import asyncio
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

os.chdir(r"C:\Users\Semyon\Desktop\code\other")

bot = discord.Client()
bot = commands.Bot(command_prefix='!')#you can change it to anything you want
bot.remove_command('help')#remove if you want default !help command

@bot.command()
async def play(ctx):
	l = "◀️"
	d = "🔽"
	u = "🔼"
	r = "▶️"
	ent = "➡️"
	game = await ctx.send("Press on reactions to play the game!")
	await game.add_reaction(l)
	await game.add_reaction(d)
	await game.add_reaction(u)
	await game.add_reaction(r)
	await game.add_reaction(ent)
	@bot.event
	async def on_reaction_add(reaction, user):
		if reaction.emoji == l:
			keyboard.press(Key.left)
			time.sleep(0.50)
			keyboard.release(Key.left)
			await game.remove_reaction(reaction, user)
		elif reaction.emoji == d:
			keyboard.press(Key.down)
			time.sleep(0.50)
			keyboard.release(Key.down)
			await game.remove_reaction(reaction, user)
		elif reaction.emoji == u:
			keyboard.press(Key.up)
			time.sleep(0.50)
			keyboard.release(Key.up)
			await game.remove_reaction(reaction, user)
		elif reaction.emoji == r:
			keyboard.press(Key.right)
			time.sleep(0.50)
			keyboard.release(Key.right)
			await game.remove_reaction(reaction, user)
		elif reaction.emoji == ent and user.id!=839058586251427900:
			keyboard.press(Key.enter)
			time.sleep(1)
			keyboard.release(Key.enter)
			await game.remove_reaction(reaction, user)

bot.run(token)
