# 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int, sys.stdin.readline().split(" "))
Pokemons = {}
nums = [str(i) for i in range(1, 10)]

for i in range(1, N + 1):
    Pokemon = sys.stdin.readline().rstrip()
    Pokemons[str(i)] = Pokemon
    Pokemons[Pokemon] = i

for _ in range(M):
    Order = sys.stdin.readline().rstrip()
    print(Pokemons[Order])
