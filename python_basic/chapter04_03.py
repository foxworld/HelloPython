# Chapter04_3
# 파이썬 반복문
# while 실습

# while <expr>:
#    <statement(s)>


# 예제1
n = 5
while n > 0:
    print(n)
    n = n -1
print()

# 예제2
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop())
print()

# 예제3
#  break, continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')
print()

# if 중첩
# 예제4
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
print()

# 예제5
i = 1
while i <= 10:
    print('i:',i)
    if i == 6:
        break
    i += 1

# while - else 구문
# 예제6
n = 10
while n > 0:
    n -= 1
    print(n)
    if n ==11:
        break
else:
    print('else out.')

# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'
i = 0
while i < len(a):
    if a[i] == s:
        print(a[i])
        break
    i += 1
else:
    print(s, 'not found in list.')
print()

# 무한반복
# while True:
#    print('foo')

# 예제8
a = ['foo', 'bar', 'baz', 'qux']
while True:
    if not a:
        break
    print(a.pop())
