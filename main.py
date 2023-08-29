import pygame
from pygame import mixer

from constant import *
from key import PianoKey


def calcPositions():
    """
    This function will calculate every black key and white key's x position.
    :return: black and white keys' positions.
    """

    whiteKeysPositions = []
    blackKeysPositions = []

    for i in range(WHITE_KEY_NUM):
        whiteKeysPositions.append(i * WHITE_KEY_WIDTH)

    blackKeyIndex = 0
    for i in range(WHITE_KEY_NUM):
        res = i % 7
        if res != 0 and res != 3:
            blackKeysPositions.append(i * WHITE_KEY_WIDTH - BLACK_KEY_WIDTH / 2)
            blackKeyIndex += 1

    return whiteKeysPositions, blackKeysPositions


if __name__ == '__main__':
    # init here.
    pygame.init()
    font = pygame.font.Font(None, FONT_SIZE)
    mixer.init()
    mixer.set_num_channels(CHANNEL_NUMS)

    window = pygame.display.set_mode(WINDOW_SIZE)

    whiteKeyPositions, blackKeyPositions = calcPositions()

    # build a map between the keyboard and the piano key.
    keysMapping = {
        pygame.K_1: PianoKey(True,  '1', 'C3 ', whiteKeyPositions[0],  'audio/C3.wav',  font),
        pygame.K_2: PianoKey(False, '2', 'Db3', blackKeyPositions[0],  'audio/Db3.wav', font),
        pygame.K_3: PianoKey(True,  '3', 'D3 ', whiteKeyPositions[1],  'audio/D3.wav',  font),
        pygame.K_4: PianoKey(False, '4', 'Eb3', blackKeyPositions[1],  'audio/Eb3.wav', font),
        pygame.K_5: PianoKey(True,  '5', 'E3 ', whiteKeyPositions[2],  'audio/E3.wav',  font),
        pygame.K_6: PianoKey(True,  '6', 'F3 ', whiteKeyPositions[3],  'audio/F3.wav',  font),
        pygame.K_7: PianoKey(False, '7', 'Gb3', blackKeyPositions[2],  'audio/Gb3.wav', font),
        pygame.K_8: PianoKey(True,  '8', 'G3 ', whiteKeyPositions[4],  'audio/G3.wav',  font),
        pygame.K_9: PianoKey(False, '9', 'Ab3', blackKeyPositions[3],  'audio/Ab3.wav', font),
        pygame.K_0: PianoKey(True,  '0', 'A3 ', whiteKeyPositions[5],  'audio/A3.wav',  font),
        pygame.K_q: PianoKey(False, 'Q', 'Bb3', blackKeyPositions[4],  'audio/Bb3.wav', font),
        pygame.K_w: PianoKey(True,  'W', 'B3 ', whiteKeyPositions[6],  'audio/B3.wav',  font),
        pygame.K_e: PianoKey(True,  'E', 'C4 ', whiteKeyPositions[7],  'audio/C4.wav',  font),
        pygame.K_r: PianoKey(False, 'R', 'Db4', blackKeyPositions[5],  'audio/Db4.wav', font),
        pygame.K_t: PianoKey(True,  'T', 'D4 ', whiteKeyPositions[8],  'audio/D4.wav',  font),
        pygame.K_y: PianoKey(False, 'Y', 'Eb4', blackKeyPositions[6],  'audio/Eb4.wav', font),
        pygame.K_u: PianoKey(True,  'U', 'E4 ', whiteKeyPositions[9],  'audio/E4.wav',  font),
        pygame.K_i: PianoKey(True,  'I', 'F4 ', whiteKeyPositions[10], 'audio/F4.wav',  font),
        pygame.K_o: PianoKey(False, 'O', 'Gb4', blackKeyPositions[7],  'audio/Gb4.wav', font),
        pygame.K_p: PianoKey(True,  'P', 'G4 ', whiteKeyPositions[11], 'audio/G4.wav',  font),
        pygame.K_a: PianoKey(False, 'A', 'Ab4', blackKeyPositions[8],  'audio/Ab4.wav', font),
        pygame.K_s: PianoKey(True,  'S', 'A4 ', whiteKeyPositions[12], 'audio/A4.wav',  font),
        pygame.K_d: PianoKey(False, 'D', 'Bb4', blackKeyPositions[9],  'audio/Bb4.wav', font),
        pygame.K_f: PianoKey(True,  'F', 'B4 ', whiteKeyPositions[13], 'audio/B4.wav',  font),
        pygame.K_g: PianoKey(True,  'G', 'C5 ', whiteKeyPositions[14], 'audio/C5.wav',  font),
        pygame.K_h: PianoKey(False, 'H', 'Db5', blackKeyPositions[10], 'audio/Db5.wav', font),
        pygame.K_j: PianoKey(True,  'J', 'D5 ', whiteKeyPositions[15], 'audio/D5.wav',  font),
        pygame.K_k: PianoKey(False, 'K', 'Eb5', blackKeyPositions[11], 'audio/Eb5.wav', font),
        pygame.K_l: PianoKey(True,  'L', 'E5 ', whiteKeyPositions[16], 'audio/E5.wav',  font),
        pygame.K_z: PianoKey(True,  'Z', 'F5 ', whiteKeyPositions[17], 'audio/F5.wav',  font),
        pygame.K_x: PianoKey(False, 'X', 'Gb5', blackKeyPositions[12], 'audio/Gb5.wav', font),
        pygame.K_c: PianoKey(True,  'C', 'G5 ', whiteKeyPositions[18], 'audio/G5.wav',  font),
        pygame.K_v: PianoKey(False, 'V', 'Ab5', blackKeyPositions[13], 'audio/Ab5.wav', font),
        pygame.K_b: PianoKey(True,  'B', 'A5 ', whiteKeyPositions[19], 'audio/A5.wav',  font),
        pygame.K_n: PianoKey(False, 'N', 'Bb5', blackKeyPositions[14], 'audio/Bb5.wav', font),
        pygame.K_m: PianoKey(True,  'M', 'B5 ', whiteKeyPositions[20], 'audio/B5.wav',  font),
    }

    # to speed up rendering, I use these 2 list to split the white keys and black keys.
    whitePianoKeys = []
    blackPianoKeys = []

    for pianoKey in keysMapping.values():
        if pianoKey.isWhiteKey():
            whitePianoKeys.append(pianoKey)
        else:
            blackPianoKeys.append(pianoKey)

    """
    event loop.
    When a key is pressed, if it is in our keysMapping, change the corresponding piano key's color,
    play the sound, and reset its color when the key is released. This is used to simulate the feedback
    effect of piano pressing in reality.
    """
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                pianoKey = keysMapping.get(event.key)

                if pianoKey is not None:
                    pianoKey.setColor(COLOR_MIKU)
                    pianoKey.playedOn(pygame.mixer.Channel(event.key % CHANNEL_NUMS))
            elif event.type == pygame.KEYUP:
                pianoKey = keysMapping.get(event.key)

                if pianoKey is not None:
                    pianoKey.resetColor()

        # render
        for key in whitePianoKeys:
            key.drawOn(window)

        for key in blackPianoKeys:
            key.drawOn(window)

        pygame.display.flip()

    pygame.quit()
