# 내 학점을 구해줘

T = int(input())

for _ in range(T):
    c_sum = 0
    g_sum = 0
    N = int(input())
    for _ in range(N):
        C, G = map(float, input().split(" "))
        c_sum += C
        g_sum += C * G
    print(int(c_sum), round(g_sum / c_sum, 1))
