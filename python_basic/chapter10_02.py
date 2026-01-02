# Chapter10-2
# Hangman(행맨) 미니 게입 제작(2)
# 프로그램 완성 및 최종 테스트

import time
import csv
import random
import winsound

# 처음 인사
name = input("What is you name? ")

print("Hi, " + name, "Time to play hangman game!")
print()

time.sleep(1)
print("Start Loading...")
print()
time.sleep(0.5)

# CSV 단어 리스트
words = []

# 문제 csv 파일 로드
with open('./resource/word_list.csv','r') as f:
    reader = csv.reader(f)
    # header skp
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)
q = random.choice(words)
print(q)

#  정답단어
word = q[0].strip()

# 추측단어
guesses = ''

# 기회
turns = 10

# 핵심 while loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답단어반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측단어 출력
            print(char, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print("_", end=' ')
            failed += 1

    #단어 추측이 성공 한 경우
    if failed == 0:
        print()
        print()
        # 성공 사운드
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations! The Guesses is correct.')
        break
    print()

    # 추측 문자 글자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a character.")

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 잏ㅆ지 않으면
    if guess not in word:
        # 기회횟수 차감
        turns -= 1
        # 오류 메시지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", turns, "more guesses!")

        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            # 싶패 메시지
            print("You hangman game failed bye!")
