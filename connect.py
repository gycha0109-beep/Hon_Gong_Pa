import oracledb


class Connect:
    def __init__(self):
        dsn = oracledb.makedsn("localhost", 1522, service_name="XE")
        self.conn = oracledb.connect(
            user="c##mbc",
            password="qwer1234",
            dsn=dsn,
        )
        self.cursor = self.conn.cursor()
