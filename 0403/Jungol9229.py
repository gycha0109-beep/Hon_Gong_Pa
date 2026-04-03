age = int(input())
if age >= 13:
    print("Middle School")
else:
    print("Elementary School")

# print("Middle School" if int(input()) >= 13 else "Elementary School")

'''
age = int(input())
schools = ["Elementary School", "Middle School"]
print(schools[age >= 13]) # False면 0, True면 1을 리스트 인덱스해서 찾음
'''