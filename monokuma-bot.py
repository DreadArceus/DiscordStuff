import discord
from discord.ext import tasks
import time

target_channel = 772381855575441428

class CustomClient(discord.Client):
    async def on_ready(self):
        message_channel = client.get_channel(target_channel)
        await message_channel.send('I am here')
        print(f'Logged on as {self.user}!')
        kuma_time.start()
        with open('log.txt', 'r') as file:
            current_yday = file.readline().strip()
        x = time.gmtime().tm_yday
        if(f'{x}:' != current_yday and time.gmtime().tm_hour >= 1 and time.gmtime().tm_min > 30):
            with open('log.txt', 'w') as file:
                file.write(f'{x}:\n\n')
        elif(f'{x-1}:' != current_yday and time.gmtime().tm_hour <= 1 and time.gmtime().tm_min < 30):
            with open('log.txt', 'w') as file:
                file.write(f'{x-1}:\n\n')
        
    async def on_message(self, message):
        if(message.author == self.user or message.channel == client.get_channel(target_channel)):
            return
        with open('log.txt', 'a') as file:
            file.write(f'{message.author}: {message.content} || {message.created_at}\n\n')
        await message.channel.send('bruh, get a life')

client = CustomClient()

@tasks.loop(minutes=1)
async def kuma_time():
    kuma_channel = client.get_channel(target_channel)
    if(time.gmtime().tm_hour == 16 and time.gmtime().tm_min == 30):
        await kuma_channel.send('Mm, ahem, this is a school announcement. It is now 10 p.m.\nAs such, it is officially nighttime.\nSoon the doors to the dining hall will be locked and entry beyond that point is strictly prohibited.\nOkay then...sweet dreams, everyone! Good night, sleep tight, don\'t let the bed bugs bite...\n@everyone')
        print('Goodnight Kuma')
    if(time.gmtime().tm_hour == 1 and time.gmtime().tm_min == 30):
        await kuma_channel.send('Good morning, everyone! It is now 7 a.m. and nighttime is officially over! Time to rise and shine!\nGet ready to greet another beee-yutiful day!\n@everyone')
        print('Goodmorning kuma')
        with open('log.txt', 'w') as file:
            x = time.gmtime().tm_yday
            file.write(f'{x}:\n\n')
@kuma_time.before_loop
async def wait():
    await client.wait_until_ready()

client.run('NzcxMzk1NDc5NDYwMjQ5NjMx.X5rgBg.-kjqc_eVIK6LOJoIiKqel1ju3ks')