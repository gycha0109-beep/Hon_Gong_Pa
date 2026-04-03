lst = []
for i in range(50):
    A = int(input())
    lst.append(A)
print(*lst[::-1])

# print(*[int(input()) for i in range(50)][::-1])
