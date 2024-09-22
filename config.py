## Built-in modules:
from os import getenv
from os import PathLike
from os.path import dirname

## Pip modules:
from dotenv import load_dotenv
from disnake.activity import Activity

## Load enviroment.
load_dotenv()

## Get bots token.
TOKEN: str = getenv('TOKEN')

## Configuration.
COMMAND_PREFIX: str = "!"
DESCRIPTION: str = "Bot for download youtube videos." 
OWNER_ID: list[int] = [989213469595283496, 1250875663108538555]
ACTIVITY: Activity = Activity(
    name="Youtube",
)

## Other constancts.
BOT_NAME: str = "YTLoaderBOT"
DIR_PATH: PathLike = dirname(__file__)
