# J박스

T = int(input())

for i in range(T):
    n = int(input())

    if n!=1:
        print('#'*n)
        for __ in range(n-2):
            print('#'+'J'*(n-2)+'#')
        print('#'*n)
    else:
        print('#')

    if i != T-1:
        print()
