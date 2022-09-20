# run.py
import discord
import asyncio

from to import Token

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('{0.user} 이 준비되었습니다!'.format(client))
    # 상태메시지 표시
    await client.change_presence(status=discord.Status.online, activity=discord.Game("국어"))


@client.event
async def on_message(message):
    if message.author == client.user:
        # 봇 자신이 보내는 메세지는 무시
        return

    if message.content == '안녕':
        await message.channel.send('안녕!')


# 보안상 다른 파일에서 토큰값을 가져옴
client.run(Token)
