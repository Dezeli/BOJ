# Poziome serca

heart =  [  " @@@   @@@ ", 
            "@   @ @   @", 
            "@    @    @",
            "@         @", 
            " @       @ ",
            "  @     @  ", 
            "   @   @   ", 
            "    @ @    ",
            "     @     "
            ]
n = int(input())

for line in heart:
    big_line = [line for _ in range(n)]
    print(" ".join(big_line))
