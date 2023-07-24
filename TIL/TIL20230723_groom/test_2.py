N, K = 4, 6
move = 'ULRDUU'
miro = []
for i in range(N):
    miro.append(list(map(int, input().split())))
r, c = 0, 0
for i in range(N):
    for j in range(N):
        if miro[i][j] == 1:            
            r = i
            c = j

real_move = 0
check = 0
for i in range(K):
    real_move += 1
    if move[i] == 'U':
        r -= 1
        if r < 0:
            r = 0
            real_move -= 1
    elif move[i] == 'L':
        c -= 1
        if c < 0:
            c = 0
            real_move -= 1
    elif move[i] == 'R':
        c += 1
        if c > N - 1:
            c = N - 1
            real_move -= 1
    else:
        r += 1
        if r > N - 1:
            r = N - 1
            real_move -= 1
    
    if miro[r][c] == 2:
        check = 1
        print(f'SUCCESS {real_move}')
        break
    elif miro[r][c] == 3:
        real_move -= 1
        if move[i] == 'U':
            r += 1
        elif move[i] == 'L':
            c += 1
        elif move[i] == 'R':
            c -= 1
        else:
            r -= 1

if check == 0:
    print('FAIL')