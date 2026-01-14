## Web Scraping
### xpath
```aiignore
    <학교 이름="나도고등학교">
        <학년 value="1학년">
            <반 value="1반">
                <학생 value="1번" 학번="1-1-1">이지은</학생>
                <학생 value="2번" 학번="1-1-2">유재석</학생>
                <학생 value="3번" 학번="1-1-3">조세호</학생>
                <학생 value="4번" 학번="1-1-4">박명수</학생>
                <학생 value="5번" 학번="1-1-5">이지은</학생>
            </반>
            <반 value="2반"/>
            <반 value="3반"/>
            <반 value="4반"/>
        </학년>
        <학년 value="2학년"/> ... 3반 유재석 <...>
        <학년 value="3학년"/>
    </학교>
```
```aiignore
  //*[@학번="1-1-5"]
  * ```//``` : 모든 하위경로
  * ```*``` : 모든 엘리먼트
  * ```@학번``` : id Key(유니크)
  * ```1-1-5``` : 값
```

* XPath는 XML/HTML 문서에서 노드(요소, 속성 등)를 찾기 위한 경로 표현식
* 절대/상대 경로
  * 절대: 루트부터 정확히 지정 (/root/child/...)
  * 상대: 문서 내 어디서나 탐색 (//node)
* 노드와 속성
  * 요소 선택: node
  * 속성 선택: @attr
* 프레디케이트(조건)
  * 인덱스: [2] (두번째 자식)
  * 조건: [@id="foo"], [text()="값"]
* 함수
  * contains(), starts-with(), text(), normalize-space() 등
* 축(axes)
  * 부모: parent::node()
  * 조상: ancestor::node()
  * 형제: following-sibling::node(), preceding-sibling::node()


## 정규식(Regular Expression)
### 패턴
* ```.``` (ca.e): 하나의 문자를 의미 > care, cafe, case | caffe
* ```^``` (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
* ```$``` (se\$) : 문자열의 끝 >  case, base (O) | face (X)
### 함수
* p = re.compile("원하는 패턴")
* m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
* m = p.search("비교할 문자열") : 주어진 문자열 중 일치하는지 확인
* lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

