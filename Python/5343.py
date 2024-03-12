# Parity Bit

N = int(input())

for _ in range(N):
    bit = input()
    cnt = 0
    for i in range(0, len(bit), 8):
          cntOnes = 0
          for j in range(7):
            if bit[i + j]=='1':
                cntOnes += 1
          if str(cntOnes%2)!=bit[i+7]:
            cnt += 1
    print(cnt)