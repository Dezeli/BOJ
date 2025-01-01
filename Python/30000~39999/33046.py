# Alea Iacta Est

A, B = map(int, input().split())
C, D = map(int, input().split())

jin = (A+B+C+D)%4-1
if jin<=0:
    jin += 4
print(jin)