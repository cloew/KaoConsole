import sys
import select

__on_windows__ = False
try:
    import tty, termios
except ImportError:
    __on_windows__ = True
    import msvcrt    

from ascii import *

def getch(blocking=True):
    """ Retrieves a single character from the command line """
    if __on_windows__:
        return __getch_WINDOWS(blocking)
    else:
        return __getch_UNIX_CYGWIN(blocking)

def __getch_WINDOWS(blocking=True):
    """ Retrieves a single character from the command line for Windows """
    return msvcrt.getch()
    
def __getch_UNIX_CYGWIN(blocking=True):
    """ Retrieves a single character from the command line for UNIX or cygwin """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        if blocking:
            char = _getCharacterAndBlock()
        else:
            char = _getCharacterWithoutBlocking()
        metaChars = _getMetaCharacters()
        # print char, metaChars
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
    return _processMetaCharacter(char, metaChars)
    
def cls():
    """ Clears the console """
    sys.stdout.write("\033c")
    
def _getCharacterAndBlock():
    """ """
    return ord(sys.stdin.read(1))
    
def _getCharacterWithoutBlocking():
    """ """
    char = None
    i,o,e = select.select([sys.stdin],[],[],.0001)
    for s in i:
        if s == sys.stdin:
            char = _getCharacterAndBlock()
    return char
    
def _getMetaCharacters():    
        """ """
        metaBytes = []
        while True:
            metaByte = _getMetaCharacter()
            if metaByte is None:
                break
            else:
                metaBytes.append(metaByte)
        return metaBytes

def _getMetaCharacter():  
    """ Gets a Metadata Character """
    return _getCharacterWithoutBlocking()
    
def _processMetaCharacter(char, metaChars):
    """ Processes an escaped meta-data character """
    dict = MetaCharToKAO
    if char == ESCAPE and len(metaChars) > 0 and metaChars[0] in MetaCharToKAO:
        for metaChar in metaChars:
            if metaChar in dict:
                dict = dict[metaChar]
                if type(dict) is int:
                    return dict
            else:
                return ord(" ")
    return char