import random
from copy import deepcopy
import time, os

cells = []

size = 100
for i in range(size):
    tmp = []
    for j in range(size):
        tmp.append(0)
    cells.append(tmp)

'''
cells[4][4] = 1
cells[4][5] = 1
cells[5][4] = 1
cells[5][6] = 1
cells[6][5] = 1
'''

# '''
for i in range(1000):
    cells[random.randint(0, size - 1)][random.randint(0, size - 1)] = 1
'''
for i in cells:
    for j in i:
        print(j,end='')
    print()

print()
'''


def check_single_cell(x, y):
    try:
        if cells[x][y] == 1:
            return True
    except:
        return False


def check_neighborhood(i, j):
    s = 0
    if check_single_cell(i - 1, j - 1):
        s += 1
        # print('ul')
    if check_single_cell(i - 1, j): s += 1
    if check_single_cell(i - 1, j + 1): s += 1
    if check_single_cell(i, j - 1): s += 1
    if check_single_cell(i, j + 1): s += 1
    if check_single_cell(i + 1, j - 1): s += 1
    if check_single_cell(i + 1, j): s += 1
    if check_single_cell(i + 1, j + 1): s += 1
    # if s!=0: print(i,j,s)
    return s


def draw():
    tmp = []
    for i in range(size):
        for j in range(size):
            if cells[i][j] == 0 and check_neighborhood(i, j) == 3:
                tmp.append([i, j, 1])
                # c_tmp[i][j] = 1
                # print('www')
            elif cells[i][j] == 1 and check_neighborhood(i, j) != 3 and check_neighborhood(i, j) != 2:
                # print('totu')
                # c_tmp[i][j] = 0
                tmp.append([i, j, 0])
    for i in tmp:
        cells[i[0]][i[1]] = i[2]
    # print(tmp)


'''
while True:
    os.system('cls')
    for i in range(size):
        for j in range(size):
            if check_neighborhood(cells,i,j) == 3:
                cells[i][j] = 1
            elif cells[i][j] == 1 and (check_neighborhood(cells,i,j) != 3 or check_neighborhood(cells,i,j) != 2):
                cells[i][j] = 0



    for i in c_tmp:
        for j in i:
            print(j,end='')
        print()

    #cells = deepcopy(c_tmp)

    for i in cells:
        for j in i:
            print(j, end='')
        print()

    draw()

    time.sleep(1)

'''