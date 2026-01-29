import jaydebeapi
import socket

print("hello, world!")

s = socket.socket()
try:
    s.connect(("localhost", 9092))
    print("9092 포트 연결 성공")
except Exception as e:
    print("9092 포트 연결 실패:", e)
s.close()

H2_JAR = "C:/tools/h2-2.3.232/bin/h2-2.3.232.jar"
DB_PATH = "C:/tools/test"   # test.mv.db → test 만!

try:
    conn = jaydebeapi.connect(
        "org.h2.Driver",
        f"jdbc:h2:file:{DB_PATH}",
        ["sa", ""],
        H2_JAR
    )
    print("H2 연결 성공 (file 모드)")

    cur = conn.cursor()
    cur.execute("SELECT 1")
    print(cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("연결 실패:", e)

