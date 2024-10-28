# 과목선택
import sys

subjectList1 = []
subjectList2 = []
for i in range(4):
    subjectList1.append(int(sys.stdin.readline().rstrip()))
for i in range(2):
    subjectList2.append(int(sys.stdin.readline().rstrip()))
subjectList1.remove(min(subjectList1))
subjectList2.remove(min(subjectList2))
print(sum(subjectList1) + sum(subjectList2))
