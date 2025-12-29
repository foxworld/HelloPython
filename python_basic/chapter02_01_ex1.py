# Chapter02-ex1: 출력하기
# 파이썬 완전 기초
# print 사용법
# 파이썬 3가지 print Formatting
# 자주 나오는 print 옵션들

"""
참고 : Escape 문자

\n : 다음 줄로 이동
\t : 탭 간격만큼 이동
\\ : 문자  \
\' : 작은 따옴표  '
\" : 큰 따옴표  "
\000 : 널 문자
"""

### 3가지 Format Practice ###

x = 50
y = 100
text = 304276567
n = 'Hello, Python!'

# 출력1
ex1 = 'n=%s, y=%s, sum=%d' % (n, text, x + y)
print(ex1)

# 출력2
ex2 = 'n={n}, y={s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3
ex3 = f'n={n}, y={text}, sum={x + y}'
print(ex3)
print(f'n={n}, y={text}, sum={x + y}')


# 구분기호
m = 10000000
print(f'm={m:,}')          # 천 단위 콤마

# 정렬
# ^ : 가운데 정렬, < : 왼쪽 정렬, > : 오른쪽 정렬
print(f'[{n:<20}]')        # 왼쪽 정렬
print(f'[{n:>20}]')        # 오른쪽 정렬
print(f'[{n:^20}]')        # 가운데 정렬

print(f'center : [{n:-^20}]')        # 가운데 정렬
print(f'center : [{n:#^20}]')        # 가운데 정렬
print(f'left   : [{n:#<20}]')          # 왼쪽 정렬


