import random

def create_array(size):
    cells = []
    for i in range(size):
        tmp = []
        for j in range(size):
            tmp.append(0)
        cells.append(tmp)
    return cells

def fill_random_cells(cells, size):
    for i in range(size*10):
        cells[random.randint(0, size - 1)][random.randint(0, size - 1)] = 1

def check_single_cell(cells, x, y):
    try:
        if cells[x][y] == 1:
            return True
    except:
        return False

def check_neighborhood(cells, i, j):
    s = 0
    if check_single_cell(cells, i - 1, j - 1): s += 1
    if check_single_cell(cells, i - 1, j): s += 1
    if check_single_cell(cells, i - 1, j + 1): s += 1
    if check_single_cell(cells, i, j - 1): s += 1
    if check_single_cell(cells, i, j + 1): s += 1
    if check_single_cell(cells, i + 1, j - 1): s += 1
    if check_single_cell(cells, i + 1, j): s += 1
    if check_single_cell(cells, i + 1, j + 1): s += 1
    return s

def array_update(cells, size):
    tmp = []
    for i in range(size):
        for j in range(size):
            if cells[i][j] == 0 and check_neighborhood(cells, i, j) == 3:
                tmp.append([i, j, 1])
            elif cells[i][j] == 1 and check_neighborhood(cells, i, j) != 3 and check_neighborhood(cells, i, j) != 2:
                tmp.append([i, j, 0])
    for i in tmp:
        cells[i[0]][i[1]] = i[2]
