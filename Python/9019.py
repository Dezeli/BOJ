# DSLR
from sys import stdin
from collections import deque, defaultdict

T = int(stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, stdin.readline().split(" "))
    check = defaultdict(int)

    queue = deque()
    queue += [[A, ""]]
    check[A] = 1
    while queue:
        cur, ord = queue.popleft()
        if cur == B:
            print(ord)
            break
        check[cur] = 1
        D = cur * 2 % 10000
        if check[D] == 0:
            queue += [[D, ord + "D"]]
            check[D] = 1
        S = cur - 1
        if S == -1:
            S = 9999
        if check[S] == 0:
            queue += [[S, ord + "S"]]
            check[S] = 1
        L = (cur * 10 + cur // 1000) % 10000
        if check[L] == 0:
            queue += [[L, ord + "L"]]
            check[L] = 1
        R = cur % 10 * 1000 + cur // 10
        if check[R] == 0:
            queue += [[R, ord + "R"]]
            check[R] = 1
