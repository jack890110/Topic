import pymssql
import pyodbc
#對資料庫進行寫入及編輯的副程式
def query(sql):
    try:
        # SQL Server電腦位置及帳號密碼等
        # conn = pymssql.connect(host='localhost', server="DESKTOP-URU9MLH\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
        # conn = pyodbc.connect(host='localhost', server="DESKTOP-URU9MLH\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')

        server = 'DESKTOP-URU9MLH\SQLEXPRESS'
        database = 'Topic_DB'
        username = 'Timmy'
        password = 'qazwsx!1'
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


        
        #下2行為對資料庫進行操作
        cur = conn.cursor()
        cursor = conn.cursor()
        
        cursor.execute(sql)
       
       #下2行為對資料庫操作完成，關閉資料庫
        conn.commit()
        conn.close()
        return True
    except ValueError as e:
        print(e)
        return False

#對資料庫進行讀取(並顯示出資料)的副程式
def select(sql):
    try:
        # conn = pymssql.connect(host='localhost', server="DESKTOP-URU9MLH\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
        # conn = pyodbc.connect(host='localhost', server="DESKTOP-URU9MLH\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
     
        server = 'DESKTOP-URU9MLH\SQLEXPRESS'
        database = 'Topic_DB'
        username = 'Timmy'
        password = 'qazwsx!1'
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

        cur = conn.cursor()
        cursor = conn.cursor()
        
        cursor.execute(sql)
        
        #對資料庫進行讀取操作
        result = cursor.fetchall()

        #下2行為對資料庫操作完成，關閉資料庫
        conn.commit()
        conn.close()
        return result
    except:
        return False