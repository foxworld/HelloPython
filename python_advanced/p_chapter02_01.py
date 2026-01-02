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
# 관리하기가 불폍
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari','Bmw', 'Audi']
car_detail_list = [
    {'color': 'white','horsepower':400, 'price':8000},
    {'color': 'block','horsepower':270, 'price':5000},
    {'color': 'silver', 'horsepower':300, 'price':6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 딕셔너리구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'white','horsepower':400, 'price':8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'block','horsepower':270, 'price':5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'silver', 'horsepower':300, 'price':6000}}
]
print(car_dicts)
del car_dicts[1]
print(car_dicts)

print()
print()
