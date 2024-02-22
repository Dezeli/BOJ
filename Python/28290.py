# 안밖? 밖안? 계단? 역계단?

press = {"fdsajkl;":"in-out", "jkl;fdsa":"in-out", "asdf;lkj":"out-in",
         ";lkjasdf":"out-in", "asdfjkl;":"stairs", ";lkjfdsa":"reverse"}

s = input()
if s in press:
    print(press[s])
else:
    print("molu")