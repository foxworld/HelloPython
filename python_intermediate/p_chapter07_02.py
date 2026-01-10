# Chapter07-01
# AsyncIO
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# Non-blocking 비동기 처리

# Blocking I/O : 호출된 함수가 자신의 작업이 완료 될때까지 제어권을 가지고 있음
# NonBlocking I/O : 호출된 함수가 리턴후 호출한 함수(메인함수) 에 제어권 전달 -> 타함수 일 지속

# 쓰레드 단점 : 디버깅, 지원 접근 시 레이스컨디셔(경쟁상태), 데드락) -> 고려후 코딩
# 코루틴 장점 : 하나의 루틴만실행 -> 락 관리 필요X -> 제어권으로 실행
# 코루틴 단점 : 사용함수가 비동기로 구현이 되어 있어야 하나거나, 또는 직접 비동기로 구현

import asyncio
import timeit
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import threading

# 실행 시작시간
start = timeit.default_timer()
# 서비스 방향이 비슷한 사이트로 실습 권장(예 게시판성 켜뮤니티)
urls = [
    'https://daum.net',
    'https://naver.com',
    'https://mlbpark.donga.com',
    'https://tistory.com'
]

async def fetch(url, executor):
    loop = asyncio.get_running_loop()  # 수정된 부분

    # 쓰레드명 출력
    print('Thread Name : ', threading.current_thread().name, 'Start', url)
    # 실행
    req = Request(url, headers={
        'User-Agent': 'Mozilla/5.0'
    })

    res = await loop.run_in_executor(executor, urlopen, req)

    soup = BeautifulSoup(res.read(), 'html.parser')
    # 전체 페이지 소스 확인
    # print(soup.prettify())
    result_data = soup.title

    print('Thread Name : ', threading.current_thread().name, 'Done', url)

    #결과반환
    return result_data

async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)
    # future 객체 모아서 gather 에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    # 결과 취합
    rst = await asyncio.gather(*futures) # Unpacking
    print()
    print('Result : ', rst)


if __name__ == '__main__':
    #루프 초기화
    # loop = asyncio.get_event_loop()
    # 작업오완료까지 대기
    asyncio.run(main())
    # 수행시간 계산
    duration = timeit.default_timer() - start
    #총실행시간
    print(f'Total Running Time : {duration:.4}s')

