# 텀 프로젝트
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    team_check = [-1 for _ in range(n + 1)]
    team_check[0] = 0
    select = [0] + list(map(int, input().split()))

    for i in range(1, n + 1):
        if team_check[i] != -1:
            continue

        nums = [i]
        team_check[i] = -2

        while True:
            next = select[i]
            if team_check[next] == -2:
                while True:
                    r = nums.pop()
                    team_check[r] = 1
                    if r == next:
                        for j in nums:
                            team_check[j] = 0
                        break
                break
            elif team_check[next] != -1:
                for j in nums:
                    team_check[j] = 0
                break

            nums.append(next)
            team_check[next] = -2
            i = next
    print(n - sum(team_check))
