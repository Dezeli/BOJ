# 모범생 포닉스

N = int(input())

times = list(map(int, input().split()))

hours = sum(times)+(N-1)*8

print(*divmod(hours, 24))