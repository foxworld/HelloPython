# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError 등
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 예외로 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다
# 4. 예외 무시

# SyntaxError :  문법오류
# print('error)
# print('error'))
#if True
#    pass

# NameError 참조가 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError
# print(100 / 0)

# IndexError
x = [50, 70, 90]
#print(x[1])
#print(x[3])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError
# dic = {'name': 'Lee', 'age': 41, 'city': 'busan'}
# print(dic['hobby'])
# print(dic.get('hobby'))

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP:Easier to Ask Forgiveness than Permission)

# AttributeError : 모류 클래스엣 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError
# x = [10, 50, 90]
# x.remove(50)
# x.remove(200)

# FileNotFoundError
# f = open('test.txt')

# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'
# print(x + y)
# print(x + z)
# print (y + z)
# print(x + list(y))

# 예외처리 기분
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1: 여러개 가능
# except 에어명2
# else : try  블럭의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['kim', 'lee','park']

# 예제1
# try:
#     z = 'kim' # 'cho' # 예외발생 값
#     x = name.index(z)
#     print('{} Found it {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! -= Occurred ValueError!')
# else:
#     print('OK! else.')
#
# print()

# try:
#     z = 'cho' # 예외발생 값
#     x = name.index(z)
#     print('{} Found it {} in name'.format(z, x + 1))
# except:
#     print('Not found it! -= Occurred ValueError!')
# else:
#     print('OK! else.')
#print()

# 에제 3
# try:
#     z = 'cho' # 예외발생 값
#     x = name.index(z)
#     print('{} Found it {} in name'.format(z, x + 1))
# except Exception as e:
#     print(e)
#     print('Not found it! -= Occurred ValueError!')
# else:
#     print('OK! else.')
# finally:
#     print('OK! finally')

print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
try:
    a = 'park'
    if a == 'park':
        print('OK! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occurred Exception!')
else:
    print('OK! else.')

print()
