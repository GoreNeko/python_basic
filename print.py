# print 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 3, s : 'python', f : 3.141592)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice')) #왼쪽을 _로 채움
print('{:^10}'.format('nice')) #중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy')) #10만큼의 공간을 확보하지만 5글자만 나오게 절삭.

print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%1.8f' % (3.141592)) # 정수는 1자리, 소수는 8자리
print('{:f}'.format(3.141592))
print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))