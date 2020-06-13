from discord.ext import commands
import discord
import time

def get_prefix(client, message):

    prefixes = ['*']   


    return commands.when_mentioned_or(*prefixes)(client, message)

client = discord.Client()
bot = commands.Bot(                         
    command_prefix=get_prefix,              
    description='Bot De Polo 83',  
    owner_id=319511103736512512,            
    case_insensitive=True                   
)



cogs = ['cogs.solo', 'cogs.duo', 'cogs.soloprivate', 'cogs.duoprivate', 'cogs.sectionprivate', 'cogs.arene', 'cogs.areneprivate', 'cogs.channels', 'cogs.messages', 'cogs.test', 'cogs.roles', 'cogs.reactions', 'cogs.automatic', 'cogs.attente']
@bot.event
async def on_ready():                                    
    print(f'Connecté en tant que {bot.user.name} - {bot.user.id}')  
    for cog in cogs:
        bot.load_extension(cog)
    return

bot.run('TON TOLKEN x)', bot=True, reconnect=True)
