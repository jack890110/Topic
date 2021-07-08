import pymssql
#對資料庫進行寫入及編輯的副程式
def query(sql):
    try:
        # SQL Server電腦位置及帳號密碼等
        conn = pymssql.connect(host='localhost', server="DESKTOP-U1V0R4A\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
        #下2行為對資料庫進行操作
        cur = conn.cursor()
        cursor = conn.cursor()
        
        cursor.execute(sql)
       
       #下2行為對資料庫操作完成，關閉資料庫
        conn.commit()
        conn.close()
        return True
    except: 
        return False

#對資料庫進行讀取的副程式
def select(sql):
    try:
        conn = pymssql.connect(host='localhost', server="DESKTOP-U1V0R4A\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
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
        # return result
        return False

#對資料庫進行讀取的副程式測試
# def select(select,username):
#     try:
#         conn = pymssql.connect(host='localhost', server="DESKTOP-U1V0R4A\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
#         cur = conn.cursor()
#         cursor = conn.cursor()
        
#         cursor.execute(select , (username))
        
#         #對資料庫進行讀取操作
#         result = cursor.fetchall()

#         #下2行為對資料庫操作完成，關閉資料庫
#         conn.commit()
#         conn.close()
#         return result
#     except: 
#         # return result
#         return False