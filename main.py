import time

import pygame, sys, random, tmp

pygame.init()

win = pygame.display.set_mode((800, 800))
WHITE =(255, 255, 255)
squares =[]

clock=pygame.time.Clock()

while True:
    win.fill((0, 0, 0))
    clock.tick(60)
    c1 = random.randint(0,255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            squares.clear()
            x,y = pygame.mouse.get_pos()
            x =(x//10)*10
            y =(y//10)*10
            #squares.append([win,WHITE,(x,y,20,20)])

    for i in range(10, 800, 10):
        pygame.draw.line(win, WHITE,(0, i),(800, i), 2)
        pygame.draw.line(win, WHITE,(i, 0),(i, 800), 2)
        #squares.append([win,(c1,c2,c3),(random.randrange(22,780,20),random.randrange(22,780,20),18,18)])

#pygame.draw.rect(win,WHITE,(random.randrange(20,480,20),random.randrange(20,480,20),20,20))
    #for i in squares:
        #pygame.draw.rect(*i)
    for i in range(tmp.size):
        for j in range(tmp.size):
            if tmp.cells[i][j] == 1:
                pygame.draw.rect(win,WHITE,(i*10+2,j*10+2,8,8))
            #else:
                #print(pygame.draw.rect(win, (120,0,0), (i * 20, j * 20, 18, 18)))

    tmp.draw()

#time.sleep(1)
    pygame.display.update()
    #time.sleep(0.2)
    #print(tmp.cells)
