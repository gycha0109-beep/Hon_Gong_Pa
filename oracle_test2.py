import oracledb


# 데이터베이스 접속 정보 설정
dsn = oracledb.makedsn("localhost", 1522, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="qwer1234", dsn=dsn)

# 쿼리 실행을 위한 커서 생성
cursor = conn.cursor()

def show_menu():
    print('-- 임직원 관리 시스템 --')
    print('|  1. 직 원 추 가  |')
    print('|  2. 직 원 삭 제  |')
    print('|  3. 직 원 조 회  |')
    print('| 4. 프로그램 종료  |')
    order = input("메뉴를 선택해주세요.")
    return order
def insert_emp(): 
    print('사번과 이름을 입력하시오')
    empno, ename = input().split()
    print(empno, ename)
    try:
        cursor.execute("INSERT INTO emp(empno, ename) VALUES (:1, :2)", [empno, ename.upper()])
        conn.commit()
        print("Data inserted successfully")
    except oracledb.DatabaseError as e:
        print(f"Error inserting data: {e}")
def delete_emp():    
    ename = input()
    try:
        cursor.execute("DELETE FROM emp WHERE ename = :1", [ename.upper()])
        conn.commit()
        print("Bye bye~")
    except oracledb.DatabaseError as e:
        print(f"Error deleting data: {e}")
def select_emp():
    print('이름을 입력하시오')
    ename = input()
    try:
        cursor.execute("SELECT * FROM emp where ename = :1", [ename.upper()])
        for row in cursor:
            print(row)
    except oracledb.DatabaseError as e:
        print(f"Error fetching data: {e}")

loop = True

while loop:
    choice = int(show_menu())
    if choice == 1:
        print('1. 직원추가를 선택하셨습니다.')
        insert_emp()
    elif choice == 2:
        print('2. 직원삭제를 선택하셨습니다.')
        delete_emp()
    elif choice == 3:
        print('3. 직원조회를 선택하셨습니다.')
        select_emp()
    elif choice == 4:
        print('기타')
        loop = False




# 커서 및 커넥션 닫기
cursor.close()
conn.close()
