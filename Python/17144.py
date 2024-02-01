# 미세먼지 안녕!
import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

AC_room = []
AC_location = []
for i in range(R):
    line = list(map(int, input().split()))
    for j in range(C):
        if line[j]==-1:
            AC_location.append(i)
    AC_room.append(line)

def spread():
    Spread_room = [[0 for _ in range(C)] for __ in range(R)]
    for i in range(R):
        for j in range(C):
            val = AC_room[i][j]
            if val == -1:
                Spread_room[i][j] = -1
                continue
            elif val == 0:
                continue
            
            able = {"Up":True, "Down":True, "Left":True, "Right":True}
            if i==0:
                able["Up"] = False
            if i==R-1:
                able["Down"] = False
            if j==0:
                able["Left"] = False
            if j==C-1:
                able["Right"] = False
            if j==0 and i+1 in AC_location:
                able["Down"] = False
            if j==0 and i-1 in AC_location:
                able["Up"] = False
            if j==1 and i in AC_location:
                able["Left"] = False

            spread_val = val//5
            if able["Up"]:
                Spread_room[i-1][j] += spread_val
                val -= spread_val
            if able["Down"]:
                Spread_room[i+1][j] += spread_val
                val -= spread_val
            if able["Left"]:
                Spread_room[i][j-1] += spread_val
                val -= spread_val
            if able["Right"]:
                Spread_room[i][j+1] += spread_val
                val -= spread_val
            Spread_room[i][j] += val
    return Spread_room

def ac():
    AC_room = [[0 for _ in range(C)] for __ in range(R)]
    ACu = AC_location[0]
    ACd = AC_location[1]
    for i in range(R):
        for j in range(C):
            val = Spread_room[i][j]
            if j==0:
                if i < ACu:
                    AC_room[i+1][j] = val
                if i > ACd:
                    AC_room[i-1][j] = val
                continue
            if i==0 or i==R-1:
                if j!= 0:
                    AC_room[i][j-1] = val
                continue
            if j==C-1:
                if 0 < i <= AC_location[0]:
                    AC_room[i-1][j] = val
                if R-1 > i >= AC_location[1]:
                    AC_room[i+1][j] = val
                continue
            if i==ACu or i==ACd:
                if 0 < j < C-1:
                    AC_room[i][j+1] = val
                continue
            AC_room[i][j] = val
    AC_room[ACu][0], AC_room[ACd][0] = -1, -1
    return AC_room


for _ in range(T):
    Spread_room = spread()
    AC_room = ac()

dust = sum([sum(line) for line in AC_room]) + 2
print(dust)