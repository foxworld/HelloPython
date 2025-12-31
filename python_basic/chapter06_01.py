# Chapter06-1
# 파이썬 클래스
# OOP(객체지향 프로그램밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스, 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능 / java 에서 static 변수 동일함 / 생성없이 메모리에 할당
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: # object 상속
    # 클래스 속성
    species = 'first_dog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)

# 인스터스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('mikky', 2)

# 비교
print(f'a==b {a == b}, id(a)={id(a)}, id(b)={id(b)}')
print(f'a==b {a == c}, id(a)={id(a)}, id(b)={id(c)}')

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'first_dog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

Dog.species = 'second_dog'
print('a.species', a.species)
print('b.species', b.species)

# 예제2
# self의 이해
class SelfTest:
    def func1():
        print('func1 called')

    def func2(self):
        print(id(self))
        print('func2 called')

f = SelfTest()
print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()

SelfTest.func1()
# SelfTest.func2() # 예외
SelfTest.func2(f) # SelfTest f값을 넣어주면 실행됨

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 # 재고

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')
print(user1.stock_num)
print(user2.stock_num)

# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1 #  소멸자를 통해 실행 하게 되면  def __del__(self) 동작
print('after', Warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'first_dog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 ㅅ ㅐㅇ성
c = Dog('july', 4)
d = Dog('marry', 4)
# 메소드 호출
print(c.info())
print(c.speak('hello'))
print(d.info())
print(d.speak('wal wal'))