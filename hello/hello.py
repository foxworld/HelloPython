import jaydebeapi
import socket

import jpype
jpype.startJVM(classpath=["C:/IdeaProjects/study/HelloPython/libs/h2-2.3.232.jar"])
print("JVM 시작 성공")
jpype.shutdownJVM()

print("hello, world!")

s = socket.socket()
try:
    s.connect(("localhost", 9092))
    print("9092 포트 연결 성공")
except Exception as e:
    print("9092 포트 연결 실패:", e)
s.close()

H2_JAR = "C:/IdeaProjects/study/HelloPython/libs/h2-2.3.232.jar"
try:
    conn = jaydebeapi.connect(
        "org.h2.Driver",
        #"jdbc:h2:tcp://localhost/~/test",
        "jdbc:h2:file:C:/tools/test",
        # "jdbc:h2:file:C:/tools/test",
        ["sa", ""],
        H2_JAR
    )

    # conn = jaydebeapi.connect(
    #     "org.h2.Driver",
    #     "jdbc:h2:~/test",
    #     ["sa", ""],
    #     H2_JAR,)

    print("H2 연결 성공 (tcp 모드)")

    cur = conn.cursor()
    cur.execute("SELECT 1")
    print(cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("연결 실패:", e)
