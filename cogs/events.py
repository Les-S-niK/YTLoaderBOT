## Built-in modules:

## Pip modules:
from disnake.ext.commands import Cog, Bot
from disnake.ext.commands import Context

## Bot modules
from bot_modules.bot_logger import on_ready_logger

##* All events:
class Events(Cog):
    """Events cog for bot.

    Args:
        Cog (class): Cog class.
    """
    
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        
    ## Starts if bot is ready to work.
    @Cog.listener(name="on_ready")
    async def on_ready(self) -> None:
        """Event when bot is ready.
        """
        on_ready_logger()
        
## Setup bot cogs.
def setup(bot: Bot) -> None:
    bot.add_cog(Events(bot=bot))