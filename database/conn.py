import pymysql
from datetime import datetime

conn = pymysql.connect(host='127.0.0.1', user='root', password='seokmin68', db='stock')
curs = conn.cursor()

delete_sql = "DROP TABLE nasdaq_stock"

curs.execute(delete_sql)
conn.commit()
print(f'{datetime.now()} - DELETE PREVIOUS TABLE')

create_sql = "CREATE TABLE nasdaq_stock (number INT NOT NULL AUTO_INCREMENT, symbol VARCHAR(200) NOT NULL, now_price VARCHAR(200) NOT NULL, target_price VARCHAR(200) NOT NULL, profit VARCHAR(200) NOT NULL, pre_price VARCHAR(200) NOT NULL, predict VARCHAR(200) NOT NULL, PRIMARY KEY(number));"
curs.execute(create_sql)
conn.commit()
print(f'{datetime.now()} - CREATE NEW TABLE')

insert_sql = "INSERT INTO nasdaq_stock (symbol, now_price, target_price, profit, pre_price, predict) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("MRIN", "$21", "$30", "+30%", "Pre. $25", "It will be decreased")

curs.execute(insert_sql, val)

conn.commit()

print(curs.rowcount, "record inserted")
