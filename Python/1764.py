# 듣보잡
import sys
import collections

N, M = map(int, sys.stdin.readline().split())
people = collections.defaultdict(int)

for _ in range(N+M):
    person = sys.stdin.readline().rstrip()
    people[person] += 1


same_list = []
for key, val in people.items():
    if val==2:
        same_list.append(key)
same_list.sort()
print(len(same_list))
for person in same_list:
    print(person)