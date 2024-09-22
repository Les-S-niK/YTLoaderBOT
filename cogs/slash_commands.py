## Built-in modules:
from datetime import datetime

## Pip modules: 
from disnake import AppCommandInteraction
from disnake import Embed, Color
from disnake.ext.commands import Cog, Bot, Param
from disnake.ext.commands import slash_command

## Bot modules:
from bot_modules.bot_logger import command_logger

##* All slash_commands:
class Slash_commands(Cog):
    """Slashcommands cog for bot.
    Args:
        Cog (class): Cog class
    """
    
    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
    
    ##! /download_video
    @slash_command(name="download_video", description="Download some video from Youtube.")
    async def download_video(self, inter: AppCommandInteraction, url: str = Param(description="Enter videos url. that you will download.")) -> None:
        """Download video from Youtube using url.

        Args:
            url (str): Videos url.
        """
        ## Command logging.
        command_logger(command="/download_video", 
                username=inter.author.name, 
                user_id=inter.author.id, 
                channel_name=inter.channel.name, 
                guild_name=inter.guild.name,
                command_args=url
        )

        ## Send embed message.  
        await inter.send(
            embed=Embed(
                title="Videos information",
                color=Color.red(),
                timestamp=datetime.now(),
            )
            .add_field(
                name="`<------Main-info------>`",
                value="**Duration:** None\n**Views:** None\n**Likes:** None\n**Premiered:** None", 
                inline=False
            )
            .add_field(
                name="`<------Other-info------>`",    
                value="**Subscribers:** None\n**Channel name:** None\n**Description:** None", 
                inline=False
            )
            .set_footer(text=inter.guild.name)
            .set_image(url=None)
        )
        
    
## Setup bot cogs.        
def setup(bot: Bot) -> None:
    bot.add_cog(Slash_commands(bot=Bot))