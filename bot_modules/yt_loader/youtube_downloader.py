""" Made by Les-S-nik """

## Built-in modules:
from os import PathLike
from os.path import exists
from os import mkdir, remove

## Pip modules:
from pytubefix import YouTube, Stream, StreamQuery

## Bot modules:
from config import DIR_PATH
from bot_modules.yt_loader.downloader_logger import init_youtube_request, downloading_completed


class YouTubeLoader(object):
    """Load YouTube video and audio files with user options.

    Args:
        object: basic inheritance class in python3.
    """
    def __init__(
        self,
        url: str,
        is_mp3: bool = False,
    ) -> None:
        """Init YouTube video and audio downloader.

        Args:
            url (str): video url to download.
            is_high_resolution (bool): Optional. Default to false. high video resolution to download.
            is_mp3 (bool): Optional. Default to false. download mp3 file.
        """
        self.URL: str = url
        self.FILES_PATH: PathLike = f"{DIR_PATH}//bot_modules//yt_loader//files"
        self._is_mp3: bool = is_mp3
        self._youtube_video: YouTube = YouTube(url=self.URL)
        self.video_name: str = self._youtube_video.title
        self.video_views: str = self._youtube_video.views
        self.video_img_url: str = self._youtube_video.thumbnail_url
        self.video_id: str = self._youtube_video.video_id
        self._download_file(self._init_youtube_streams())


    def _init_youtube_streams(self) -> None:
        """Initialize the YouTube video streams to download.

        Returns:
            Stream: streams object.
        """
        init_youtube_request(
            url=self.URL,
            title=self.video_name,
            video_id=self.video_id
        )
        youtube_streams: StreamQuery = self._youtube_video.streams
        
        if self._is_mp3:
            return youtube_streams.get_audio_only()
        else:
            return youtube_streams.get_lowest_resolution()


    def _download_file(
        self,
        stream: Stream,
    ) -> None:
        if not exists(self.FILES_PATH):
            mkdir(self.FILES_PATH)
        
        file_postfix: str = "mp3" if self._is_mp3 else "mp4"
        filename: str = f"{self.video_id}.{file_postfix}"
        
        stream.download(
            output_path=self.FILES_PATH,
            filename=filename
        )
        downloading_completed(
            filename=filename
        )
        return None


    def remove_current_file(self) -> None:
        """
        Remove downloaded file.
        """
        remove(f"{self.FILES_PATH}//{self.video_id}")