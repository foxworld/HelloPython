# Chapter09-1
# 파일일기 및 쓰기

# 읽기 모드 : r,  쓰기모드 : w, 추가모드 : a, 텍스트모드 : t, 바이너리 모드 : b
# 상대경로('../,/'), 절대경로('c:/workspaces/example...')

# 파일읽기(read)
# 예제1
f = open('./resource/it_news.txt', 'r', encoding='UTF-8')
# 속성확인
print(dir(f))
# 인코딩확인
print(f.encoding)
# 파일이름
print(f.name)
# 모드확인
print(f.mode)

cts = f.read()
print(cts)

# 반드시 close
f.close()

# 예제2
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read() : 전체읽기,  read(10) : 10 bytes
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(100)
    print(c)

print()

# 예제4
# readline : 한줄씩 읽기

with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예제5
# readlines :  전체를 읽은 후 라인 단위ㅣ 리스트 저장
with open('./resource/it_news.txt', 'r', encoding='UTF-8') as f:
    cts  = f.readlines()
    print(cts)
    print()
    for c in cts:
            print(c, end='')

print()

# 파일 쓰기(write)
# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['Orange\n','Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)



