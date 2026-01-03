# Chapter02-03
# 객체 지향 프로그래밍 (OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복작
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Peter
    Date : 2026.1.3
    Description : class, static, instance method
    """
    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f'str : {self._company} {self._details}'

    def __repr__(self):
        return f'repr : {self._company} {self._details}'

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current id: {id(self)}')
        print(f'Car detail info : {self._company} {self._details.get('price')}')

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, {}'.format(self._company, self._details.get('price'))

    def get_price_culc(self):
        return 'After Car Price -> company : {}, {}'.format(self._company, self._details.get('price') * Car.price_per_raise)


# self 의미
car1 = Car('Ferrari', {'color': 'white', 'horsepower':400, 'price':8000})
car2 = Car('Bmw', {'color': 'block', 'horsepower':270, 'price':5000})

# 전체정보
car1.detail_info()
car2.detail_info()

# 가격정보
print(car1._details.get('price'))
print(car2._details.get('price'))

print(car1.get_price())
print(car1.get_price_culc())

