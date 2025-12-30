# Chapter04-2
# 파이썬 반복문
# for 실습

# 코딩의 핵심
# for in <collection>
#     <loop body>
# collection : 리스트, 튜플, 문자열, 집합, 사전 등 반복 가능한 자료형
# loop body : 반복할 코드(들)
# for 문의 특징
# collection의 처음부터 끝까지 반복
# 반복할 때마다 collection에서 한 개의 항목을 꺼내서 변수에
# 할당한 후 loop body를 수행
# for 문의 기본 구조

for v1 in range(10):  # 0 ~ 9
    print('v1 is :', v1)
print()
for v2 in range(1, 11):  # 1 ~ 10
    print('v2 is :', v2)
print()
for v3 in range(1, 11, 2):  # 1 ~ 10, 2씩 증가
    print('v3 is :', v3)
print()
for v4 in range(10, 0, -1):  # 10 ~ 1, 1씩 감소
    print('v4 is :', v4)
print()
# 1 ~ 100 합
sum1 = 0
for v in range(1, 101):
    sum1 += v
print(f'1 ~ 100 Sum : {sum1:,}')
print()
print(f'1 ~ 100 Sum : {sum(range(1,101)):,}')
print(f'1 ~ 100 4의 배수의 합 : {sum(range(4,101, 4)):,}')
print()

# Iterable 객체(반복 가능한 객체)
# 문자열, 리스트, 튜플, 집합, 사전
# iterable : 하나씩 꺼낼 수 있는 객체
# 반복 가능한 이유 : 내부적으로 iter() 함수를 호출해서
# iterator 객체를 반환하기 때문
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip 등

# 예제1
names = ['Kim', 'Park', 'Cho', 'Choi', 'Yoo']
for name in names:
    print('You are :', name)
print()

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]
for n in lotto_numbers:
    print('lotto number :', n)
print()

# 예제3
word = 'Beautiful'
for s in word:
    print('word :', s)
print()

# 예제4
my_info = {
    'name': 'Lee',
    'age': 33,
    'city': 'Seoul'
}
for key in my_info:
    print('key :', key, ', value :', my_info[key])
print()
for key, value in my_info.items():
    print('key :', key, ', value :', value)
print()

# 예제5
name = 'FineAppLE'
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 3, 15, 34, 26, 38]
for n in numbers:
    if n == 34:
        print('Found number=', n)
        break
    else:
        print('Not found number=', n)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    print('current type:', v, type(v))
    print("multiply by 2", v * 3)
    print(True * 3)

# for - else
# break 를 만나지 않고 끝나면 else: 를 탄다
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 3, 15, 34, 26, 38]
for num in numbers:
    if num == 55:
        print(f"Found number : {num}")
        break
else:
    print("Not Found number : 55")
print()

# 구구단 출력
for j in range(1, 10):          # 세로 방향(1~9)
    for i in range(2, 10):      # 가로 방향(2~9단)
        print(f"{i} x {j} = {i*j:2}", end="   ")
    print()
print()

# 변환 예제
name2 = 'Aceman'
print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))
