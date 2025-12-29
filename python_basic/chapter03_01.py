# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
"""
int  : 정수
float: 실수
complex : 복소수
bool : 불린 (True, False)
str  : 문자열(시퀀스)
list : 리스트 (배열)(시퀀스)
tuple : 튜플 (고정 배열)(시퀀스)
set  : 집합
dict : 사전 (key-value 쌍)
"""

# 데이터 타입
str1 = "Python"
bool1 = True
str2 = 'Anaconda'
float1 = 10.0    # 10.0 = 10
int1 = 7
list1 = [str1, str2]
dict1 = {'name':'Machine Learning', 'version':2.0}
tuple1 = (7, 8, 9)
set1 = {3, 5, 7}
complex1 = 3 + 5j
print(type(str1), type(bool1), type(str2))
print(type(float1), type(int1))
print(type(list1), type(dict1), type(tuple1), type(set1), type(complex1))
print()


# 숫잫ㅇ 연산자
"""
+ : 더하기
- : 빼기
* : 곱하기
/ : 나누기 (실수형)
// : 몫
% : 나머지
** : 제곱 
abs(x) : 절대값
pow(x, y) : x의 y제곱  x**y = 2  ** 3 = 2 * 2 * 2
divmod(x, y) : x를 y로 나눈 몫과 나머지를 튜플 형태로 반환 
"""

# 정수선언
i = 77
i2 = -14
big_int = 7777777777777777777777777777777777777777777
print(i, i2, big_int)
print(type(i), type(i2), type(big_int))
print()

# 실수선언
f = 0.9999
f2 = 3.14159265358979
f3 = -3.9
f4 = 3 / 9
print(f, f2, f3, f4)
print(type(f), type(f2), type(f3), type(f4))
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 7777777777777777777777777777777777777
big_int2 = 8888888888888888888888888888888888888
f1 = 1.234
f2 = 3.939
print(">>>>> + <<<<<")
print("i1 + i2 : ", i1 + i2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print("f1 + f2 : ", f1 + f2)
print()

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7
print(type(a), type(b), type(c), type(d))

