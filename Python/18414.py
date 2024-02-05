# X に最も近い値 (The Nearest Value) 

X, L, R = map(int, input().split())

near = L
for i in range(L, R+1):
    if abs(X-near)>abs(X-i):
        near = i

print(near)