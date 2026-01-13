# === 웹크롤링(Web Crawling) === 
* Web(거미줄) + Crawling(기어다니다)
* 웹스크래핑(Web Scraping : 긁어모으다)
* https://cafe.naver.com/startcodingofficial

## 웹크롤링 활용 
* 데이터 분석 : 엄청나게 많은 데이터로 유의미한 인사이트를 얻는 것
* 웹사이트 자동화
* 인공지능 학습 데이터

## 웹크롤링 주요 활용 사례
* 삼품, 컨텐츠 자동 업로드
* 부동산 주식 재테크 데이터 수집
* 인스타그램, 유튜브 모니터링 및 분석
* 뉴스 데이터 수집
* 논문, 구인공고 데이터 수집

## 준비문
* HTML 기초
* CSS 선택자

## 웹사이트 개발의 3요소
* HTML : 구조
* CSS : 디자인
* javascript: 동작

## HTML 이란?
* Hyper Text Markup Language
* 웹사이트의 구조를 표시하기 위한 언어
* 태그구조 
```
<테그이름 속성="속성값">내용</태그이름>
- 내용에는 텍스트나 태그가 들어갈수있다
- 내용은 없어도 된다
```

## CSS 디자인
```css
    h1{ color:red; }
    .large {
        font-size : 32px;
        text-decoration : underline; 
    }
    #titls {
        font-size : 32px;
        text-decoration : underline;
    }
    div > p { 
      font-size : 32px 
    }
```
* 선택자(selector)
  * 웹페이지에서 원하는 태그를 선택하는 문법
* 테그선택자 : 태그이름으로 선택하는것
* 클래스선택자
  * 클래스 속성 값으로 선택하는 것 
  * 클래스는 태그에 별명을 주는 것 
  * 클래스명 구분자 : ```.```  
* 아이디선택자 
  * 아이디 속성 값을 선택하는 것
  * 아이디는 태그에 별명을 주는것
  * 아이디명 구분자 : ```#```
* 자식선택자
  * 바로 아래 자식태그를 선택하는 것
  * 내가 원하는 태그에 별명이 없을 때 사용 
  * 자식선택 구분자 : ```>```

## 웹크롤링 기초
* 정적페이지(static page) 크롤링 : 데이터의 추가적인 변경이 일어나지 않는 페이지
* 정적페이지 크롤링 방법 
  * 데이터 받아오기 
    * 파이썬에서 서버에 요청을 보내고 응답받기 
    * http통신으로 html을 받아오기
  * 데이터 뽑아내기 
    * html에서 원하는 부분만 추출 
    * css 선택자를 잘 만드는것이 핵심

## 실전! 크롤링
* 1단계 : 한개의 상품 크롤링
* 2단계 : 여려개의 상품 크롤링
  * 3단계 : 여러 페이지 크롤링
    * URL(Uniform Resource Locator) 
      * 인터넷 주소 형식
      * Protocol - Domain - Path - Parameter
    * 페이지 알고리즘
      ```aiignore
        https://startcoding.pythonanywhere.com/basic?page=1
        https://startcoding.pythonanywhere.com/basic?page=2
        https://startcoding.pythonanywhere.com/basic?page=3
        https://startcoding.pythonanywhere.com/basic?page=4
      ```
* 4단계 : 데이터 엑셀에 저장

 
