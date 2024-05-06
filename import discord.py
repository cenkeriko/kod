import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$discord'):
        await message.channel.send("Discord, topluluk kurma için tasarlanmış bir anlık mesajlaşma ve dijital dağıtım platformudur. Aralık 2020 tarihi itibarıyla 300 milyondan fazla kayıtlı kullanıcısı ve aylık 140 milyon aktif kullanıcısı vardır. Discord Windows, macOS, Linux, iOS, Android ve Web tarayıcısı üzerinde çalışabilmektedir.https://discord.comdan kendinize bir hesap oluşturabilirsiniz")
    elif message.content.startswith('$udemy'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$udemy'):

    elif message.content.startswith('$minecraft'):

    elif message.content.startswith('$shazam'):

    elif message.content.startswith('$whatsapp'):

    elif message.content.startswith('$instagram'):

    elif message.content.startswith('$udemy'):

    elif message.content.startswith('$udemy'):

    elif message.content.startswith('$udemy'):



elif message.content.startswith('$udemy'):

elif message.content.startswith('$udemy'):


    else:
        await message.channel.send(message.content)

client.run("BOTUNUZUN TOKEN BURADA OLMALIDIR!")