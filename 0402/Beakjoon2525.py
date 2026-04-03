H, M = map(int, input().split())
cook = int(input())
A = (H*60 + M + cook) % 1440
print(f"{A//60} {A%60}")