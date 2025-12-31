# Chapter05-2-ex1
# 파이썬 사용자 입력
# input 사용법
# 기본 타입(str)

# 예제1 -> 예외처리
def func1():
    try:
        n = int(input('Enter a number: '))
        print('Input Your Number: ', n)
    except ValueError:
        print('This is not number!')
# func1()

# 예제2 -> 올바른 값 입력 완료 까지 지속
def func2():
    while True:
        try:
            n = int(input('Enter a number: '))
            print('Input Your Number: ', n)
            break
        except ValueError:
            print('This is not number!')
func2()