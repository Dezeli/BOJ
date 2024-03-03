# Jo’s Pet
import sys


def scenario():
    o, w = map(int, sys.stdin.readline().split())
    scenarioNum = 1
    while True:
        work, amount = sys.stdin.readline().split()
        if work == "#":
            if o * 0.5 < w < o * 2:
                print(f"{scenarioNum} :-)")
            else:
                print(f"{scenarioNum} :-(")
            scenarioNum += 1
            o, w = map(int, sys.stdin.readline().split())
            if o == 0:
                break
        elif work == "F":
            w += int(amount)
        elif work == "E":
            w -= int(amount)
            if w <= 0:
                print(f"{scenarioNum} RIP")
                scenarioNum += 1
                while work == "F" or work == "E":
                    work, amount = sys.stdin.readline().split()
                o, w = map(int, sys.stdin.readline().split())
                if o == 0:
                    break


scenario()
