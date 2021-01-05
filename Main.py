import discord
import os
import json
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot
import random

bot = discord.Client()

bot = commands.Bot(command_prefix='&')
bot.remove_command('help')

# this was the first thing I added and is technically the main feature of the bot 
@bot.event
async def on_message(message):
	blacklist = json.load(open(f'{os.getcwd()}/blacklist.json', 'r'))
	try:
		if blacklist[f'{message.author.id}'] == 'blacklisted':
			return False
	except KeyError:
		pass
	if message.author.id is bot.user.id:
		return False
	elif message.content.lower().startswith("bruh"):
		await message.channel.send("Bruh")
	await bot.process_commands(message)

# I spent so much god damn time trying to add this simple command and I feel so ashamed about it 
@bot.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, said):
	await ctx.message.delete()
	await ctx.send(said)


@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Fapping"))


@bot.command()
@commands.has_permissions(manage_messages=True)
async def poll(ctx, question, option1=None, option2=None):
	blacklist = json.load(open(f'{os.getcwd()}/blacklist.json', 'r'))
	try:
		if blacklist[f'{ctx.author.id}'] == 'blacklisted':
			await ctx.send(
			    "<a:spin:774262875275395112> You are blacklisted <a:spin:774262875275395112>"
			)
			return False
	except KeyError:
		pass
	if option1 == None and option2 == None:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```\n**✅ = Yes** **❎ = No**")
		await message.add_reaction('✅')
		await message.add_reaction('❎')
	elif option1 == None:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```\n**✅ = {option1}****❎ = No**")
		await message.add_reaction('✅')
		await message.add_reaction('❎')
	elif option2 == None:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```\n**✅ = Yes** **❎ = {option2}**")
		await message.add_reaction('✅')
		await message.add_reaction('❎')
	else:
		await ctx.channel.purge(limit=1)
		message = await ctx.send(
		    f"```New poll: \n{question}```**✅ = {option1}**\n**={option2}**")
		await message.add_reaction('✅')
		await message.add_reaction('❎')


@bot.command()
async def  bruh(ctx):
	blacklist = json.load(open(f'{os.getcwd()}/blacklist.json', 'r'))
	try:
		if blacklist[f'{ctx.author.id}'] == 'blacklisted':
			await ctx.send(
			    "<a:spin:774262875275395112> You are blacklisted <a:spin:774262875275395112>"
			)
			return False
	except KeyError:
		pass


@bot.command()
async def blacklist(ctx, user: discord.Member):
	if ctx.author.id == 661369623383375873 or ctx.author.id == 526470337295024148:
		with open(f'{os.getcwd()}/blacklist.json', 'r') as f:
			blacklist = json.load(f)

			blacklist[str(user.id)] = f'blacklisted'

			with open(f'{os.getcwd()}/blacklist.json', 'w') as f:
				json.dump(blacklist, f, indent=4)

		await ctx.send(f"Added {user.mention} to blacklist.")
	else:
		await ctx.send(
		    "<a:spin:774262875275395112> Okay non-bot owner <a:spin:774262875275395112>"
		)
# the next few commands are all for discord emotes that I liked
@bot.command()
async def mario(ctx):
 await ctx.message.delete()
 await ctx.send('<a:mario:775164352448692234>')

@bot.command()
async def no(ctx):
 await ctx.message.delete()
 await ctx.send('<a:pogdisagree:776458393367740416>')
 
@bot.command()
async def nut(ctx):
 await ctx.message.delete()
 await ctx.send('<a:nut:737318888819130369>')
 
@bot.command()
async def nugget(ctx):
 await ctx.message.delete()
 await ctx.send('<a:nugget:759933698614755389>')
 
@bot.command()
async def wide(ctx):
 await ctx.message.delete()
 await ctx.send('<a:kiryuWide1:775080575517065256><a:kiryuWide2:775081151018041385>')
 
@bot.command()
async def ban(ctx):
 await ctx.message.delete()
 await ctx.send('<a:yoshiban:714516887828168738>')

@bot.command()
async def penis(ctx):
 await ctx.message.delete()
 await ctx.send('<a:penis:771537465344393246>')

keep_alive()
token = os.environ['DISCORD_BOT_TOKEN']
bot.run(token)
