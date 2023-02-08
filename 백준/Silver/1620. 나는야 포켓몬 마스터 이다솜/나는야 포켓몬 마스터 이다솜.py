import sys
input = sys.stdin.readline
N, M = map(int,input().split())
pokemon = dict()
for i in range(1,N+1):
    name = input().rstrip('\n')
    pokemon[str(i)] = name
    pokemon[name] = str(i)
    
for _ in range(M):
    order = input().rstrip('\n')
    print(pokemon.get(order))