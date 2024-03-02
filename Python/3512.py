# Flat 

n, c = map(int, input().split())

bed_area = 0
bal_area = 0
total_area = 0
for _ in range(n):
    a, s = input().split()
    a = int(a)
    if s=='bedroom':
        bed_area += a
    if s=='balcony':
        bal_area += a
    total_area += a

print(total_area)
print(bed_area)
print(total_area*c-bal_area*(c/2))
