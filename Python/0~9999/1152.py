# 단어의 개수
import sys

sentence = sys.stdin.readline().strip()
if sentence != "":
    word_List = sentence.split(" ")
else:
    word_List = []

print(len(word_List))
