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

        # click - pause and manual add
        # o - unpause
        # 1 - speed speed
        # 2 - low speed
        # s - clear screen
        # d - fill with random rectangles

        if event.type == pygame.MOUSEBUTTONDOWN:
            array_logic.manual_add(cells,win,BLACK,size,edge)
            #x, y = pygame.mouse.get_pos()
            #x = (x // 10)
            #y = (y // 10)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                cells = array_logic.create_array(size)
            if event.key == pygame.K_d:
                array_logic.fill_random_cells(cells, size)
            if event.key == pygame.K_1:
                speed = 0
            if event.key == pygame.K_2:
                speed = 1
        # end of experimental features


    array_logic.pygame_draw_lines(win,BLACK,edge)
    array_logic.pygame_draw_rect(win, BLACK, cells, size)
    array_logic.array_update(cells, size)
    pygame.display.update()
    if speed == 1: time.sleep(0.2)
