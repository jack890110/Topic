#Python宣告使用的套件方式，不可刪除
from flask import Flask, render_template , request , make_response, jsonify
import pymssql

#導入db.py內的SQL基本語法副程式，減少程式碼重複
import db
   
# 此為Flask基本語法不可刪除
app = Flask(__name__)

# 註冊一個"學生"帳號的SQL語法
@app.route("/register_student" , methods=["POST"])
def register():
    request_data = request.get_json()
    email = request_data['email'] #email帳號
    password = request_data['password'] #使用者密碼
    name = request_data['name'] #姓名
    #joinDate為註冊新帳號加入的時間，已於SQL方處理完成，此區不需寫入資料進去資料庫
    school = request_data['school'] #學校名稱
    department = request_data['department'] #科系名稱
    grade = request_data['grade'] #年級
    studentnumber = request_data['studentnumber'] #學生學號
    phone = request_data['phone'] #電話號碼
    id = 0 #寫入資料庫系統ID等於0是學生，等於1是老師
    
    #目前下列程式碼測試有問題的部分(猜測是副程式問題)
    # select = "SELECT [username] FROM [Topic_DB].[dbo].[Student_DB] WHERE convert(nvarchar(255),username) = (%s)"
    # sql = select, (username)
    # result = db.select(sql)

    # if(not(result)):
    #     return_obj = {
    #         'status': 400,
    #         'data': {}
    #     }
    #     return jsonify(return_obj)
    
    # #下面5行為SQL回傳至JSON API的值
    # return_obj = {
    #     'status': 200,
    #     'data': {}
    # }
    # return jsonify(return_obj)

    
    #以下程式碼是註冊的使用者帳號相同 測試完成可以的
    conn = pymssql.connect(host='localhost', server="DESKTOP-U1V0R4A\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
    cur = conn.cursor()
    cursor = conn.cursor()
    #尋找是否有相同的電子郵件，如果有的話res陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，有陣列內容回報電子郵件已經註冊禁止註冊帳號
    select = "SELECT [email] FROM [Topic_DB].[dbo].[Student_DB] WHERE convert(nvarchar(255),email) = (%s)"
    cursor.execute(select, (email))
    res = cursor.fetchall()
    #判斷如果res內陣列的長度為0時，即可註冊，否則因電子郵件相同或其他問題無法註冊帳號
    if len(res) == 0:
        #進行註冊資料進入資料庫的語法
        sql = "INSERT INTO [Topic_DB].[dbo].[Student_DB] ([email],[password],[name],[school],[department],[grade],[studentnumber],[phone],[id] VALUES ('{0}', '{1}', '{2}', '{3}','{4}','{5}','{6}','{7}','{8}')".format(
        email,
        password,
        name,
        school,
        department,
        grade,
        studentnumber,
        phone,
        id
        )
        #呼叫SQL副程式db.py檔案內的query副程式
        result = db.query(sql)
        
        if(not(result)):
            print("123")
            return_obj = {
            "status": 400,
            "data": '請檢察其他資訊然後再試一次。'
            #下一行為JSON格式範例"key:":{"key":'value' , "key2": 'value'}
            #"data3": {"data2":'帳號建立成功~!'}
            }
            print("請檢察其他資訊然後再試一次。")
            return jsonify(return_obj)
    
        #下面5行為SQL回傳至JSON API的值
        return_obj = {
            "status": 200,
            "data": '帳號建立成功~!'
            }
        print("帳號建立成功，您的電子郵件地址為",email)
        return jsonify(return_obj)
        
    else:
        return_obj = {
            "status": 400,
            "data": '帳號已經重複，或發生其他問題，請更改其他名稱然後再試一次。'
        }
        print("帳號已經重複，或發生其他問題，請更改其他名稱然後再試一次。\n重複的帳號為",email)
        return jsonify(return_obj)
    
     
    
    # #註冊的程式碼
    # sql = "INSERT INTO [Topic_DB].[dbo].[Student_DB] ([username], [password], [email], [name]) VALUES ('{0}', '{1}', '{2}', '{3}')".format(
    #     username,
    #     password,
    #     email,
    #     name,
    # )
    # #呼叫SQL副程式db.py檔案內的query副程式
    # result = db.query(sql)
    # if(not(result)):
    #     return_obj = {
    #         'status': 400,
    #         'data': {}
    #     }
    #     return jsonify(return_obj)
    
    # #下面5行為SQL回傳至JSON API的值
    # return_obj = {
    #     'status': 200,
    #     'data': {}
    # }
    # return jsonify(return_obj)

#學生登入系統的SQL語法
@app.route("/login_student" , methods=["POST"])
def login():
    request_data = request.get_json()
    email = request_data['email'] #email帳號
    password = request_data['password'] #使用者密碼
    
    #以下程式碼是註冊的使用者帳號相同 測試完成可以的
    conn = pymssql.connect(host='localhost', server="DESKTOP-U1V0R4A\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
    cur = conn.cursor()
    cursor = conn.cursor()
    #尋找是否有相同的電子郵件，如果有的話res陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，有陣列內容回報電子郵件已經註冊禁止註冊帳號
    select = "SELECT [email] FROM [Topic_DB].[dbo].[Student_DB] WHERE convert(nvarchar(255),email) = (%s)"
    cursor.execute(select, (email))
    res = cursor.fetchall()
    #判斷如果res內陣列的長度為0時，無此帳號，請使用者建立新的帳號
    if len(res) == 0:
        #下面5行為SQL回傳至JSON API的值
        return_obj = {
            "status": 400,
            "data": '查無此帳號，請確定輸入的Email是否正確'
            }
        print("查無此帳號，請確定輸入的Email是否正確，你輸入的Email是",email)
        return jsonify(return_obj)
    else:
        #以下程式碼是註冊的使用者帳號相同 測試完成可以的
        conn = pymssql.connect(host='localhost', server="DESKTOP-U1V0R4A\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
        cur = conn.cursor()
        cursor = conn.cursor()
        #尋找是否有相同的密碼，如果有的話res陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，
        select = "SELECT [password] FROM [Topic_DB].[dbo].[Student_DB] WHERE convert(nvarchar(255),password) = (%s)"
        cursor.execute(select, (password))
        res = cursor.fetchall()
        #判斷如果res內陣列的長度為0時，密碼錯誤，請使用者確認輸入密碼是否正確
        if len(res) == 0:
            return_obj = {
                "status": 400,
                "data": '密碼錯誤，請確定輸入的密碼是否正確'
            }
            print("密碼錯誤，您輸入的密碼為",password)
            return jsonify(return_obj)
        else:
            return_obj = {
                "status": 200,
                "data": '登入成功'
            }
            print("登入成功，您的電子郵件地址為",email)
            return jsonify(return_obj)


@app.route("/data" , methods=["POST"])
def data():
    #以下程式碼是註冊的使用者帳號相同 測試完成可以的
    conn = pymssql.connect(host='localhost', server="DESKTOP-U1V0R4A\SQLEXPRESS",port='1433', user='Timmy', password='qazwsx!1', database='Topic_DB')
    cur = conn.cursor()
    cursor = conn.cursor()
    #尋找是否有相同的電子郵件，如果有的話res陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，有陣列內容回報電子郵件已經註冊禁止註冊帳號
    select = "SELECT [email] FROM [Topic_DB].[dbo].[Student_DB] WHERE convert(nvarchar(255),email) = (%s)"
    cursor.execute(select, (email))
    res = cursor.fetchall()

#下2行為基本語法不可刪除
if __name__ == "__main__":
    app.run(debug=True)