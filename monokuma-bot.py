import discord
from discord.ext import tasks
import time

target_channel = 771402388116471870

class CustomClient(discord.Client):
    async def on_ready(self):
        message_channel = client.get_channel(target_channel)
        await message_channel.send('I am here')
        print(f'Logged on as {self.user}!')
        kuma_time.start()
    async def on_message(self, message):
        if(message.author == self.user):
            return
        print(f'Message from {message.author}: {message.content}')
        await message.channel.send('bruh, get a life')

client = CustomClient()

@tasks.loop(minutes=1)
async def kuma_time():
    await client.wait_until_ready()
    kuma_channel = client.get_channel(target_channel)
    if(time.gmtime().tm_hour == 8 and time.gmtime().tm_min == 5):
        await kuma_channel.send('Mm, ahem, this is a school announcement. It is now 10 p.m.\nAs such, it is officially nighttime.\nSoon the doors to the dining hall will be locked and entry beyond that point is strictly prohibited.\nOkay then...sweet dreams, everyone! Good night, sleep tight, don\'t let the bed bugs bite...')
        print('Goodnight Kuma')
    if(time.gmtime().tm_hour == 1 and time.gmtime().tm_min == 30):
        await kuma_channel.send('Good morning, everyone! It is now 7 a.m. and nighttime is officially over! Time to rise and shine!\nGet ready to greet another beee-yutiful day!')
        print('Goodmorning kuma')

client.run('NzcxMzk1NDc5NDYwMjQ5NjMx.X5rgBg.-kjqc_eVIK6LOJoIiKqel1ju3ks')