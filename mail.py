
import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('^~^')
GreenYellow=(173,255,47)
red=(255,0,0)
LightCyan=(224,225,225)
Snake_x = 190
Snake_y=125

Snake_size = 20
Snake_speed_y = 0
gravity = 0.5
jump_height = -10
game_over = False

def draw_objects():
    dis.fill(LightCyan)
    pygame.draw.rect(dis, GreenYellow, (Snake_x,Snake_y, Snake_size, Snake_size))


clock = pygame.time.Clock()

while not game_over:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Snake_x -=10
            elif event.key == pygame.K_RIGHT:
                Snake_x += 10
            elif event.key == pygame.K_UP:
                Snake_y -=10
            elif event.key == pygame.K_DOWN:
                Snake_y +=10

                clock.tick(10)
        draw_objects()
        pygame.display.update()
        pygame.display.flip()
        print(event)
pygame.quit()
quit()
