
## Pip modules:
from loguru import logger


def init_youtube_request(
    url: str,
    title: str,
    video_id: int,
) -> None:
    """Logging the initialization of downloader.

    Args:
        url (str): video url.
        title (str): video title.
        video_id (int): video_id.
    """
    LOG_TEXT: str = f"""
    <<< INITIALIZATION THE DOWNLOADER >>>
    <<< URL: {url} >>>
    <<< TITLE: {title} >>>
    <<< VIDEO ID: {video_id} >>>
    """
    logger.debug(LOG_TEXT)


def downloading_completed(
    filename: str 
) -> None:
    LOG_TEXT: str = f"""
    <<< FILE DOWNLOADED >>> 
    <<< FILENAME: {filename} >>>
    """
    logger.info(LOG_TEXT)