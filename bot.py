import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, MissingPermissions
from discord import Activity, ActivityType

prefix = "/", "*"
Bot = commands.Bot(command_prefix=prefix)

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def say(ctx, *,arg):
    deleted = await ctx.message.channel.purge(limit=1)
    await ctx.send(arg)

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def saytwo(ctx, *,arg):
    deleted = await ctx.message.channel.purge(limit=1)
    await ctx.send(embed = discord.Embed(description = arg))

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx, user:discord.Member, time:int, *, reason=None):
    role = discord.utils.get(user.guild.roles, name="Muted")
    await ctx.send(f'{user} получил мут на {time} минут.\nПричина: {reason}') # перенос строки осуществляется добавлением: /n, а не ENTER
    await user.add_roles(role)
    await usr.move_to(None)
    await asyncio.sleep(time * 60)
    await user.remove_roles(role)

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx, *, user:discord.Member):
    text = name=f"Участник {user} был размучен." 
    role = discord.utils.get(ctx.guild.roles, name="Muted") 
    await user.remove_roles(role)
    await ctx.channel.send(text)


@Bot.event
async def on_ready():
    print("Бот был успешно включён!")
    await Bot.change_presence(status=discord.Status.idle, activity=discord.Game(""))

Bot.run(process.env.BOT_TOKEN)