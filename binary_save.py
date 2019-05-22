"""
二进制存储
增删改
"""
import pymysql

#创建连接
db =pymysql.connect(host = 'localhost',
                    user = 'root',
                    passwd = '123456',
                    database = 'stu',
                    charset = 'utf8')
# 创建游标
cur = db.cursor()

#存储文件
with open('bitree.jpg','rb') as fd:
    data = fd.read()
# try:
#     sql = "insert into Images values (1,'Bitree.jpg',%s);"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

#获取文件
sql  = "select * from Images where filename = 'Bitree.jpg'"
cur.execute(sql)
image = cur.fetchone()
with open(image[1],'wb') as fd:
    fd.write(image[2])

cur.close()
db.close()

