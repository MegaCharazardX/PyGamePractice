import pygame

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Hello")
clock = pygame.time.Clock()
running = True


PG = pygame

dt = 0
player_pos = PG.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in PG.event.get():
        if event.type == PG.QUIT:
            running = False
    screen.fill("WHITE")
    
    PG.draw.line(screen, "black", (0, 1), (1000,1), 30)
    
    PG.draw.circle(screen, "black", (player_pos), 5, 3)
    
    PG.draw.rect(screen, "red", (100, 400, 100, 100))
    
    PG.display.flip()
    dt = clock.tick(60)/1000
        
PG.quit()
