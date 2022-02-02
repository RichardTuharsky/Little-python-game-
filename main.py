import pygame
import sys

if __name__ == "__main__":
    bg = pygame.image.load("assets/background.jpg")
    window = pygame.display.set_mode((500, 800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.blit(bg, )
        pygame.display.update()
