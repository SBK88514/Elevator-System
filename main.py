import pygame
import Manager

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
            manager.check_click()

    manager.update()
    pygame.display.flip()

pygame.quit()

