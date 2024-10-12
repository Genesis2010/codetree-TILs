from collections import deque

MAX_ATTACK = 5000
MAP = [[]]
ATTACK_TIME = [[]]
visited = [[]]
dx_dy = [[]]
MIN_ATTACK_TOWER = (0,0,0)
MAX_ATTACK_TOWER = (0,0,0)
N, M, K = 0, 0, 0
K_count = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def max_col_towers(max_tower):
    max_col_tower = 0
    temp = []

    for i in range(len(max_tower)):
        r, c = max_tower[i]
        if max_col_tower < c:
            max_col_tower = c
            temp = (r, c)

    return temp
def max_row_col_tower(lastest_towers):
    max_tower = 0
    temp = []

    for i in range(len(lastest_towers)):
        r, c = lastest_towers[i]

        if max_tower < r + c:
            max_tower = r + c
            temp = [(r, c)]
        elif max_tower == r + c:
            temp.append((r, c))

    return temp
def latest_attack_tower(min_towers):
    latest_attack = 0
    temp = []

    for i in range(len(min_towers)):
        r, c = min_towers[i]
        if latest_attack < ATTACK_TIME[r][c]:
            latest_attack = ATTACK_TIME[r][c]
            temp = [(r, c)]
        elif latest_attack == ATTACK_TIME[r][c]:
            temp.append((r, c))

    return temp
def min_attack_tower():
    global MIN_ATTACK_TOWER
    temp_attack = MAX_ATTACK
    temp = []

    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if temp_attack > MAP[i][j] and MAP[i][j] > 0:
                temp = []
                temp_attack = MAP[i][j]
                temp.append((i, j))
            elif temp_attack == MAP[i][j]:
                temp.append((i, j))

    return temp
def selectAttackTower():
    global MIN_ATTACK_TOWER

    # 공격력이 가장 낮은 포탑
    min_towers = min_attack_tower()

    if len(min_towers) == 1:
        i, j = min_towers[0]
        MIN_ATTACK_TOWER = (i, j, MAP[i][j] + N + M)

    # 공격력이 낮은 포탑이 2개 이상일 때, 가장 최근에 공격한 포탑
    elif len(min_towers) >= 2:
        lastest_towers = latest_attack_tower(min_towers)

        if len(lastest_towers) == 1:
            i, j = lastest_towers[0]
            MIN_ATTACK_TOWER = (i, j, MAP[i][j] + N + M)

        # 가장 최근에 공격한 포탑이 2개 이상일 때 행, 열의 합이 가장 큰 포탑
        else:
            max_tower = max_row_col_tower(lastest_towers)

            if len(max_tower) == 1:
                i, j = max_tower[0]
                MIN_ATTACK_TOWER = (i, j, MAP[i][j] + N + M)

            else:
                max_col_tower = max_col_towers(max_tower)
                i, j = max_tower[0]
                MIN_ATTACK_TOWER = (i, j, MAP[i][j] + N + M)

    i, j, k = MIN_ATTACK_TOWER
    MAP[i][j] = k

def min_col_towers(min_tower):
    min_col_tower = 0
    temp = []

    for i in range(len(min_tower)):
        r, c = min_tower[i]
        if min_col_tower < c:
            min_col_tower = c
            temp = (r, c)

    return temp
def min_row_col_tower(last_towers):
    min_tower = 0
    temp = []

    for i in range(len(last_towers)):
        r, c = last_towers[i]

        if min_tower > r + c:
            min_tower = r + c
            temp = [(r, c)]
        elif min_tower == r + c:
            temp.append((r, c))

    return temp
def late_attack_tower(max_towers):
    late_attack = 1000
    temp = []

    for i in range(len(max_towers)):
        r, c = max_towers[i]
        if late_attack > ATTACK_TIME[r][c]:
            latest_attack = ATTACK_TIME[r][c]
            temp = [(r, c)]
        elif late_attack == ATTACK_TIME[r][c]:
            temp.append((r, c))

    return temp
def max_attack_tower():
    temp_attack = 0
    temp = []

    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if temp_attack < MAP[i][j] and MAP[i][j] > 0:
               temp = []
               temp_attack = MAP[i][j]
               temp.append((i, j))
            elif temp_attack == MAP[i][j]:
                temp.append((i, j))

    return temp
