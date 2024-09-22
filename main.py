## Pip modules:
from disnake import Intents
from disnake.ext.commands import Bot

## Bot modules:
from config import TOKEN, COMMAND_PREFIX, DESCRIPTION, OWNER_ID, ACTIVITY
from bot_modules.bot_logger import start_logger, error_logger

## Create a bot instance:
bot: Bot = Bot( 
    command_prefix=COMMAND_PREFIX,
    help_command=None, 
    description=DESCRIPTION,
    owner_ids=OWNER_ID,
    intents=Intents.all(),
    activity=ACTIVITY
)

## loading all extensions.
bot.load_extensions('cogs/')
    
## Turn on this Bot.
try:
    start_logger()
    bot.run(token=TOKEN)
    
except Exception as launch_error:
    error_logger(launch_error)