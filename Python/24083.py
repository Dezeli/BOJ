# 短針 (Hour Hand)


A = int(input())
B = int(input())
time = (A+B)%12
if time==0: time = 12
print(time)