def select_attacked_tower():
    global MAX_ATTACK_TOWER

    # 공격력이 가장 높은 포탑
    max_towers = max_attack_tower()

    if len(max_towers) == 1:
        i, j = max_towers[0]
        MAX_ATTACK_TOWER = (i, j, MAP[i][j] + N + M)

    # 공격력이 낮은 포탑이 2개 이상일 때, 가장 최근에 공격한 포탑
    elif len(max_towers) >= 2:
        last_towers = late_attack_tower(max_towers)

        if len(last_towers) == 1:
            i, j = last_towers[0]
            MAX_ATTACK_TOWER = (i, j, MAP[i][j] + N + M)

        # 가장 최근에 공격한 포탑이 2개 이상일 때 행, 열의 합이 가장 큰 포탑
        else:
            min_tower = min_row_col_tower(last_towers)

            if len(min_tower) == 1:
                i, j = min_tower[0]
                MAX_ATTACK_TOWER = (i, j, MAP[i][j] + N + M)

            else:
                max_col_tower = min_col_towers(min_tower)
                i, j = min_tower[0]
                MAX_ATTACK_TOWER = (i, j, MAP[i][j])

def clean_tower():
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] <= 0:
                MAP[i][j] == 0

def fix_tower():
    for i in range(len(ATTACK_TIME)):
        for j in range(len(ATTACK_TIME[i])):
            if ATTACK_TIME[i][j] < K_count and MAP[i][j] != 0:
                MAP[i][j] += 1

def first_attack():
    min_x, min_y, min_k = MIN_ATTACK_TOWER
    max_x, max_y, max_k = MAX_ATTACK_TOWER

    queue = deque()
    queue.append((min_x, min_y))
    visited[min_y][min_x] = True

    isSuccess = False

    while queue:
        y, x = queue.popleft()

        if y == max_x and x == max_y:
            isSuccess = True
            break

        for i in range(4):
            ny = (y + dy[i]) % N
            nx = (x + dx[i]) % M

            if 0 <= ny < N and 0 <= nx < M and MAP[ny][nx] != 0:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    dx_dy[ny][nx] = (dy[i], dx[i])
                    queue.append((ny, nx))

    if isSuccess == True:
        ATTACK_TIME[min_x][min_y] += K_count
        MAP[max_x][max_y] -= min_k
        ATTACK_TIME[max_x][max_y] += K_count
        temp_x, temp_y = max_x, max_y

        while not (temp_x == min_x and temp_y == min_y):
            y, x = dx_dy[temp_x][temp_y]

            temp_x, temp_y = temp_x - y, temp_y - x
            # MAP[temp_x][temp_y] -= min_k // 2
            # ATTACK_TIME[temp_x][temp_y] += K_count

            if not (temp_x == min_x and temp_y == min_y):
                MAP[temp_x][temp_y] -= min_k // 2
                ATTACK_TIME[temp_x][temp_y] += K_count

    clean_tower()

    return isSuccess

def second_attack():

    x, y, k = MAX_ATTACK_TOWER
    min_x, min_y, min_k = MIN_ATTACK_TOWER
    MAP[x][y] -= min_k
    ATTACK_TIME[x][y] += K_count

    for i in range(x-1, x+1):
        for j in range(y-1, y+1):
            ni, nj = i % 4, j % 4

            if 0 <= ni < N and 0 <= nj < M and MAP[ni][nj] != 0:
                if not (ni == min_x and nj == min_y):
                    MAP[ni][nj] -= min_k // 2
                    ATTACK_TIME[ni][nj] += K_count

    clean_tower()

def init():
    global visited, dx_dy, MIN_ATTACK_TOWER, MAX_ATTACK_TOWER

    dx_dy = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    MIN_ATTACK_TOWER = (0, 0, 0)
    MAX_ATTACK_TOWER = (0, 0, 0)

def solution():
    global MAP, ATTACK_TIME, N, M, K, visited, dx_dy, K_count
    N, M, K = map(int, input().split())
    K_count += 1
    MAP = [list(map(int, input().split())) for _ in range(N)]
    ATTACK_TIME = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx_dy = [[0] * M for _ in range(N)]
    max_tower = 0

    for _ in range(K):
        selectAttackTower()
        select_attacked_tower()

        result = first_attack()

        if not result:
            second_attack()

        fix_tower()

        K_count += 1
        init()

    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if MAP[i][j] > max_tower:
                max_tower = MAP[i][j]

    print(max_tower)

solution()