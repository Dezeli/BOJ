# Gnome Sequencing

N = int(input())
print("Gnomes:")
for _ in range(N):
    line = list(map(int, input().split()))

    if line==sorted(line) or line[::-1]==sorted(line):
        print("Ordered")
    else:
        print("Unordered")