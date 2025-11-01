# 큐빙
import sys

input = sys.stdin.readline

def rotate_face(face, clock=True):
    if clock:
        return [face[6], face[3], face[0],
                face[7], face[4], face[1],
                face[8], face[5], face[2]]
    else:
        return [face[2], face[5], face[8],
                face[1], face[4], face[7],
                face[0], face[3], face[6]]


TC = int(input())

for _ in range(TC):
    # | U 위 | D 민 | F 앞 | B 뒤 | L 왼 | R 오 |
    # | w 흰 | y 노 | r 빨 | o 주 | g 초 | b 파 |
    cube = [['w']*9, ['y']*9, ['r']*9, ['o']*9, ['g']*9, ['b']*9]

    n = int(input())
    actions = list(input().rstrip().split())
    
    
    for act in actions:
        face, dir = act[0], act[1]
        clock = (dir == '+')

        if face == 'U':
            cube[0] = rotate_face(cube[0], clock)
            if clock:
                tmp = cube[2][0:3]
                cube[2][0:3] = cube[5][0:3]
                cube[5][0:3] = cube[3][0:3]
                cube[3][0:3] = cube[4][0:3]
                cube[4][0:3] = tmp
            else:
                tmp = cube[2][0:3]
                cube[2][0:3] = cube[4][0:3]
                cube[4][0:3] = cube[3][0:3]
                cube[3][0:3] = cube[5][0:3]
                cube[5][0:3] = tmp

        elif face == 'D':
            cube[1] = rotate_face(cube[1], clock)
            if clock:
                tmp = cube[2][6:9]
                cube[2][6:9] = cube[4][6:9]
                cube[4][6:9] = cube[3][6:9]
                cube[3][6:9] = cube[5][6:9]
                cube[5][6:9] = tmp
            else:
                tmp = cube[2][6:9]
                cube[2][6:9] = cube[5][6:9]
                cube[5][6:9] = cube[3][6:9]
                cube[3][6:9] = cube[4][6:9]
                cube[4][6:9] = tmp

        elif face == 'F':
            cube[2] = rotate_face(cube[2], clock)
            if clock:
                tmp = [cube[0][6], cube[0][7], cube[0][8]]
                cube[0][6], cube[0][7], cube[0][8] = cube[4][8], cube[4][5], cube[4][2]
                cube[4][8], cube[4][5], cube[4][2] = cube[1][2], cube[1][1], cube[1][0]
                cube[1][2], cube[1][1], cube[1][0] = cube[5][0], cube[5][3], cube[5][6]
                cube[5][0], cube[5][3], cube[5][6] = tmp
            else:
                tmp = [cube[0][6], cube[0][7], cube[0][8]]
                cube[0][6], cube[0][7], cube[0][8] = cube[5][0], cube[5][3], cube[5][6]
                cube[5][0], cube[5][3], cube[5][6] = cube[1][2], cube[1][1], cube[1][0]
                cube[1][2], cube[1][1], cube[1][0] = cube[4][8], cube[4][5], cube[4][2]
                cube[4][8], cube[4][5], cube[4][2] = tmp

        elif face == 'B':
            cube[3] = rotate_face(cube[3], clock)
            if clock:
                tmp = [cube[0][0], cube[0][1], cube[0][2]]
                cube[0][0], cube[0][1], cube[0][2] = cube[5][2], cube[5][5], cube[5][8]
                cube[5][2], cube[5][5], cube[5][8] = cube[1][8], cube[1][7], cube[1][6]
                cube[1][8], cube[1][7], cube[1][6] = cube[4][6], cube[4][3], cube[4][0]
                cube[4][6], cube[4][3], cube[4][0] = tmp
            else:
                tmp = [cube[0][0], cube[0][1], cube[0][2]]
                cube[0][0], cube[0][1], cube[0][2] = cube[4][6], cube[4][3], cube[4][0]
                cube[4][6], cube[4][3], cube[4][0] = cube[1][8], cube[1][7], cube[1][6]
                cube[1][8], cube[1][7], cube[1][6] = cube[5][2], cube[5][5], cube[5][8]
                cube[5][2], cube[5][5], cube[5][8] = tmp

        elif face == 'L':
            cube[4] = rotate_face(cube[4], clock)
            if clock:
                tmp = [cube[0][0], cube[0][3], cube[0][6]]
                cube[0][0], cube[0][3], cube[0][6] = cube[3][8], cube[3][5], cube[3][2]
                cube[3][8], cube[3][5], cube[3][2] = cube[1][0], cube[1][3], cube[1][6]
                cube[1][0], cube[1][3], cube[1][6] = cube[2][0], cube[2][3], cube[2][6]
                cube[2][0], cube[2][3], cube[2][6] = tmp
            else:
                tmp = [cube[0][0], cube[0][3], cube[0][6]]
                cube[0][0], cube[0][3], cube[0][6] = cube[2][0], cube[2][3], cube[2][6]
                cube[2][0], cube[2][3], cube[2][6] = cube[1][0], cube[1][3], cube[1][6]
                cube[1][0], cube[1][3], cube[1][6] = cube[3][8], cube[3][5], cube[3][2]
                cube[3][8], cube[3][5], cube[3][2] = tmp

        elif face == 'R':
            cube[5] = rotate_face(cube[5], clock)
            if clock:
                tmp = [cube[0][2], cube[0][5], cube[0][8]]
                cube[0][2], cube[0][5], cube[0][8] = cube[2][2], cube[2][5], cube[2][8]
                cube[2][2], cube[2][5], cube[2][8] = cube[1][2], cube[1][5], cube[1][8]
                cube[1][2], cube[1][5], cube[1][8] = cube[3][6], cube[3][3], cube[3][0]
                cube[3][6], cube[3][3], cube[3][0] = tmp
            else:
                tmp = [cube[0][2], cube[0][5], cube[0][8]]
                cube[0][2], cube[0][5], cube[0][8] = cube[3][6], cube[3][3], cube[3][0]
                cube[3][6], cube[3][3], cube[3][0] = cube[1][2], cube[1][5], cube[1][8]
                cube[1][2], cube[1][5], cube[1][8] = cube[2][2], cube[2][5], cube[2][8]
                cube[2][2], cube[2][5], cube[2][8] = tmp

    for i in range(0, 9, 3):
        print(''.join(cube[0][i:i+3]))