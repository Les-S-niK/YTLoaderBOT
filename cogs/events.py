## Built-in modules:
from datetime import datetime

## Pip modules:
from disnake import Embed, Color, AppCommandInteraction
from disnake.errors import InteractionResponded, InteractionTimedOut
from disnake.ext.commands import Cog, Bot
from disnake.ext.commands import Context
from disnake.ext.commands.errors import CommandNotFound, MissingPermissions, NotOwner

## Bot modules
from bot_modules.bot_logger import on_ready_logger, error_logger

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
        on_ready_logger()
    
    ## Calls on error in command.
    @Cog.listener(name="on_command_error")
    async def on_command_error(self, ctx: Context, error: Exception) -> None:
        """Handler of the commands errors.

        Args:
            error (Exception): error
        """
        ## Author mention.
        author_mention: str = ctx.author.mention
            
        ## If Command isn't found.
        if isinstance(error, CommandNotFound):
            await ctx.send(
                embed=Embed(
                    description=f"""🛑 Sorry {author_mention}, but this command is **not found!**""",
                    color=Color.red(),
                    timestamp=datetime.now()
                ).set_footer(text=ctx.guild.name)
            )
            
        ## If member haven't permissions or member isn't owner.
        elif isinstance(error, MissingPermissions) or isinstance(error, NotOwner) :
            await ctx.send(
                embed=Embed(
                    content=f"""🛑 Sorry {author_mention}, but you **haven't permissions** to use command: **{ctx.command.name}**!""",
                    color=Color.red(),
                    timestamp=datetime.now()
                ).set_footer(text=ctx.guild.name)
            )
            
        ## Other errors
        else:
            await ctx.send(
                embed=Embed(
                    content=f"""🛑 Sorry {author_mention}, but then using the command **{ctx.command.name}** error occurs:\n{error}!""",
                    color=Color.red(),
                    timestamp=datetime.now()
                ).set_footer(text=ctx.guild.name)
            )
            error_logger(error=error)
        
    ## Calls on error in slash_command.
    @Cog.listener(name="on_slash_command_error")
    async def on_slash_command_error(self, inter: AppCommandInteraction, error: Exception) -> None:
        """Errors handler in slash_commands

        Args:
            inter (AppCommandInteraction): AppCommandInteraction
            error (Exception): error
        """
        ## Author mention.
        author_mention: str = inter.author.mention

        ## If commands responce have error.
        if isinstance(error, InteractionResponded):
            await inter.send(
                embed=Embed(
                    description=f"""🛑 Sorry {author_mention}, but then using this command error occurs:\n{error}!**""",
                    ephemeral=True,
                    color=Color.red(),
                    timestamp=datetime.now()
                ).set_footer(text=inter.guild.name)
            )
            
        ## If waiting time is out.
        elif isinstance(error, InteractionTimedOut):
            await inter.send(
                embed=Embed(
                    description=f"""🛑 Sorry {author_mention}, **waiting time is out!**""",
                    ephemeral=True,
                    color=Color.red(),
                    timestamp=datetime.now()
                ).set_footer(text=inter.guild.name)
            )
        ## Other errors
        else:
            await inter.send(
                embed=Embed(
                    description=f"""🛑 Sorry {author_mention}, but then using this command error occurs:\n{error}!**""",
                    ephemeral=True,
                    color=Color.red(),
                    timestamp=datetime.now()
                ).set_footer(text=inter.guild.name)
            )
            error_logger(error=error)
## Setup bot cogs.
def setup(bot: Bot) -> None:
    bot.add_cog(Events(bot=bot))