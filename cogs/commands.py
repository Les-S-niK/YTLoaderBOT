## Built-in modules:

## Pip nodules:
from disnake import Embed, Color
from disnake.ext.commands import Cog, Bot
from disnake.ext.commands import Context
from disnake.ext.commands import command, is_owner

## Bot modules:
from config import COMMAND_PREFIX, BOT_NAME
from bot_modules.bot_logger import command_logger

##* All commands:
class Commands(Cog):
    """Commands cog for bot.
    Args:
        Cog (class): Cog class
    """
    
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    ## !exit
    @command(name="exit", description="Turn off the bot.", brief=f"{COMMAND_PREFIX}exit")
    @is_owner() 
    async def exit(self, ctx: Context) -> None:
        """Exit command.
        
        Args:
            ctx (Context): Context object.
        """
        ## Command logging.
        command_logger(command="!exit", 
                username=ctx.author.name,
                user_id=ctx.author.id, 
                channel_name=ctx.channel.name, 
                guild_name=ctx.guild.name, 
                command_args=None)
        
        ## Send a message in current chat.
        await ctx.send(
            embed=Embed(
                color=Color.green(),
                title=f"<--------------------------------------->\
                    \n          **{BOT_NAME}** is offline now!\
                    \n<--------------------------------------->"
            )
        )
        
        ## Turn off the Bot.
        exit()
        
## Setup bot cogs.         
def setup(bot: Bot) -> None:
    bot.add_cog(Commands(bot=Bot))