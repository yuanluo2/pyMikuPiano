import pygame
from pygame import mixer
from constant import *


class PianoKey:
    def __init__(self, isWhiteFlag, keyName, toneName, initX, soundFilePath, font):
        """
        :param isWhiteFlag: is this a white key or a black key?
        :param keyName: the name on the keyboard, like a, b ,3 ...
        :param toneName: the name of the tone, like C3, D4 ...
        :param initX: x position, this is used to determine piano key rectangle's position.
        :param soundFilePath: the sound file's path.
        :param font: used to render text.
        """
        self.isWhiteFlag = isWhiteFlag
        self.initX = initX
        self.color = COLOR_WHITE if isWhiteFlag else COLOR_BLACK
        self.sound = mixer.Sound(soundFilePath)

        if isWhiteFlag:
            self.keyName = font.render(keyName, True, COLOR_BLACK)
            self.toneName = font.render(toneName, True, COLOR_BLACK)
        else:
            self.keyName = font.render(keyName, True, COLOR_WHITE)
            self.toneName = font.render(toneName, True, COLOR_WHITE)

    def isWhiteKey(self):
        return self.isWhiteFlag

    def setColor(self, color):
        self.color = color

    def resetColor(self):
        self.color = COLOR_WHITE if self.isWhiteFlag else COLOR_BLACK

    def drawOn(self, window):
        if self.isWhiteFlag:
            pygame.draw.rect(window, self.color, (self.initX, 0, WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT))
            pygame.draw.rect(window, COLOR_BLACK, (self.initX, 0, WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT), BORDER_SIZE)

            keyNameRect = self.keyName.get_rect(center=(self.initX + WHITE_KEY_WIDTH/2, WHITE_KEY_HEIGHT - KEY_NAME_DISTANCE))
            toneNameRect = self.toneName.get_rect(center=(self.initX + WHITE_KEY_WIDTH/2, WHITE_KEY_HEIGHT - TONE_NAME_DISTANCE))
        else:
            pygame.draw.rect(window, self.color, (self.initX, 0, BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT))

            keyNameRect = self.keyName.get_rect(center=(self.initX + BLACK_KEY_WIDTH / 2, BLACK_KEY_HEIGHT - KEY_NAME_DISTANCE))
            toneNameRect = self.toneName.get_rect(center=(self.initX + BLACK_KEY_WIDTH / 2, BLACK_KEY_HEIGHT - TONE_NAME_DISTANCE))

        window.blit(self.keyName, keyNameRect)
        window.blit(self.toneName, toneNameRect)

    def playedOn(self, channel):
        channel.play(self.sound)
