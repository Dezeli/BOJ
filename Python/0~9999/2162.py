# 선분 그룹
import sys

input = sys.stdin.readline

def isDivided(x1, y1, x2, y2, x3, y3, x4, y4):
    m1= (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)
    m2= (x2-x1)*(y4-y1) - (y2-y1)*(x4-x1)
    if m1 * m2 < 0:
        return True
    
    return False

def isCross(x1,y1, x2,y2, x3,y3, x4,y4):
    b1 = isDivided(x1, y1, x2, y2, x3, y3, x4, y4)
    b2 = isDivided(x3, y3, x4, y4, x1, y1, x2, y2)
    if b1 and b2:
        return True
    return False

