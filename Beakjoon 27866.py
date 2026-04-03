S = input() 
i = input() # input 두 개로 입력값 두 개 생성
n = int(i) # i는 기본적으로 문자열이므로 정수형으로 다시 형 변환해줌
print(S[i-1]) # 그냥 'i'만 하면 i 직전의 문자가 나오므로 -1을 해줘야함

# print(input()[int(input())-1]) 이런식으로도 가능함.

