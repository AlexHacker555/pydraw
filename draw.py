import pygame

pygame.init()
screen = pygame.display.set_mode((900,900))
clock = pygame.time.Clock()
running = True
dt = 0
max_fps = 500
squares = []
color = [255, 255, 255]
font = pygame.font.Font(None, 36)
while running:
    screen.fill((0,0,0))
    fps = font.render(f"fps: {round(clock.get_fps())}", False, (255,255,255), (25,25,25))
    count = font.render(f"count: {len(squares)}", False, (255,255,255), (25,25,25))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    btn = pygame.mouse.get_pressed()
    if btn[0]:
        if not pygame.Rect((x, y, 20, 20)) in squares:
            squares.append(pygame.Rect(x + 5, y + 5, 20, 20))
    for i in squares:
        pygame.draw.rect(screen, tuple(color), i)
    key = pygame.key.get_pressed()
    pygame.mouse.set_visible(False)
    x, y = pygame.mouse.get_pos()
    if key[pygame.K_x]:
        squares.clear()
    elif key[pygame.K_q]:
        color = [255,0,0]
    elif key[pygame.K_w]:
        color = [0,255,0]
    elif key[pygame.K_e]:
        color = [0,127,255]
    elif key[pygame.K_r]:
        color = [255, 255, 255]
    elif key[pygame.K_t]:
        for i in range(x - 40, x + 40):
            for j in range(y - 40, y + 40):
                if pygame.Rect((i, j, 20, 20)) in squares:
                    squares.pop(squares.index(pygame.Rect(i,j,20,20)))
    screen.blit(fps, fps.get_rect(topleft=(10, 10)))
    screen.blit(count, count.get_rect(topleft=(10, 30)))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x, y, 30, 30))
    pygame.display.flip()
    dt = clock.tick(max_fps)