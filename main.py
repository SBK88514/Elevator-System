import pygame
import Manager
from settings import SCREEN

manager = Manager.Manager()

running = True

# Main loop - responsible for the main execution of the application
while running:
    # Launch the initial screen or main interface
    manager.launch_screen()
    # Get and process user events
    events = pygame.event.get()
    for event in events:
        # Check if the user closed the window
        if event.type == pygame.QUIT:
            running = False
        # Check if the user clicked with the mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Handle building click events
            manager.check_click_building(mouse_pos)
    # Clear the screen with a black background
    SCREEN.fill((0, 0, 0))
    # Update the state and display changes
    manager.update()
    pygame.display.flip()
# Quit pygame when the loop ends
pygame.quit()
