import discord
import openai
import os


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))


print('over')


# openai.api_key_path = '/Users/hiro002/discord bot/keys.env'

openai.api_key = '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'

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = input("Human: ")
original = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

response = openai.Completion.create(
  engine="davinci",
  prompt=original + response + '\n',
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)
