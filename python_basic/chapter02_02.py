# Chapter02-2: 출력하기
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75
# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))
print()

# Object References
# 변수값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 할당
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777
print(n, type(n))

m = n
# m -> 777 < - n
print(m, type(m))
print()

m = 400
print(m, n)
print()

# id(identity} 확인 : 객체의 고유값 확인
m=800
n=655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m=800
n=800
z=800
print(id(m))
print(id(n))
print(id(m) == id(n))
print(id(m) == id(z))
print()


# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> 주로 함수명, 변수명
# Pascal Case : NumberOfCollegeGraduates -> 주로 클래스명
# Snake Case  : number_of_college_graduates  -> 주로 변수명, 함수명 ( 파이썬 권장 )

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_age_ = 8
# 1age = 9        # 숫자로 시작 불가
# age-1 = 10      # 특수문자 불가

# 예약어는 변수명에 사용 불가
# for = 11      # 오류
"""
** 예약어 목록 **
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
"""