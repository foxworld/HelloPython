# Chapter08-1
# 파이썬 내장(Built-in) 함수
# 사용하다보면 자연스럽게 숙달
# str(), int(), tuple() 형변환 이미 학습

# 절대값
# abs()
print('abs(-1) -', abs(-1))

# all, any : iterable 요소 검사(참 ,거짓)
print('all([1,2,3]) -', all([1,2,3])) # and
print('any[1,2,0] - ', any([1,2,0]))    # or


# chr : 아스키 -> 문자, ard : 문자 -> 아스키
print('chr(67) -', chr(67))
print('ord(\'C\') -', ord('C'))

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# filter : 반복가능한 객체 요소를 지정ㅎ산 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2
print('filter -', list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print('filter -', list(filter(lambda x: abs(x) > 2,[1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스) 변환
print('id(int(5)) -', id(int(5)))
print('id(4) -', id(5))

# len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1,2,3,4,5,6,7,8]))

# max, min : 최대값, 최소값
print(max([1,2,3]))
print(max('Python study'))
print(min([1,2,3]))
print(min('Python_study'))

# map : 반복가능한 객체 요소를 지정한 함 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x:abs(x), [1, -3, 2, 0, -5, 6])))

# pow : 제곱값 반환
print(pow(2,10))

# range : 반복 가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# round : 반올림
print(round(6.5781, 2))
print(round(6,5))

# sorted : 반속 가능한 객체 (Iterable)
print(sorted([6,4,3,1,2]))
a = sorted([6,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10]))
print(sum(range(1,101)))


# type : 자료형확인
print(type(3))
print(type({3,4}))
print(type(()))
print(type([]))

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10,20,30],[40,50,60,70])))
print(type(list(zip([10,20,30],[40,50,60,70]))[0]))
