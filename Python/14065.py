# Gorivo
# 보스니아어 문제
import sys

gfl = float(sys.stdin.readline().rstrip())
L = 3.785411784
KM = 1.609344
result = L / (gfl * KM) * 100
print(result)
