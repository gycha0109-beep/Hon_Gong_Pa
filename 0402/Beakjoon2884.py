H, M = map(int, input().split())
newtime = H*60 + M-45
if newtime < 0:
    newtime += 1440
print(f"{newtime//60} {newtime%60}")