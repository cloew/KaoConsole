import string
import sys

ESCAPE = 27
ARROW_ESCAPE = 91
LINUX_HOME_END_ESCAPE = 79
ENDL = 13
TAB = 9
TAB_FINAL = 90

BACKSPACE = 127
DELETE = 51

HOME = 72
END = 70

# Add CTRL Letters
asciiValue = 1
for letter in string.uppercase:
    name = "CTRL_{0}".format(letter) 
    setattr(sys.modules[__name__], name, asciiValue)
    asciiValue += 1

# Add meta characters
UP_ARROW = 65
DOWN_ARROW = 66
RIGHT_ARROW = 67
LEFT_ARROW = 68

SEQUENCE_ESCAPE_1 = 49
SEQUENCE_ESCAPE_2 = 59

CTRL_ESCAPE = 53

PAGE_UP = 53
PAGE_DOWN = 54

PAGE_KEY_FINAL = 126


ArrowEscapeToKAO = {}
CtrlEscapeToKAO = {}

escapeKeys = {"":ArrowEscapeToKAO,
              "CTRL":CtrlEscapeToKAO}

keys = {"UP":UP_ARROW,
        "DOWN":DOWN_ARROW,
        "LEFT":LEFT_ARROW,
        "RIGHT":RIGHT_ARROW,
        "DELETE":DELETE,
        "HOME":HOME,
        "END":END,
        "PAGE_UP":PAGE_UP,
        "PAGE_DOWN":PAGE_DOWN}

        
__kao_index = 260
for escapeKey in escapeKeys:
    for key in keys:
        prefix = "KAO"
        if not escapeKey == "":
            prefix += "_"
            prefix += escapeKey
        name = prefix + "_" + key
        setattr(sys.modules[__name__], name, __kao_index)
        escapeKeys[escapeKey][keys[key]] = __kao_index
        __kao_index += 1
        
KAO_SHIFT_TAB = __kao_index
__kao_index += 1
                   
PageUpEscapeToKAO = {PAGE_KEY_FINAL:KAO_PAGE_UP}
PageDownEscapeToKAO = {PAGE_KEY_FINAL:KAO_PAGE_DOWN}

Sequence2EscapeToKAO = {CTRL_ESCAPE:CtrlEscapeToKAO}
Sequence1EscapeToKAO = {SEQUENCE_ESCAPE_2:Sequence2EscapeToKAO}

ArrowEscapeToKAO[SEQUENCE_ESCAPE_1]  = Sequence1EscapeToKAO 
ArrowEscapeToKAO[PAGE_UP]  = PageUpEscapeToKAO 
ArrowEscapeToKAO[PAGE_DOWN]  = PageDownEscapeToKAO
ArrowEscapeToKAO[TAB_FINAL]  = KAO_SHIFT_TAB

LinuxEscapeToKAO = {HOME:KAO_HOME,
                    END:KAO_END,
                    }

MetaCharToKAO = {ARROW_ESCAPE:ArrowEscapeToKAO,
                 LINUX_HOME_END_ESCAPE:LinuxEscapeToKAO
                }