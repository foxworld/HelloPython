# Chapter02-01
# 객체 지향 프로그래밍 (OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복작
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딍
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'white'},
    {'horsepower':400},
    {'price':8000}
]
# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'block'},
    {'horsepower':270},
    {'price':5000}
]
# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'silver'},
    {'horsepower':300},
    {'price':6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'white', 'horsepower':400, 'price':8000},
    {'color': 'block', 'horsepower':270, 'price':5000},
    {'color': 'silver', 'horsepower':300, 'price':6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 딕셔너리구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'white', 'horsepower':400, 'price':8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'block', 'horsepower':270, 'price':5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'silver', 'horsepower':300, 'price':6000}}
]
print(car_dicts)
del car_dicts[1]
print(car_dicts)

print()
print()

# Class 구조
# 구조 ㅓㄹ계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, details):
        self.company = company
        self.details = details

    def __str__(self):
        return f'str : {self.company} {self.details}'

    def __repr__(self):
        return f'repr : {self.company} {self.details}'

    def __reduce__(self):
        return type(self), (self.company, self.details)


car1 = Car('Ferrari', {'color': 'white', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color': 'block', 'horsepower':270, 'price':5000})
car3 = Car('Audi', {'color': 'silver', 'horsepower':300, 'price':6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(dir(car1))

print()
print()

car_list =[]
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

# 반복(__str__)
for x in car_list:
    print(repr(x))

print(car1.__reduce__())