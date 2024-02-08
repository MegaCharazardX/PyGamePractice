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
    screen.fill("#000000")

    PG.draw.circle(screen, "#ffffff", player_pos, 40)
    
    keys = PG.key.get_pressed()
    if keys[PG.K_UP] or keys[PG.K_w] :
        player_pos.y -= 300*dt
        
    if keys[PG.K_DOWN] or keys[PG.K_s] :
        player_pos.y += 300*dt
        
    if keys[PG.K_LEFT] or keys[PG.K_a] :
        player_pos.x -= 300*dt
        
    if keys[PG.K_RIGHT] or keys[PG.K_d] :
        player_pos.x += 300*dt
    
    if event.type == PG.MOUSEWHEEL:
        # pos = PG.mouse.get_pos()
        # print(pos)1
        # player_pos.x = pos[0]
        # player_pos.y = pos[1]
        PG.draw.circle(screen, "red", player_pos, 40)
        
    
    # if event.type == PG.MOUSEBUTTONDOWN:
    #     pos = PG.mouse.get_pos()
    #     player_pos.x += pos[0]
    #     player_pos.y += pos[1]
    
    PG.display.flip()
    
    dt = clock.tick(60)/1000
        

PG.quit()
