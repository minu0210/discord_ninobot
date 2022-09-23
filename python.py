# run.py
from socket import MsgFlag
from ssl import CHANNEL_BINDING_TYPES
import discord
import asyncio

from to import Token

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('{0.user} 이 준비되었습니다!'.format(client))
    # 상태메시지 표시
    await client.change_presence(status=discord.Status.online, activity=discord.Game(""))


@client.event
async def on_message(message):
    if message.author == client.user:
        # 봇 자신이 보내는 메세지는 무시
        return

    if message.content == '안녕':
        channel = message.channel

        await message.channel.send('https://pbs.twimg.com/media/FcnWOQaaEAAU318.jpg')
        await message.channel.send(f'안녕 {message.author.name}!\n여기는 세카이야\n너의 마음으로 이루어진 곳이지!')
        await asyncio.sleep(6)
        await message.channel.send('응.')


# 보안상 다른 파일에서 토큰값을 가져옴
client.run(Token)
