import pygame
pygame.init()
screen = pygame.display.set_mode()

pygame.draw.circle(screen , "green", [100,500] , 20)
pygame.display.flip()
pygame.time.wait(3000)
pygame.draw.circle(screen, "red", [150,500], 40)
pygame.display.flip()
pygame.time.wait(3000)
pygame.draw.circle(screen, "orange", [200,500], 60)
pygame.display.flip()
pygame.time.wait(3000)
