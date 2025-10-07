import pymysql

DB_NAME = "aimljrny"

conn = pymysql.connect(host="127.0.0.1", user="root", password="", port=3306, autocommit=True)
try:
    with conn.cursor() as cur:
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
        )
        print(f"Database '{DB_NAME}' is ready.")
finally:
    conn.close()
