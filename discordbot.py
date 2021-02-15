import discord
client= discord.Client()
keywords=["alone","gm","pls meme","tf"]
spam_content="US/Mexican border scene.We hear light chatter and Mexican folk music. From overhead we hover on a sign“You areleaving Mexico” then on a well groomed Latin wearing a capmaking his way through the line and into America. He exits the turnstiles to the street and into the backof a non-descriptcar. TINO knows the driverandthey exchange pleasantries as theydrive away. Tino and MARTINEare sitting on a truck tailgate in a desert café parking lot. Tino’s driver is leaning on the side of the trucksmoking.Allthree arecomfortable with each other butkeepa sharp eye out. We noticeTino and Martine are wearing caps with official logo’s on them.Tino and his driver droveall night. They round an alley in a run down neighborhood and stop beside a gatewherePACO, a Mexican with aneye tattoo greets themgang style. The truck is parked in the yard. Tino and his driver disappear thru the back door of the house.Another latin appears and helpsPacoremove the trucks contents to the garage."
spam=spam_content.split(".")

@client.event
async def on_message(message):
    if keywords[1] in message.content:
        await message.channel.send("Gm bestus")
    if keywords[2] in message.content:
        await message.channel.send("i aint got any meme nigga")
    if keywords[3] in message.content:
        await message.channel.send("what the fuck is going on here")
    if keywords[0] in message.content:
        for i in range(len(spam)):
            await message.channel.send(spam[i])

client.run("NzgyNTEyNzM3Njk5MjMzODIy.X8NRxw.Ltf6ARlxZs400921scp7mGKRL0E")
# https://discord.com/api/oauth2/authorize?client_id=782512737699233822&permissions=0&scope=bot