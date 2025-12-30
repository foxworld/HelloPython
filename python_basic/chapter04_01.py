# Chapter04-1
# 파이썬 제어문
# if 실습

# 기본 형식
print(type(True)) # <class 'bool'>  / 0이 아닌 수, "abc", [1,2,3] 등은 True로 간주
print(type(False)) # <class 'bool'> / 0, "", [], None 등은 False로 간주
print()

# 예1
if True:
    print('Good')
if False:
    print('Bad')

# 예2
if False:
    print('Bad!')
else:
    print('Good!')

# 관계연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10
print('x=', x, ', y=', y) # 콤마(,) 사용 방식
print('x={}, y={}'.format(x, y)) # 기본 포맷 방식
print('x={x}, y={y}'.format(x=x, y=y)) # f-string 이전 방식
print(f'x={x}, y={y}') # f-string 방식
print('x > y  -', x > y)  # True
print('x >= y -', x >= y)  # True
print('x < y  -', x < y)  # False
print('x <= y -', x <= y)  # False
print('x == y -', x == y)  # False
print('x != y -', x != y)  # True
print()

# 예3
city = ""
if city:  # 빈 문자열은 False로 간주
    print("You are in", city)
else:
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in", city)
else:
    print("Please enter your city")
print()

# 논리연산자
# and, or, not
a = 75
b = 40
c = 10
print('a=', a, ', b=', b, ', c=', c)
print('a > b and b > c :', a > b and b > c) # a > b > c
print('a > b or b > c  :', a > b or b > c) # 앞부분이 True이면 뒷부분은 검사하지 않음
print('not a > b       :', not a > b) # a > b True -> not True = False
print('not True - ', not True)
print('not False - ', not False)
print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1 :', 3 + 12 > 7 + 4)  # 산술
print('e2 :', 5 + 10 * 3 > 7 + 3 * 20)  # 산술
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10)  # 산술 > 관계 > 논리
print('e4 :', 5 + 10 > 3 and not 7 + 3 == 10)  # 산술 > 관계 > 논리

# 예4
score1 = 90
score2 = 'A'
print(f'score1={score1}, score2={score2}')
# 복수의 조건이 모두 참일 경우에 신행
if score1 >= 90 and score2 >= 'A':
    print('Pass')
else:
    print('Fail')
print()

# 예5
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'
print(f'id1={id1}, id2={id2}, grade={grade}')
# 복수의 조건 중 하나라도 참일 경우에 신행
if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')
else:
    print('일반 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자 입장')
print()

# 예6
# 다중 조건문
num = 90
print(f'num={num}')
if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('Grade : D')
print()

# 중첩조건문
grade = 'A'
total = 95
print(f'grade={grade}, total={total}')
if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금없음')

# in, not in
q = [10, 20, 30] # 리스트
w = {70, 80, 90, 100} # 집합
e = {'name': 'Lee', 'city': 'Seoul', 'grade': 'A'} # 딕셔너리
r = (10, 12, 14) # 튜플

print('15 in q =', 15 in q) # False
print('20 in q =', 20 in q) # True
print('90 in w =', 90 in w) # True
print('100 not in w =', 100 not in w) # False
print("'name' in e =", 'name' in e) # True
print("'Seoul' in e.values() =", 'Seoul' in e.values()) # True



