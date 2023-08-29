# we only use C3 - B5 tones, 15 black and 21 white keys.
BLACK_KEY_NUM = 15
WHITE_KEY_NUM = 21

# piano keys are just rectangles, here are their info.
WHITE_KEY_WIDTH = 46
WHITE_KEY_HEIGHT = 390
BLACK_KEY_WIDTH = 30
BLACK_KEY_HEIGHT = 254

WINDOW_SIZE = (WHITE_KEY_WIDTH * WHITE_KEY_NUM, WHITE_KEY_HEIGHT)

# pygame could set the number of channels, which is very helpful when playing multiple sound at the same time.
CHANNEL_NUMS = 8

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_MIKU = (57, 197, 187)   # Hatsune Miku color, #39C5BB

# some info about the text.
BORDER_SIZE = 1
FONT_SIZE = 20
KEY_NAME_DISTANCE = 20
TONE_NAME_DISTANCE = 40
