import pygame

print('Setup Start')
pygame.get_init()
window = pygame.display.set_mode(size=(600,480))
print('Setup Start')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit() #Close Window
            quit() #end pygame

