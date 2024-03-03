# 치킨댄스를 추는 곰곰이를 본 임스

N = int(input())
A, B = map(int, input().split())

print(min(N, A // 2 + B))
