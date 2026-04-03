lang = 'PYTHON'
print(lang) # PYTHON
print(lang[0]) # P 인덱스 0 (0부터 시작)
print(lang[-1]) # N 인덱스 -1 (끝에서 1번째)
print(lang[:3]) # PYT 인덱스 0부터 2까지
print(lang[2:]) # THON 인덱스 2부터 끝까지
print(lang[:]) # PYTHON 인덱스 0부터 끝까지

num = 3
num += 2 # num = num + 2
print(num) # 5

num -= 1 # 4 
num *= 2 # 8
num /= 4 # 2.0
print(num) # 2.0

snack = '꿀꽈배기'
print(len(snack)) # 4 = 문자열의 길이

snack = '''꿀꽈배기는
너무
맛있어요'''
print(snack)

print('-' * 10) # -를 10번 출력하겠다
print('Nadocoding')
print('*' * 20) # *를 20번 출력하겠다

# 문자열 메소드 
letter = 'How are YOU?'
print(letter.lower()) # 소문자로 변환
print(letter.upper()) # 대문자로 변환
print(letter.capitalize()) # 첫글자를 대문자로 변환
print(letter.title()) # 각 단어의 첫글자를 대문자로 변환
print(letter.swapcase()) # 대소문자 반전
print(letter.split()) # 하나의 문자열을 각각의 배열로 변환함. 제일 많이 쓰임
print(letter.count('How')) # 'How'가 몇 번 쓰였는가?

# 문자열 메소드 2
s = '나도고등학교'
print(s.startswith('나도')) # '나도'라는 값으로 시작하는가? => True
print(s.endswith('초등학교')) # '초등학교'라는 값으로 끝나는가? => False
print(s.endswith('고등학교')) # '고등학교'라는 값으로 끝나는가? => True
print(s.replace('고등학교', '고교')) # '고등학교'를 '고교'로 대체시키겠다.
print(s.find('학교')) # 찾고자 하는 문자의 위치가 몇 번째인가?(인덱스 형식)
print(s.find('너도')) # **찾고자 하는 문자가 없을때는 결과값이 '-1'이다.**
print(s.center(10, '-')) # 변수를 가운데로 두고 나머지를 '-'로 채우면서 10의 길이를 맞추겠다

s2 = '...나도고등학교...'
print(s2.strip('.')) # 맨앞, 맨뒤의 '.'값을 제거

s3 = '.,.나도고등학교.,.'
print(s3.strip('.')) # 안쪽의 콤마는 안잘려나갔다.

s4 = '나도고등학교 너도고등학교'
print(s4.replace('고등학교','고교')) # 여러개도 다 바꿔준다