import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('MyFirstGame')

start_game = True
while start_game:
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            start_game = False
            pygame.quit()