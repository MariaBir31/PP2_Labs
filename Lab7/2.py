import pygame
import datetime

pygame.init()

clock_face = pygame.image.load('Lab7/clock.png')
min_hand = pygame.image.load('Lab7/min_hand.png')
sec_hand = pygame.image.load('Lab7/sec_hand.png')

WIDTH, HEIGHT = clock_face.get_size()
CENTER = (WIDTH // 2, HEIGHT // 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

def blit_rotate_center(surf, image, angle, pos):
    rotated_image = pygame.transform.rotate(image, -angle)  
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(clock_face, (0, 0))  

    now = datetime.datetime.now()
    minute_angle = now.minute * 6  
    second_angle = now.second * 6  

    blit_rotate_center(screen, min_hand, minute_angle, CENTER)
    blit_rotate_center(screen, sec_hand, second_angle, CENTER)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100)  

pygame.quit()
