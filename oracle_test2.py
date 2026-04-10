import oracledb


# 데이터베이스 접속 정보 설정
dsn = oracledb.makedsn("localhost", 1522, service_name="XE")
conn = oracledb.connect(user="c##mbc", password="qwer1234", dsn=dsn)

# 쿼리 실행을 위한 커서 생성
cursor = conn.cursor()
employee = []
class Person:
    def __init__(self, empno, ename, job, mgr, hiredate, sal, comm, deptno):
        self.empno = empno
        self.ename = ename
        self.job = job
        self.mgr = mgr
        self.hiredate = hiredate
        self.sal = sal
        self.comm = comm
        self.deptno = deptno
    
    def info_emp(self):
        print(f"{self.empno}, {self.ename}, {self.job}, {self.mgr}, {self.hiredate}, {self.sal}, {self.comm}, {self.deptno}")



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
    if empno.isdigit():
        try:
            cursor.execute("INSERT INTO emp(empno, ename) VALUES (:1, :2)", [empno, ename.upper()])
            conn.commit()
            print("Welcome")
        except oracledb.DatabaseError as e:
            print(f"Error inserting data: {e}")
    else:
        print('CHA 0001 : 입력 오류입니다. 사번+이름을 입력해주세요')
def delete_emp():  
    print('이름을 입력하시오')  
    ename = input()
    try:
        cursor.execute("DELETE FROM emp WHERE ename = :1", [ename.upper()])
        conn.commit()
        print("Bye bye~")
    except oracledb.DatabaseError as e:
        print(f"Error deleting data: {e}")
def select_emp():
    try:
        cursor.execute('''
        SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, DEPTNO
        FROM emp
        ORDER BY EMPNO''')  
        for row in cursor:
            p = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            employee.append(p)
        for i in employee:
            i.info_emp()
    except oracledb.DatabaseError as e:
        print(f"Error fetching data: {e}")

while True:
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
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못된 입력입니다.')



# 커서 및 커넥션 닫기
cursor.close()
conn.close()
