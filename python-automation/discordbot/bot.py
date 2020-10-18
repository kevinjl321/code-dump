import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '/')
status = cycle(['with yokuchi', 'with makuchi'])

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status = discord.Status.online, activity = discord.Game("with yokuchi"))
    print('Kuchi is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has slid into the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has skrt skrt outta the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Bot latency is: {round(client.latency * 1000)} ms')

@client.command(aliases = ['8ball'])
async def _8ball(ctx, *, question):
    responses =  ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            return

@tasks.loop(seconds = 60)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command does not exist.")

client.run('')
