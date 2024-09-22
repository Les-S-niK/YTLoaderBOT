""" Made by Les-S-nik """

## Built-in modules:
from os import PathLike
from os.path import exists
from os import mkdir, remove

## Pip modules:
from pytubefix import YouTube, Stream, StreamQuery
from datetime import datetime

## Bot modules:
from bot_modules.bot_logger import init_youtube_request, downloading_completed
from bot_modules.yt_loader.exceptions import DownloadError
from config import DIR_PATH

class YouTubeLoader(object):
    """Load YouTube video and audio files with user options.

    Args:
        object: basic inheritance class in python3.
    """
    def __init__(self, url: str, is_mp3: bool = False) -> None:
        """Init YouTube video and audio downloader.

        Args:
            url (str): video url to download.
            is_mp3 (bool): Optional. Default to false. download mp3 file.
        """
        
        self.URL: str = url
        self.FILES_PATH: PathLike = f"{DIR_PATH}\\bot_modules\\yt_loader\\files\\"
        self._is_mp3: bool = is_mp3
        self._youtube_video: YouTube = YouTube(url=self.URL)
        self.video_name: str = self._youtube_video.title
        self.video_views: str = self._youtube_video.views
        self.video_img_url: str = self._youtube_video.thumbnail_url
        self.video_duration: str = self.video_duration_settings(self._youtube_video.length)
        self.video_id: str = self._youtube_video.video_id
        self.video_premiered: datetime = self._youtube_video.publish_date
        self.filename: str = f"{self.video_id}.mp3" if self._is_mp3 else f"{self.video_id}.mp4"
        
            
    @staticmethod 
    def video_duration_settings(duration: float) -> str:
        ## Writing video duration.
        if duration >= 60:
            minutes: int = duration // 60
            seconds: int = duration % 60 
        
            if seconds < 10: 
                seconds: str = f"0{seconds}"
            if minutes < 10:
                minutes: str = f"0{minutes}"
            duration = f"{minutes}:{seconds}"
            
        else: 
            duration: str = f"0:{duration}"

        return duration


    def download_file(self) -> None:
        """Download mp3 / mp4 file from YouTube.
        """
        
        if not exists(self.FILES_PATH):
            mkdir(self.FILES_PATH)
        try:
            stream: Stream = self._init_youtube_streams()
            stream.download(
                output_path=self.FILES_PATH,
                filename=self.filename
            )
        except Exception as error:
            self.remove_current_file()
            raise DownloadError(error=error)
        
        downloading_completed(
            filename=self.filename
        )
        return None


    def remove_current_file(self) -> None:
        """Remove downloaded file.
        """
        remove(f"{self.FILES_PATH}{self.filename}")


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
        
        ## Video information.
        youtube_streams: StreamQuery = self._youtube_video.streams
        
        if self._is_mp3:
            return youtube_streams.get_audio_only()
        else:
            return youtube_streams.get_lowest_resolution()