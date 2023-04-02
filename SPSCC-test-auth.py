import discord 
import csv

client = discord.Client()
CSV_FILE_PATH = "C:\Users\darth\Downloads\Emails2.csv"
ROLE_NAME = "Authorized"

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Check that the message is in the text channel we're interested in
    if message.channel.name == "authorization":
        with open(CSV_FILE_PATH, 'r') as csv_file:
            reader = csv.reader(csv_file)
            # Loop over the rows in the CSV file
            for column in reader:
                # Check if the email in the row matches the message content
                if column[1] == message.content:
                    # Find the "Verified" role
                    for role in message.guild.roles:
                        if role.name == ROLE_NAME:
                            # Assign the role to the message author
                            await message.author.add_roles(role)
                            print(f"{message.author.name} was assigned the {ROLE_NAME} role")
                            return

# Replace the token with your bot's token
client.run('Get your own lol')
