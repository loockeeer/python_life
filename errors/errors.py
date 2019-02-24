class Error(Exception):pass

class CookTimeError(Error):
    """Raise when cook time is upper than 999999999 seconds"""

class NoNameGiven(Error):
    """Raise when no was given for a person"""
