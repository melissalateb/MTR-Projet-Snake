import pygame
from controller import GameController

def main():
    pygame.init()
    controller = GameController()
    controller.run_game()

if __name__ == "__main__":
    main()
