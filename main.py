import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='_', intents=intents, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Playing(name="_help"))
    print(f'We have infiltrated the headquarters as {client.user}')

@client.command()
async def ping(ctx):
    
    await ctx.send("Pong!")


# SOMEONE DO THIS LATER
@client.command()
async def help(ctx):
    
    await ctx.send('i can\'t help sry')

@client.command()
async def say(ctx, msg=None):
    if ctx.author.id == 773204048751886377 or ctx.author.id == 701621878631956572:
        await ctx.send(msg)
    else:
        await ctx.send('<:chuckle:1282380972087574609>')

#kick command start
@client.command()
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, reason):
    await ctx.guild.kick(member)
    if reason == None:
        em = discord.Embed(title=f"User {member.mention} Kicked")
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title=f"User {member.mention} Kicked", description=f"Reason: {reason}")
        await ctx.send(embed=em)
#kick command end

#ban command start
@client.command()
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, reason):
    await ctx.guild.ban(member)
    if reason == None:
        em = discord.Embed(title=f"User {member.mention} Banned")
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title=f"User {member.mention} Banned", description=f"Reason: {reason}")
        await ctx.send(embed=em)
#ban command end

#kik command start
@client.command()
async def kik(ctx, member:discord.Member, reason):
    if reason == None:
        em = discord.Embed(title=f"User {member.mention} Kicked")
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title=f"User {member.mention} Kicked", description=f"Reason: {reason}")
        await ctx.send(embed=em)
#kik command end

#bam command start
@client.command()
async def bam(ctx, member:discord.Member, reason):
    if reason == None:
        em = discord.Embed(title=f"User {member.mention} Banned")
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title=f"User {member.mention} Banned", description=f"Reason: {reason}")
        await ctx.send(embed=em)
#bam command end


client.run(os.environ['DISCORD_TOKEN'])
