# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)


# 선언
a = [] # 빈 리스트
b = list() # 빈 리스트
c = [70, 75, 80, 85] # 정수형 리스트
d = [1000, 10000, 'Ace', 'Base', 'Captain'] # 문자열 리스트
e = [1000, 10000, ['Ace', 'Base', 'Captain']] # 중첩 리스트
f = [21.42, 'foobar', 3, 4, False, 3.14159] # 다양한 자료형 혼합
print(type(a), type(b), type(c), type(d), type(e), type(f))
print()

# 인덱싱
print('>>>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1]) # 인덱스 1
print('d - ', d[0] + d[1] + d[1]) # 인덱스 0,1,1
print('d - ', d[-1]) # 인덱스 -1
print('d - ', d[-3]) # 인덱스 -3
print('e - ', e[-1][1]) # 중첩 리스트 인덱싱
print('e - ', list[e[-1][1]]) # 중첩 리스트 인덱싱
print()

# 슬라이싱
print('>>>>>>>>>')
print('d - ', d[0:3]) # 인덱스 0~2
print('d - ', d[2:]) # 인덱스 2~끝
print('d - ', d[1:4]) # 인덱스 1~3
print('d - ', d[::2]) # 인덱스 처음~끝, 2칸씩
print('d - ', d[1::2]) # 인덱스 1~끝, 2칸씩
print('e - ', e[-1][1:3]) # 중첩 리스트 슬라이싱
print()

# 리스트 연산
print('>>>>>>>>>')
print('c + d - ', c + d) # 리스트 연결
print('c * 3 - ', c * 3) # 리스트 반복
print("'Test' + c[0] - ", 'Test' + str(c[0])) # 문자열 + 정수형 -> 오류
print("'Test' + str(c[0]) - ", 'Test' + str(c[0])) # 문자열 + 정수형 변환  -> 정상
print()

# 값비교
print(c == c[:3] + c[3:]) # 슬라이싱한 값과 원본 리스트 비교
print(c)
print(c[:3]+c[3:])
print()

# Identity(id)
temp = c
print(temp, c) # temp와 c 동일
print(id(temp))
print(id(c)) # id 값 동일
print()


# 리스트 수정, 삭제
print('>>>>>>>>>')
c[0] = 4 # 인덱스 0 수정
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # 인덱스
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 인덱스
print('c - ', c)
c[1:3] = [] # 인덱스 1~2 삭제
print('c - ', c)
del c[2] # 인덱스 2 삭제
print('c - ', c)

# 리스트 함수
print('>>>>>>>>>')
a = [5, 2, 3, 1, 4]
print('a(list)      - ', a)
print('a(append)    - ', a.append(6)) # 마지막에 6 추가
print('a(sort)      - ', a.sort())  # 오름차순 정렬
print('a(reverse)   - ', a.reverse()) # 역순 정렬
print('a(index)     - ', a.index(4)) # 값 4의 인덱스
print('a(insert)    - ', a.insert(2, 7))  # 인덱스 2에 값 7 삽입
print('a(remove)    - ', a.remove(2))  # 값 2 삭제
print('a(pop)       - ', a.pop()) # 마지막 값 추출 및 삭제
print('a(after pop) - ', a)
print('a(count)     - ', a.count(4)) # 값 4 개수 세기
a.extend([8, 9]) # 리스트 확장
print('a(after extend)- ', a) # 리스트 확장
print()

# 반복문 활용
a.sort()
while a:
    data = a.pop()
    print('pop data - ', data)
print(a)
print()

# 리스트 선언 최적화
print('>>>>>>>>>')
b = [i for i in range(1, 21) if i % 2 == 0] # 1~20 짝수 리스트 선언
print('b - ', b)
c = [i * 3 for i in range(1, 21) if i % 2 == 1] # 1~20 홀수 리스트 선언 후 3곱하기
print('c - ', c)





