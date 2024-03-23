# This example requires the 'message_content' intent.
from scrapper import Scraper
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def build_message(item):
    embed = discord.Embed(type="rich", title=item["name"])
    embed.description = item["brand"]
    embed.set_thumbnail(url=item["image"])
    embed.url = item["url"]
    embed.add_field(name="원래 가격", value=item["original_price"], inline=True)
    embed.add_field(name="할인 가격", value=item["sale_price"], inline=True)
    return embed


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith("!타임세일"):
        # 무신사 타임세일 결과를 출력합니다.
        scraper = Scraper()
        results = scraper.do()

        embeds = []

        #https://discordpy.readthedocs.io/en/stable/api.html?highlight=embed#discord.Embed.type
        for item in results:
            embeds.append(build_message(item))
            #embeds.append(embed)

        await message.channel.send(embeds=embeds)
        #await message.channel.send(embed=embed)         #비동기메시지 호출 - 매번 통신 요청이 발생하게됨, 비용, 느려짐 - 한번에 리스트 형태로 저장해서 한번에 응답하도록

        #await message.channel.send(results)

client.run('MTIxOTU1OTQ4NDgyMTczMzQyNg.Gke8z3.h3mUVgzs08lXl5HcQC6hh0_I9mUYGpqVyaNHXU')
