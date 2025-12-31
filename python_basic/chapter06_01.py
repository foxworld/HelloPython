# Chapter06-1
# 파이썬 클래스
# OOP(객체지향 프로그램밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스, 인스턴스 차이 이해

# 예제1
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
