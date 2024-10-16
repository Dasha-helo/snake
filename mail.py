import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('^~^')
GreenYellow=(173,255,47)
red=(255,0,0)
LightCyan=(224,225,225)
Snake_x = 50

Snake_size = 30
Snake_speed_y = 0
gravity = 0.5
jump_height = -10
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        pygame.draw.rect(dis,GreenYellow,())
        dis.fill(LightCyan)
        pygame.display.update()
        print(event)
pygame.quit()
quit()