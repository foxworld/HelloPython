# Chapter08-2
# 파이썬 외장(External)함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time ,random 등

# 예제1
import sys
print(sys.argv)

# 얘제2(강제종료)
# sys.exit()

# 예제3(파이썬 패키지 위치)
print(sys.path)

# pickle :  객체 파일 쓰기
import pickle

# 예제4(쓰기)
f = open('test.obj', 'wb')
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj, f)
f.close()

# 예제5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

#  os : 환경변수, 디렉토리(파일) 처리 관련 운영체제 작업 관련
# mkdir, rmdir(비어있으면 삭제), rename

#예제6
import os
print(os.environ)
print(os.environ["USERNAME"])
print(os.environ["PYTHONUSERBASE"])

# 예제7
print(os.getcwd())