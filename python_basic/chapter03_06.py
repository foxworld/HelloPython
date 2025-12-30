# Chapter03-5
# 집합(Set) 특징
# 자료형(순서x, 중복x, 수정o, 삭제o)

# 선헌
a = set() # 빈 집합
b = set([1,2,3,4,5]) # 숫자 리스트로 집합 생성
c = set((1,2,3,4,5)) # 튜플로 집합 생성
d = set([1, 2, 'Pen', 'Cap', 'Plate']) # 혼합 자료형 집합 생성
e = {'foot', 'bat', 'ball'} # 중괄호로 집합 생성
f = {42, 'foo', (1,2,3), 3.14159265} # 중괄호로 혼합 자료형 집합 생성

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()


# 튜퓰변환(set -> tuple)
t = tuple(b)
print('tuple(b) - ', type(t), t)
print('t = ', t[0], t[1:3]) # 인덱싱, 슬라이싱
print()

# 리스트변환(set -> list)
l = list(c)
l2 = list(e)
print('list(c) - ', type(l), l)
print('list(e) - ', type(l2), l2)
print('l = ', l[0], l[1:3]) # 인덱싱, 슬라이싱
print()

# 길이
print('len(a) - ', len(a))
print('len(b) - ', len(b))
print('len(d) - ', len(d))
print()

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6])
print('s1 - ', s1)
print('s2 - ', s2)
# 교집합
print('s1 & s2 - ', s1 & s2)
print('s1.intersection(s2) - ', s1.intersection(s2))
# 합집합
print('s1 | s2 - ', s1 | s2)
print('s1.union(s2) - ', s1.union(s2))
# 차집합
print('s1 - s2 - ', s1 - s2)
print('s1.difference(s2) - ', s1.difference(s2))

# 중복원소확인
print('s1 & s2 - ', s1.isdisjoint(s2)) # False

# 부분집합확인
print('s1.issubset(s2) =', s1.issubset(s2)) # False
print('s2.issubset(s1) =', s2.issubset(s1)) # True
print('s1.issuperset(s2) =', s1.issuperset(s2)) # True


# 추가/제거
s1 = set([1,2,3,4])
# 추가
s1.add(5)
print('s1.add(5) - ', s1)
# 제거
s1.remove(5)
print('s1.remove(5) - ', s1)
# s1.remove(7) # 없는 값을 제거하려고 하면 오류 발생
s1.discard(3)
print('s1.remove(3) - ', s1)
s1.discard(7) # 없는 값을 제거해도 오류 발생 안함

s1.clear() # 모두 제거
print('s1.clear() - ', s1)
print()








