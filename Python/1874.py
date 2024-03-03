# 스택 수열
import sys

n = int(sys.stdin.readline().rstrip())
nums = [i for i in range(n, 0, -1)]
orders = [0]
stack = [0]
for _ in range(n):
    sn = int(sys.stdin.readline().rstrip())
    while True:
        if orders[0] == "NO":
            break
        if sn == stack[-1]:
            stack.pop()
            orders.append("-")

            break
        else:
            if nums:
                stack.append(nums.pop())
                orders.append("+")
            else:
                orders[0] = "NO"
                break

if orders[0] == "NO":
    print("NO")
else:
    for order in orders[1:]:
        print(order)
