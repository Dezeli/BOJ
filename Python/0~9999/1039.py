# 교환
import sys
import copy

N, K = sys.stdin.readline().split()
N_list = [i for i in N]
num_list = []
change_idx = []
for i in range(len(N)):
    for j in range(len(N)):
        if i != j:
            if i < j:
                change_idx.append([i, j])

same_list = []


def change_num(N_list: list[str], K: int):
    if K == 0:
        num = ""
        for i in N_list:
            num += i
        num_list.append(int(num))
        return
    for i, j in change_idx:
        new_N_list = copy.deepcopy(N_list)
        new_K = copy.deepcopy(K) - 1
        new_N_list[i], new_N_list[j] = new_N_list[j], new_N_list[i]
        if new_N_list[0] == "0":
            continue
        if (new_N_list, new_K) not in same_list:
            same_list.append((new_N_list, new_K))
            change_num(new_N_list, new_K)


change_num(N_list, int(K))

if num_list:
    print(max(num_list))
else:
    print(-1)
