import ibm_db
import subprocess
import datetime
import requests

# 1. 인포믹스 DB에서 영업일 여부 확인
def is_business_day():
    today = datetime.datetime.now().strftime("%Y%m%d")

    conn_str = (
        "DATABASE=mydb;"
        "HOSTNAME=192.168.0.10;"
        "PORT=9088;"
        "PROTOCOL=onsoctcp;"
        "UID=dbuser;"
        "PWD=dbpass;"
    )
    conn = ibm_db.connect(conn_str, "", "")
    print("Connected!")
    cur = conn.cursor()

    sql = "SELECT holi_date FROM pgcal01 WHERE trd_date = ? "
    cur.execute(sql, (today,))
    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        return False  # 데이터 없으면 비영업일로 처리

    return row[0] == 1


# 2. 외부 프로그램 실행
def run_pg_bat_purc():
    today = datetime.datetime.now().strftime("%Y%m%d")
    cmd = ["pg_bat_purc", today, "옵션값"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


# 3. 실패 시 문자 발송
def send_sms(message):
    url = "https://sms-api.example.com/send"
    data = {
        "to": "01012345678",
        "msg": message
    }
    requests.post(url, data=data)


# 메인 로직
def main():
    if not is_business_day():
        print("오늘은 비영업일. 프로그램 종료.")
        return

    code, out, err = run_pg_bat_purc()

    if code != 0:
        msg = f"[경고] pg_bat_purc 실행 실패\n에러: {err}"
        send_sms(msg)
        print("실패 문자 발송 완료.")
    else:
        print("pg_bat_purc 실행 성공.")


if __name__ == "__main__":
    main()