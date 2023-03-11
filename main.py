import random  # For generating random numbers
import sys  # We will use sys.exit to exit the program
import pygame
from pygame.locals import *  # Basic pygame imports

# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}

PLAYER = 'images/bird.png'
BACKGROUND = 'images/bg.jpg'
PIPE = 'images/pipe.png'
UPIPE = 'images/rotated_pipe.png'

def welcomeScreen


if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init()  # Initialize all pygame's modules
    FPSLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')

    GAME_SPRITES['numbers'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    )
    GAME_SPRITES['base'] = pygame.image.load('images/base.png').convert_alpha()

    GAME_SPRITES['pipe'] = (
        pygame.image.load(UPIPE).convert_alpha(),
        pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()

    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    # Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('sounds/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('sounds/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('sounds/point.wav')

while True:
    welcomeScreen() #Shows a welcome screen until the user starts the game
    mainGame()  #Main Game function
    exitGame()