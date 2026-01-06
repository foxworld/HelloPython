# Chapter04-04
# 시퀀스형
# 해시테이블(Hashtable) -> 적은 리소스를 많은 데이터를 효츌적으로 관리
# Dict -> Key 중복 허용X, Set -> 중복 허용 X
# Dict 및  Set 심화

# immutable Dict

from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

# 수정 불가
# d_frozen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'value2'
print(d)

print()
print()

s1 = {'Apple','Orange','Apple','Orange','Kiwi'}
print(s1, type(s1))
s2 = set(['Apple','Orange','Apple','Orange','Kiwi'])
print(s2, type(s2))
s3 = {3}
print(s3, type(s3))
s4 = set()
print(s4, type(s4))
s5 = frozenset({'Apple','Orange','Apple','Orange','Kiwi'})
print(s5, type(s5))

s1.add('Melon')
print(s1)

# 선언 최적화
# 바이트코드 -> 파이썬 인터프린터 실행
from dis import dis
print('-'*20)
print(dis('{10}'))
print('-'*20)
print(dis('set([10])'))

# 지능형 집합(Comprehending set)
print('-'*20)
from unicodedata import name
print({name(chr(i),'') for i in range(0, 256)})

