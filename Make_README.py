import os

Programing_Languages = ["Python"]
readme = open(f"./README.md", "w", encoding="UTF-8")
readme.write(
    "## BaekJoon Online Judge Solutions   \nhttps://www.acmicpc.net/   \n"
)
for language in Programing_Languages:
    readme.write(f"\n#### {language}\n")
    files = os.listdir(f"./{language}")
    file_list = []

    for filename in files:
        file = open(f"./{language}/{filename}", "r", encoding="UTF-8")
        title = file.readline()[2:-1]
        filenum = filename.split(".")[0]
        file_list.append([int(filenum), title, file])
    file_list.sort()

    for filenum, title, file in file_list:
        readme.write(f"- [{filenum}번 : {title}](./{language}/{filename})    \n")
readme.close()