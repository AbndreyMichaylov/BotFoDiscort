from discord.ext import commands
from discord.ext.commands import Bot
import discord, time


Bot = commands.Bot(command_prefix = '!')
global allText
global BuferForallText
global DoubleNicks
global lvl
global member

global BDofNics

@Bot.event
async def on_ready():
    print('Bot is online')

@Bot.command(pass_context = True)
async def changename(ctx, self):
    allText  = str(ctx.message.content) #Получаем текст сообщения, вида !комманда стартовыйНик>итоговыйНик
    BuferForallText = (allText.split(' ')).pop(1)  # Буфер который делает список с отсеченным текстом
    DoubleNicks = BuferForallText.split('>')  # Два ника, первый цели, а второй результат
    lvl = ctx.message.server  # С какого уровня мы работаем
    member = discord.Server.get_member_named(lvl, name=DoubleNicks[0])  # Ищем на уровне челика с таким именем
    await Bot.change_nickname(member, nickname=DoubleNicks[1]) #Меняем ники
    await Bot.say('Ник: ' + DoubleNicks[0] + ' был изменён на ' + DoubleNicks[1])  # Выдаём сообщение о том что все хорошо


    print('Command is enable', BDofNics)

@Bot.command(pass_context =  True)
async def resetnames(ctx):
    print('200', BDofNics)

Bot.run('NTUzMzE2MDczNTg0MzI4NzQw.D2Mz2w.GVhRKk0z322FpKkGGX5rcFi1fVU')