
class DownloadError(Exception):
    """Exception class for all the errors while downloading files.

    Args:
        Exception (class) 
    """
    def __init__(self, error: str) -> None:
        self.error: str
        super().__init__(error)