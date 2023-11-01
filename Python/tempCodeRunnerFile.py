# 대소문자 바꾸기

w = input()
for i in w:
    if i.isupper:
        print(i.lower, end = "")
    else:
        print(i.upper, end = "")