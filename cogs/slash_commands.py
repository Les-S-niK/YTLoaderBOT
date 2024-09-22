## Built-in modules:
from datetime import datetime

## Pip modules: 
from disnake import AppCommandInteraction, Color
from disnake import Embed, File
from disnake.errors import HTTPException
from disnake.ext.commands import Cog, Bot, Param
from disnake.ext.commands import slash_command

## Bot modules:
from bot_modules.bot_logger import command_logger, error_logger
from bot_modules.yt_loader.youtube_downloader import YouTubeLoader

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
        await inter.response.defer()
        
        ## Command logging.
        command_logger(command="/download_video", 
                username=inter.author.name, 
                user_id=inter.author.id, 
                channel_name=inter.channel.name, 
                guild_name=inter.guild.name,
                command_args=url
        )
        ## Class YoutubeLoader instance.
        youtube_loader: YouTubeLoader = YouTubeLoader(
            url=url,
            is_mp3=False
        )
        
        ## Send embed message.  
        await inter.send(
            embed=Embed(
                title="Video information",
                color=Color.red(),
                timestamp=datetime.now(),
            )
            .add_field(
                name="`<------Main-info------>`",
                value=f"""**Name:** {youtube_loader.video_name}
                    **Duration:** {youtube_loader.video_duration}
                    **Views:** {youtube_loader.video_views}
                    **Premiered:** {youtube_loader.video_premiered}""", 
                inline=False
            )
            .set_footer(text="Video is downloading... Please, wait.")
            .set_image(url=youtube_loader.video_img_url)
        )
        ## Download file.
        youtube_loader.download_file()
        downloaded_file: File = File(f"{youtube_loader.FILES_PATH}{youtube_loader.filename}")
        
        try:       
            ## Send downloaded file.
            await inter.send(content="## Video was downloaded:", file=downloaded_file)
            youtube_loader.remove_current_file()
            
        ## If file is very large:
        except HTTPException as error:
            await inter.send(embed=Embed(
                    description=f"""🛑 Sorry {inter.author.mention}, but **file is very large to send.**""",
                    color=Color.red(),
                    timestamp=datetime.now()
                ).set_footer(text=inter.guild.name), ephemeral=True
            )
            error_logger(error=error)


## Setup bot cogs.        
def setup(bot: Bot) -> None:
    bot.add_cog(Slash_commands(bot=Bot))