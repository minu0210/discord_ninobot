#run.py
import discord
from token import Token

intents = discord.Intents.all()
# intents.typing = True
# intents.presences = True
# intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{0.user} 이 준비되었습니다!'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game("")) # 상태메시지 표시

@client.event
async def on_message(message):
    if message.author == client.user: 
        # 봇 자신이 보내는 메세지는 무시
        return

    if message.content == '안녕':
        await message.channel.send('안녕!')


client.run('Token') # 보안상 다른 코드에서 토큰값을 가져옴