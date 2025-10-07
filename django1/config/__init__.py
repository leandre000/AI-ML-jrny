import pymysql

# Ensure PyMySQL acts as MySQLdb for Django's MySQL backend
pymysql.install_as_MySQLdb()
