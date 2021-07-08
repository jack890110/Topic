import pyodbc
# pymssql

# # conn = pymssql.connect(host='localhost', server="DESKTOP-URU9MLH\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
# conn = pyodbc.connect(host='localhost', server="DESKTOP-URU9MLH\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
# # conn = pymssql.connect(host='localhost', server="DESKTOP-URU9MLH\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='abcd')

server = 'DESKTOP-URU9MLH\SQLEXPRESS' 
database = 'Topic_DB' 
username = 'Timmy' 
password = 'qazwsx!1' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute(
    "INSERT INTO [Account_Number] ([email],[ID_number]) VALUES ('{0}', '{1}')".format(
        'roo314t',
        'rootffw',
    )
)

row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

os.exit()
cur = conn.cursor()
cursor = conn.cursor()


# 下2行資料表欄位名稱顯示
# field_name = [des[0] for des in cursor.description]
# print(field_name)

# 下4行為資料表資料內容顯示
# row = cursor.fetchone()
# while row:
#     print(str(row[0]) + ", " + str(row[1]) + ", " + str(row[2]) + ", " + str(row[3]) + ", " + str(row[4]) + ", " + str(row[5]))
#     row = cursor.fetchone()

#123456

# 下8行為新建、插入1筆資料範例
# cursor.execute(
#     "INSERT INTO [Topic_DB] ([username], [password], [address], [name]) VALUES ('{0}', '{1}', '{2}', '{3}')".format(
#         'roo314t',
#         'rootffw',
#         'Taichung@adad.ciom',
#         'Jack1616'
#     )
# )

# 下2行為搜尋Topic_DB資料表中尋找ID為4的資料範例
cursor.execute("SELECT * From [Topic_DB].[dbo].[Account_Number]")
a = cursor.fetchall()
print(a)
# print("\n\n")

# print(a[4])



# 下1行為指定ID為6的更改username，更新1筆資料內容，範例
# cursor.execute("""UPDATE Topic_DB SET username='114691691644' WHERE id='6'""")

# 下1行為刪除Topic_DB資料表中尋找ID為1的資料範例
# cursor.execute("""DELETE FROM Topic_DB WHERE id = 1;""")

# 如果沒有指定autocommit屬性為True的話就需要呼叫commit()方法

#下1行為使用外部變數時代入SQL語法查詢資料方法
# username = "469419193"
# sql = "SELECT [username] FROM [Topic_DB].[dbo].[Student_DB] WHERE convert(nvarchar(255),username) = (%s)"
# # cursor.execute(sql, "469419193")
# cursor.execute(sql, (username))
# a = cursor.fetchall()
# print(a)

conn.commit()
conn.close()