import os

readme = open(f"./README.md", "w", encoding="UTF-8")
readme.write(
    "## BaekJoon Online Judge Solutions   \nhttps://www.acmicpc.net/user/dezeli   \n"
)

Python = [
    "Python/0~9999",
    "Python/10000~19999",
    "Python/20000~29999",
    "Python/30000~39999",
]
readme.write(f"\n#### Python\n")
for s in Python:
    files = os.listdir(f"./{s}")
    data_list = []

    for filename in files:
        file = open(f"./{s}/{filename}", "r", encoding="UTF-8")
        title = file.readline()[2:-1]
        filenum = filename.split(".")[0]
        data_list.append([int(filenum), title, filename])

    data_list.sort()

    for filenum, title, filename in data_list:
        readme.write(f"- [{filenum} : {title}](./{s}/{filename})    \n")

Programing_Languages = [
    "아희",
    "Ada",
    "FreeBasic",
    "GolfScript",
    "Algol68",
    "Fortran",
    "C++17",
]

for language in Programing_Languages:
    readme.write(f"\n#### {language}\n")
    files = os.listdir(f"./{language}")
    data_list = []

    for filename in files:
        file = open(f"./{language}/{filename}", "r", encoding="UTF-8")
        title = file.readline()[2:-1]
        filenum = filename.split(".")[0]
        data_list.append([int(filenum), title, filename])

    data_list.sort()

    for filenum, title, filename in data_list:
        readme.write(f"- [{filenum} : {title}](./{language}/{filename})    \n")
readme.close()
