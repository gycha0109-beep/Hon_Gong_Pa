class Player():
    def __init__(self, name, AB, H):
        self.name = name
        self.AB = AB
        self.H = H
    def avg(self):
        return round(self.H / self.AB, 3)
    def profile(self):
        return f"name:{self.name}, AVG:{self.avg()}, AB:{self.AB}, H:{self.H}"

players = []

for _ in range(2):
    A, B, C = input().split()
    players.append(Player(A, int(B), int(C)))

for i in players:
    print(i.profile())