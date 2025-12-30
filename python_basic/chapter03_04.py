# Chapter03-4
# 파이썬 튜풀
# 리스트와 비교 중요
# 퓨틀 자료형(순서o, 중복o, 수정x, 삭제x) # 불변

# 선언
a = () # 빈 튜플
a1 = (1,) # 요소가 1개인 튜플, 쉼표 필수
print(type(a), type(a1))

b = tuple() # 빈 튜플
c = (70, 75, 80, 85) # 정수형 튜플
d = (1000, 10000, 'Ace', 'Base', 'Captain') # 문자열 튜플
e = (1000, 10000, ('Ace', 'Base', 'Captain')) # 중첩 튜플
f = (21.42, 'foobar', 3, 4, False, 3.14159) # 다양한 자료형 혼합
print(type(a), type(b), type(c), type(d), type(e), type(f))
print()

# 인덱싱
print('>>>>>>>>>')
print('d              - ', type(d), d)
print('d[1]           - ', d[1]) # 인덱스 1
print('d[0]+d[1]+d[1] - ', d[0] + d[1] + d[1]) # 인덱스 0,1,1
print('d[-1]          - ', d[-1]) # 인덱스 -1
print('d[-3]          - ', d[-3]) # 인덱스 -3
print()

print('e               - ', type(e), e)
print('e[2]            - ', e[2]) # 중첩 튜플 인덱싱
print('e[-1][1]        - ', e[-1][1]) # 중첩 튜플 인덱싱
print('tuple[e[-1][1]] - ', tuple[e[-1][1]]) # 중첩 튜플 인덱싱
print('list(e[-1][1])  - ', list(e[-1][1]) ) # 중첩 튜플 인덱싱 후 리스트 변환
print()

#  수정
# d[0] = 1500 # 튜플은 수정 불가 -> 오류
# print(d)

# 슬라이싱
print('>>>>>>>>>')
print('d[0:3]     - ', d[0:3]) # 인덱스 0~2
print('d[2:]      - ', d[2:]) # 인덱스 2~끝
print('d[1:4]     - ', d[1:4]) # 인덱스 1~3
print('d[::2]     - ', d[::2]) # 인덱스 처음~끝, 2칸씩
print('d[1::2]    - ', d[1::2]) # 인덱스 1~끝, 2칸씩
print('e[-1][1:3] - ', e[-1][1:3]) # 중첩 튜플 슬라이싱
print()

# 튜플 연산
print('>>>>>>>>>')
print('c + d - ', c + d) # 튜플 연결
print('c * 3 - ', c * 3) # 튜플 반복
print("'Test' + c[0] - ", 'Test' + str(c[0])) # 문자열 + 정수형 -> 오류
print("'Test' + str(c[0]) - ", 'Test' + str(c[0])) # 문자열 + 정수형 변환  -> 정상
print()

# 튜플 함수
print('>>>>>>>>>')
print('c        - ', c)
print('c.index(80) - ', c.index(80)) # 값 80의
print('c.count(80) - ', c.count(80)) # 값 80의 개수
print()

# 패킹 & 언패킹(packing & Unpacking)
print('>>>>>>>>>')
t = ('foo', 'bar', 'baz', 'qux') # 패킹
print(t)
print(t[0])
print(t[-1])
print()

(x1, x2, x3, x4) = t # 언패킹
print(type(x1), type(x2), type(x3), type(x4))
print('Unpacking -', x1, x2, x3, x4)
print()

# 패키 & 언패킹
t2 = 1, 2, 3 # 패킹
t3 = 4, # 패킹
x1, x2, x3 = t2 # 언패킹
x4, x5, x6 = (4, 5, 6) # 언패킹
print('t2 - ', t2)
print('t3 - ', t3)
print('x1, x2, x3 - ', x1, x2, x3)
print('x4, x5, x6 - ', x4, x5, x6)




