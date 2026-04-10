from person import Person
from connect import Connect

DB = Connect()
conn = DB.conn
cursor = DB.cursor

employee = []


def show_menu():
    print("-- 임직원 관리 시스템 --")
    print("|  1. 직 원 추 가  |")
    print("|  2. 직 원 삭 제  |")
    print("|  3. 직 원 조 회  |")
    print("|  4.사원 정보 수정 |")
    print("|  5. 프로그램 종료 |")
    return input("메뉴를 선택해주세요: ").strip()


def insert_emp():
    print("사번과 이름을 입력하시오")
    empno, ename = input().split()
    print(empno, ename)
    if empno.isdigit():
        try:
            cursor.execute(
                "INSERT INTO emp(empno, ename) VALUES (:1, :2)",
                [empno, ename.upper()],
            )
            conn.commit()
            print("Welcome")
        except Exception as e:
            print(f"Error inserting data: {e}")
    else:
        print("입력 오류입니다. 사번+이름을 입력해주세요")

def update_emp():
    empno = input("수정할 직원의 사번을 입력하시오: ").strip()
    cursor.execute(f"SELECT * FROM emp WHERE ename = :1", [empno])
    number = input('수정할 정보를 선택해주십시오.\n1. 직책  2. 사수  3. 연봉  4. 부서번호\n번호 입력: ').strip()
    if empno.isdigit():
        if number == "1":
            input('새 직책: ').strip()
            cursor.execute("UPDATE emp SET job where empno :1", [empno])
            conn.commit()
        elif number == "2":
            input('새 사수의 번호: ').strip()
            cursor.execute("UPDATE emp SET mgr where empno :1", [empno])
            conn.commit()
        elif number == "3":
            input('새 연봉: ').strip()
            cursor.execute("UPDATE emp SET sal where empno :1", [empno])
            conn.commit()
        elif number == "4":
            input('새 부서번호: ').strip()
            cursor.execute("UPDATE emp SET job where empno :1", [empno])
            conn.commit()
    else:
        print("잘못된 입력입니다.")
def delete_emp():
    ename = input("삭제할 이름을 입력하시오: ").strip().upper()
    try:
        cursor.execute("DELETE FROM emp WHERE ename = :1", [ename])
        conn.commit()
        print("Bye bye~")
    except Exception as e:
        print(f"Error deleting data: {e}")


def select_emp():
    try:
        employee.clear()
        cursor.execute(
            """
            SELECT EMPNO, ENAME, JOB, MGR,
                   TO_CHAR(HIREDATE, 'YYYY-MM-DD') AS HIREDATE,
                   ROUND(SAL), ROUND(COMM), DEPTNO
            FROM emp
            ORDER BY EMPNO
            """
        )
        for row in cursor:
            p = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            employee.append(p)

        for person in employee:
            person.info_emp()
        print('전체 사원 수 : ', len(employee))
    except Exception as e:
        print(f"Error fetching data: {e}")
    


while True:
    choice = show_menu()
    if choice == "1":
        print("1. 직원추가를 선택하셨습니다.")
        insert_emp()
    elif choice == "2":
        print("2. 직원삭제를 선택하셨습니다.")
        delete_emp()
    elif choice == "3":
        print("3. 직원조회를 선택하셨습니다.")
        select_emp()
    elif choice == "4":
        print("데이터를 수정합니다.")
        update_emp()
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")


cursor.close()
conn.close()
