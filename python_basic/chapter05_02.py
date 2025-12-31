# Chapter05-2
# 파이썬 사용자 입력
# input 사용법
# 기본 타입(str)

# 예제1
def func1():
    name = input('Enter Your name: ')
    grade = input('Enter Your Grade: ')
    company = input('Enter Your Company name: ')
    print(name, grade, company)

# 예제2
def func2():
    number = input('Enter number: ')
    name = input('Enter name: ')
    print('Type of number', type(number), number * 3)
    print('Type of name', type(name))

# 예제3
def func3():
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))
    print('first_number+second_number: ', first_number+second_number)

# 예제4
def func4():
    float_number = float(input('Enter float number: '))
    print('input float :', float_number)
    print('input type :', type(float_number))

# 예제5
def func5():
    print('First Name - {0}, Last Name - {1}'.format(input('Enter first name: '), input('Enter last name: ')))

# func1()
# func2()
# func3()
# func4()
func5()
