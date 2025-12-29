# Chapter02-1
# 파이썬 완전 기초
# print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 문자

\n : 다음 줄로 이동
\t : 탭 간격만큼 이동
\\ : 문자  \
\' : 작은 따옴표  '
\" : 큰 따옴표  "
\000 : 널 문자
"""

# 기본출력
print('Python Start!')  # 작은 따옴표 사용
print("Python Start!")  # 큰 따옴표 사용
print("""Python Start!""")  # 삼중 따옴표 사용
print('''Python Start!''')  # 삼중 따옴표 사용
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N')
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')  # sep 옵션에 빈 문자열 설정
print('P', 'Y', 'T', 'H', 'O', 'N', sep='-')  # sep 옵션에 하이픈 설정
print('010', '1234', '5678', sep='-')  # sep 옵션에 하이픈 설정
print('python', 'google', 'com', sep='.')  # sep 옵션에 점 설정
print()

# end 옵션
print('Welcome to', end=' ')
print('the world of', end=' ')
print('Python Programming!')

# file 옵션
import sys

print('Learn Python Programming', file=sys.stdout)  # 표준 출력
print('Learn Python Programming', file=sys.stderr)  # 표준 에러 출력
print()

# format 사용(d, s, f)
print('{} {}'.format('Learn', 'Python Programming'))  # 기본 사용
print('{0} {1}'.format('Learn', 'Python Programming'))  # 인덱스 사용
print('{1} {0}'.format('Learn', 'Python Programming'))  # 인덱스 사용
print()

print('I am %d years old.' % 20)  # 정수형
print('I am %s years old.' % 'twenty')  # 문자열형
print('%10s' % 'hi')  # 전체 10자리 확보
print('{:>10}'.format('hi'))  # 오른쪽 정렬
print('%-10s' % 'hi')  # 왼쪽 정렬
print('{:<10}'.format('hi'))  # 왼쪽 정렬
print('{:_>10}'.format('hi'))  # 왼쪽 정렬
print('{:^10}'.format('hi'))  ## 가운데 정렬
print('%.5s' % 'hello') # 앞에서 5자리
print('%.5s' % 'hello,world')  # 앞에서 5자리
print('{:10.5}'.format('hello,world'))  # 전체 10자리, 앞에서 5자리
print()

print('%d %d' % (1,2))  # 튜플 사용
print('{} {}'.format(1,2))  # format 사용

print('%4d' % 42)  # 전체 4자리 확보
print('{:4d}'.format(42))  # 전체 4자리 확보
print('%04d' % 42)  # 전체 4자리, 빈자리 0으로 채우기
print('{:04d}'.format(42))  # 전체 4자리, 빈자리 0으로 채우기
print()

print('PI is %f' % 3.141592653589793)  # 실수형
print('PI is %.2f' % 3.141592653589793)  # 소수점 2자리
print('PI is %.5f' % 3.141592653589793)  # 소수점 5자리
print('PI is {:0.2f}'.format(3.141592653589793))  # 소수점 2자리
print('PI is {:0.5f}'.format(3.141592653589793))  # 소수점 5자리
print('Pi is %06.2f' % 3.141592653589793)  # 전체 6자리, 빈자리 0으로 채우기, 소수점 2자리
print('Pi is {:06.2f}'.format(3.141592653589793))  # 전체 6자리, 빈자리 0으로 채우기, 소수점 2자리
print()

