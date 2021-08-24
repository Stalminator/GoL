import pygame, sys, array_logic, time

pygame.init()

size = 80
edge = size*10
win = pygame.display.set_mode((edge, edge))
speed = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

cells = array_logic.create_array(size)
array_logic.fill_random_cells(cells, size)

while True:
    win.fill(WHITE)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #experimental features
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = (x // 10)# * 10
            y = (y // 10)# * 10
            cells[x][y] = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                cells = array_logic.create_array(size)
            if event.key == pygame.K_d:
                array_logic.fill_random_cells(cells, size)
            if event.key == pygame.K_1:
                speed = 0
            if event.key == pygame.K_2:
                speed = 1
        #'''
    for i in range(0, edge, 10):
        pygame.draw.line(win, BLACK, (0, i), (edge, i), 2)
        pygame.draw.line(win, BLACK, (i, 0), (i, edge), 2)

    for i in range(size):
        for j in range(size):
            if cells[i][j] == 1:
                pygame.draw.rect(win, BLACK, (i * 10 + 2, j * 10 + 2, 8, 8))

    array_logic.array_update(cells, size)
    pygame.display.update()
    if speed == 1: time.sleep(0.2)
