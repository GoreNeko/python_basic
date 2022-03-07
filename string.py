# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) #문자열의 길이

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자(\) 사용

print("I'm Boy")
print('I\'m Boy')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String 이스케이프 문자를 사용하지 않음
raw_s1 = r'D:\python\test'

print(raw_s1)
print()

# 멀티라인 입력
# 역슬래시 사용
multi_str = \
"""
String
Multi line
Test
"""
print(multi_str)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How arte you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) #str_o1 안에 y라는 글자가 포함되어 있는지
print('n' in str_o1)
print('P' not in str_o2)

print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 첫글자를 대문자로 바꿈
print("endswith?: ", str_o2.endswith("e")) # 마지막에 e로 끝나는지?
print("replace", str_o1.replace("thon", ' Good')) # 치환
print("sorted: ", sorted(str_o1)) # 순서가 정렬되어서 리스트형태로 나옴
print("split: ", str_o4.split(' ')) # 분리
print()

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_sl = "Nice Python"

print(len(str_sl))
# 슬라이싱 연습
print(str_sl[0:3]) # 0에서 3까지, 0 1 2
print(str_sl[5:]) # [5:끝]
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1])
print(str_sl[1:9:2]) # 1부터 4까지 가져오는데 2개씩 건너뛰어서 가져옴
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1]) # 역으로 출력
print()

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) #문자를 아스키코드로
print(chr(122)) # 아스키코드를 문자로