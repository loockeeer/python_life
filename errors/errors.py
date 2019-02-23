class Error(Exception):pass

class CookTimeError(Error):
    """Raise when cook time is upper than 999999999 seconds"""


