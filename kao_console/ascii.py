ESCAPE = 27
ARROW_ESCAPE = 91
LINUX_HOME_END_ESCAPE = 79
ENDL = 13
TAB = 9

BACKSPACE = 127
DELETE = 51

HOME = 72
END = 70

CTRL_S = 19
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

KAO_UP = 260
KAO_DOWN = 261
KAO_LEFT = 262
KAO_RIGHT = 263
KAO_DELETE = 264
KAO_HOME = 265
KAO_END = 266
KAO_PAGE_UP = 267
KAO_PAGE_DOWN = 268
KAO_CTRL_UP = 269
KAO_CTRL_DOWN = 270
KAO_CTRL_LEFT = 271
KAO_CTRL_RIGHT = 272

CtrlEscapeToKAO = {UP_ARROW:KAO_CTRL_UP,
                   DOWN_ARROW:KAO_CTRL_DOWN,
                   LEFT_ARROW:KAO_CTRL_LEFT,
                   RIGHT_ARROW:KAO_CTRL_RIGHT,}


PageUpEscapeToKAO = {PAGE_KEY_FINAL:KAO_PAGE_UP}
PageDownEscapeToKAO = {PAGE_KEY_FINAL:KAO_PAGE_DOWN}

Sequence2EscapeToKAO = {CTRL_ESCAPE:CtrlEscapeToKAO}
Sequence1EscapeToKAO = {SEQUENCE_ESCAPE_2:Sequence2EscapeToKAO}

ArrowEscapeToKAO = {UP_ARROW:KAO_UP,
                    DOWN_ARROW:KAO_DOWN,
                    LEFT_ARROW:KAO_LEFT,
                    RIGHT_ARROW:KAO_RIGHT,
                    DELETE:KAO_DELETE,
                    HOME:KAO_HOME,
                    END:KAO_END,
                    PAGE_UP:PageUpEscapeToKAO,
                    PAGE_DOWN:PageDownEscapeToKAO,
                    SEQUENCE_ESCAPE_1:Sequence1EscapeToKAO
                    }

LinuxEscapeToKAO = {HOME:KAO_HOME,
                    END:KAO_END,
                    }

MetaCharToKAO = {ARROW_ESCAPE:ArrowEscapeToKAO,
                 LINUX_HOME_END_ESCAPE:LinuxEscapeToKAO
                }