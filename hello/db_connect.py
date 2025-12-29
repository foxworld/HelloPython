import jaydebeapi

# 1. 연결 정보 설정
h2_jar_path = r"C:/Users/이훈구/OneDrive/Apps/h2-2.3.232/bin/h2-2.3.232.jar"  # H2 드라이버 JAR 파일 경로
jdbc_url = "jdbc:h2:~/test"    # 실제 H2 URL로 변경
username = "sa"                # H2 계정
password = ""                  # 비밀번호(없으면 빈 문자열)

# 2. H2 데이터베이스 연결
try:
    print("Connecting to H2 database...")
    conn = jaydebeapi.connect(
        "org.h2.Driver",          # H2 드라이버 클래스 이름
        jdbc_url,
        [username, password],
        h2_jar_path
    )
    print("Connection:", conn)
except Exception as e:
    print("Connection failed:", e)

# 3. 커서 생성
cur = conn.cursor()

# 4. SELECT 실행
sql = "SELECT id, name FROM TEST_TABLE"
cur.execute(sql)

# 5. 결과 가져오기
rows = cur.fetchall()

# 6. 결과 화면(콘솔)에 출력
print("=== SELECT 결과 ===")
for row in rows:
    # row는 튜플 형태 (id, name)
    print(f"id={row[0]}, name={row[1]}")

# 7. 자원 정리
cur.close()
conn.close()