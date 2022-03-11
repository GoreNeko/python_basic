# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 75] #len
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.141592]

# 인덱싱 : 내가 원하는 데이터를 꺼내오는 과정
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))
print()

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])
print()

# 리스트 연산
print('>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))
print()

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()

# 리스트 수정, 삭제
print('>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2]
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)

a.append(10) # 끝 부분에 데이터를 삽입
print('a - ', a)
a.sort() # 오름차순으로 정렬
print('a - ', a)
a.reverse() # 순서를 뒤집음
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # 2번째 위치에 7을 삽입
print('a - ', a)
#del a[6]
a.remove(1) # 1이라는 값을 제거.
print('a - ', a)
print('a - ', a.pop()) # 리스트에서 마지막 index에 해당하는 원소를 가져오고, 나머지 원소들로 리스트를 재 구성.
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 4의 갯수가 몇개인지
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
