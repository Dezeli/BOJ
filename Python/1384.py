# Messages
import sys

group_num = 0
n = int(sys.stdin.readline().rstrip())
while n != 0:
    group_num += 1
    cnt = 0
    print(f"Group {group_num}")

    papers = []
    for i in range(n):
        paper = list(sys.stdin.readline().split())
        papers.append(paper)
    for i in range(n):
        for j in range(1, n):
            if papers[i][j] == "N":
                disliker = papers[(n + i - j) % n][0]
                disliked = papers[i][0]
                print(f"{disliker} was nasty about {disliked}")
                cnt += 1
    if cnt == 0:
        print("Nobody was nasty")
    print()
    n = int(sys.stdin.readline().rstrip())
