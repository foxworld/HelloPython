# Chapter03-5
# 파이썬 dictionary
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Kim', 'phone' : '01033334444', 'birth': '891225'} # key : value
b = {0 : 'Hello Python'} # key : value
c = {'arr' : [1,2,3,4,5]} # key : value(리스트)
d = {
    'name' : 'NiceMan',
    'city' : 'Seoul',
    'age' : 33,
    'grade' : 'A',
    'status' : True
}
e = dict([
    ('name', 'NiceMan'),
    ('city', 'Seoul'),
    ('age', 33),
    ('grade', 'A'),
    ('status', True)
])
f = dict(
    name = 'NiceMan',
    city = 'Seoul',
    age = 33,
    grade = 'A',
    status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()
# 출력
print('a[\'name\']      - ', a['name']) # key로 value 출력
# print('a[\'name1\'] - ', a['name1']) # 없는 key 접근 -> 오류
print('a.get(\'name\')  - ', a.get('name')) # key로 value 출력
print('a.get(\'name1\') - ', a.get('name1')) # 없는 key 접근 -> None 출력
print('b[0]             - ', b[0]) # key로 value 출력
print('c[\'arr\']       - ', c['arr']) # key로 value 출력
print('c[\'arr\'][1]    - ', c['arr'][1]) # key로 value(리스트) 출력 후 인덱싱
print('f[\'city\']      - ', f['city']) # key로 value 출력
print()

# 딕셔너리
a['address'] = 'Seoul' # 다이나믹하게 추가
print('a - ', a)
a['rank'] = [1, 2, 3] # 다이나믹하게 추가
print('a - ', a)

# 딕셔너리 길이
print('len(a) -', len(a)) # key의 개수 출력
print('len(b) -', len(b))
print('len(c) -', len(c))
print('len(d) -', len(d))
print('len(e) -', len(e))
print('len(f) -', len(f))
print()

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 활용 가능
print('a.keys()       - ', a.keys()) # key 반환
print('list(a.keys()) - ', list(a.keys())) # key 리스트형 반환
print('b.keys()       - ', b.keys())
print('c.keys()       - ', c.keys())
print()
print('a.values()       - ', a.values()) # value 반환
print('list(a.values()) - ', list(a.values())) # value 리스트형 반환
print('b.values() - ', b.values())
print('c.values() - ', c.values())
print()
print('a.items()       - ', a.items()) # key, value 쌍 반환
print('list(a.items()) - ', list(a.items())) # key, value 쌍 리스트형 반환
print('b.items()  - ', b.items())
print('c.items()  - ', c.items())
print()

# key로 value 삭제
print('a.pop(\'name\') - ', a.pop('name')) # key로 value 삭제 후 반환
print('a - ', a)
print('a - ', a.popitem()) # 마지막 key, value 쌍 삭제 후 반환
print('a - ', a)
print()

# key 존재 여부 확인
print('a -', 'birth' in a) # key 존재 여부 확인
print('a -', 'city' in a) # key 존재 여부 확인
print('a -', 'address' in a)
print('b -', 0 in b)
print()

# 수정
a['test'] = 'test_dict' # key로 value 추가
print('a - ', a)
a['address'] = 'Busan' # key로 value 수정
print('a - ', a)

a.update(birth = '910225') # update 메서드로 key로 value 수정
print('a - ', a)
a.update(address = 'Incheon') # update 메서드로 key로 value 수정
print('a - ', a)

