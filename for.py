# 파이썬 반복문
# for 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

for v1 in range(10): # 0 ~ 9
    print('v1 is :', v1)
print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is :', v2)
print()

for v3 in range(2, 11, 2):
    print('v3 is :', v3)
print()

sum1 = 0
for v4 in range(1, 1001):
    sum1 = sum1 + v4
print('1 ~ 1000 sum : ', sum1)

print('1 ~ 1000 sum : ', sum(range(1,1001)))
print('1 ~ 1000 4의 배수의 합 : ', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are :', name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number :", n)

# 예제3
word = "Beautiful"

for s in word:
    print('word :', s)
print()

# 예제4
my_info = {
    "name": "Lee",
    "Age": 33,
    "City": "Seoul"
}

for key in my_info:
    print('key :', my_info[key])

for v in my_info.values():
    print('value :', v)

print()

# 예제5
name = 'PineAppLE'
n1 = ''
for n in name:
    if n.isupper():
        n1 = n1 + n
        print(n)
    else:
        print(n.upper())
        n1 = n1 + n.upper()
print(n1)

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 4:
        print('Found : 4!')
        break
    else:
        print('Not found :', num)
print()

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool: # 자료형을 대조할때는 is를 씀
        continue
    print("current type :", type(v))
    print("multiplay by 2", v * 3)
print()

# for - else
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 55:
        print("Found : 55")
        break
else:
    print('Not Found : 55')

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()

# 구구단2
for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i * j)
    print()

# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # dictionary는 순서 X
