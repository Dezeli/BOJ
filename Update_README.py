import os

Programing_Languages = [
    "Python",
    "아희",
    "Ada",
    "FreeBasic",
    "GolfScript",
    "Algol68",
    "Fortran",
]
readme = open(f"./README.md", "w", encoding="UTF-8")
readme.write(
    "## BaekJoon Online Judge Solutions   \nhttps://www.acmicpc.net/user/dezeli   \n"
)
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
