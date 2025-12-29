# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''
print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str1_t = ''
str2_t = str()
print(type(str1_t), len(str1_t))
print(type(str2_t), len(str2_t))
print()


# 이스케이프 문자 사용
"""
\n : 개행
\t : 탭
\\ : 문자 \
\' : 문자 '
\" : 문자 "
"""

print("I'm Boy")  # 작은 따옴표 포함
print('He said "Python is very easy."')  # 큰 따옴표 포함
print("My name is \"Hong\".")  # 따옴표 포함
print("C:\\Program Files\\Python")  # 역슬래시 포함
print("Hello\nWorld")  # 줄바꿈
print("Hello\tWorld")  # 탭
print()

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s your name?'
print(escape_str1)
print(escape_str2)
print()

# Raw String
raw_s1 = r'D:\python\test\new'  # 역슬래시 그대로 출력
raw_s2 = r"\\a\\b\\c\\" # 역슬래시 그대로 출력
print(raw_s1)
print(raw_s2)
print()

# 멀티라인 입력
multi_str1 = """ 
String with 
multiple lines 
using triple double quotes.
"""
multi_str2 = \
'''
String with
multiple lines 
using triple single quotes.
한글
'''
print(multi_str1)
print(multi_str2)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = " is fun!"
str_o3 = str_o1 + str_o2
print(str_o3) # 문자열 연결
str_o4 = str_o1 * 3
print(str_o4) # 문자열 반복
str_o1 += str_o2
print(str_o1) # 복합 대입 연산
print('y' in str_o1) # 포함 관계 확인
print('z' not in str_o1) # 포함 관계 확인
print()

# 문자열 형 변환
print(str(77), type(str(77)))
print(str(10.4), type(str(10.4)))
print(str(True), type(str(True)))
print()

# 문자열 함수(메서드)
str_f = "  python is Amazing  "
print(len(str_f))  # 문자열 길이
print(str_f.lower())  # 소문자 변환
print(str_f.upper())  # 대문자 변환
print(str_f.rstrip())  # 오른쪽 공백 제거
print(str_f.lstrip())  # 왼쪽 공백 제거
print(str_f.strip())  # 양쪽 공백 제거
print(str_f.replace("python", "Java"))  # 문자열 치환
print(str_f.split())  # 공백 기준 문자열 나누기
print('Capitalize:', 'python'.capitalize())  # 첫 글자 대문자 변환
print('Endswith:', str_f.endswith("ing  "))  # 특정 문자로 끝나는지 확인
print('Find:', str_f.find("is"))  # 특정 문자 위치 반환
print('sort of Find:', sorted(str_f))  # 문자열 정렬
print()

# 반복(시퀀스)
im_str = "Python"
print(dir(im_str))  # 문자열 관련 메서드 출력 __iter__
print()
for s in im_str:
    print(s) # 한 글자씩 출력
print()

# 슬라이싱
str_s = "Nice Python"
print(len(str_s))
print(str_s[0:3])  # 0~2   0부터 3미만
print(str_s[5:])  # 5~끝 5부터 끝까지
print(str_s[:5])  # 처음~4 처음부터 5미만
print(str_s[:len(str_s)])  # 처음~끝 처음부터 끝까지
print(str_s[:])  # 처음~끝 처음부터 끝까지
print(str_s[1:9:2])  # 1~8, 2
print(str_s[-5:-2])  # 뒤에서 5~3
print(str_s[::2])  # 처음~끝, 2
print(str_s[::-1])  # 처음~끝, -1 (역순)
print()

# 아스키코드
a = 'z'
print(ord(a))  # 문자 -> 아스키코드
b = 122
print(chr(b))  # 아스키코드 -> 문자
print()

# 반복문 + 아스키코드
for c in range(ord('a'), ord('z')+1):
    print(chr(c), end=' ')
print()
for c in range(97, 123):
    print(chr(c), end=' ')
print()






