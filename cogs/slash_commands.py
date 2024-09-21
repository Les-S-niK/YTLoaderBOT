## Built-in modules:

## Pip modules:
from disnake import Embed, Color, Member
from disnake.ext.commands import Cog, Bot
from disnake.ext.commands import slash_command

##* All slash_commands:
class Slash_commands(Cog):
    """Slashcommands cog for bot.
    Args:
        Cog (class): Cog class
    """
    
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
    
## Setup bot cogs.        
def setup(bot: Bot) -> None:
    bot.add_cog(Slash_commands(bot=Bot))