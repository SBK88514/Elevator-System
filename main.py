import pygame
import Manager
from settings import SCREEN

manager = Manager.Manager()


running = True

# Main loop
while running:
    manager.launch_screen()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            manager.check_click(mouse_pos)

    SCREEN.fill((0, 0, 0))

    manager.update()
    pygame.display.flip()

pygame.quit()

