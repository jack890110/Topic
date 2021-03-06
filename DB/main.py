#Python宣告使用的套件方式，不可刪除
from flask import Flask, render_template , request , make_response, jsonify
import pyodbc

#導入db.py內的SQL基本語法副程式，減少程式碼重複
import db

# 此為Flask基本語法不可刪除
app = Flask(__name__)

# 註冊學生系統的SQL語法，已完成
@app.route("/register_student" , methods=["POST"])
def register_student():
    request_data = request.get_json()
    #以下為學生及老師共通性帳號及密碼，身分證重複會無法建立帳號
    email = request_data['email'] #email帳號
    password = request_data['password'] #使用者密碼
    #joinDate為註冊新帳號加入的時間，已於SQL方處理完成，此區不需寫入資料進去資料庫
    ID_number = request_data['ID_number'] #身分證字號(資料庫主鍵)
    change = request_data['change'] #寫入資料庫系統change等於0是學生，等於1是老師，等於3是業界人士
    name = request_data['name']
    phone = request_data['phone']
    school = request_data['school']
    #下3行資料為學生獨有
    studentnumber = request_data['studentnumber']
    department = request_data['department']
    grade = request_data['grade']
    
    change = int(change)
    
    
    #尋找是否有相同的身分證，如果有的話res陣列會產生內容，沒有則為[]，在下面的if判斷判斷是否有陣列內容，有陣列內容回報身分證已經註冊禁止註冊帳號
    sql = f"SELECT [ID_number] FROM [Topic_DB].[dbo].[Account_Number] WHERE id_number = '{ID_number}'"
    res = db.select(sql)
    
    #尋找是否有相同的電子郵件，如果有的話res2陣列會產生內容，沒有則為[]，在下面的if判斷判斷是否有陣列內容，有陣列內容回報身分證已經註冊禁止註冊帳號
    sql2 = f"SELECT [email] FROM [Topic_DB].[dbo].[Account_Number] WHERE email = '{email}'"
    res2 = db.select(sql2)

    #以下程式碼是註冊的使用者帳號相同
    #判斷如果res及res1內陣列內容為[]時，即可註冊，否則因身分證相同或其他問題無法註冊帳號
    if res == [] and res2 == []:
        # 註冊學生帳號
        #change從JSON回傳為字串，必須轉成int型態才能使用
        #進行註冊資料進入資料庫的語法
        sql = "INSERT INTO [Topic_DB].[dbo].[Account_Number] ([ID_number],[email],[password],[change]) VALUES ('{0}', '{1}', '{2}', '{3}');\
        INSERT INTO [Topic_DB].[dbo].[Student_DB] ([ID_number],[email],[studentnumber],[name],[phone],[school],[department],[grade]) VALUES ('{0}','{1}','{4}','{5}','{6}','{7}','{8}','{9}')".format(
        ID_number,
        email,
        password,
        change,

        studentnumber,
        name,
        phone,
        school,
        department,
        grade
        )
        
        #呼叫SQL副程式db.py檔案內的query副程式
        result = db.query(sql)

        if(not(result)):
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
            "data": '恭喜您的帳號建立成功~!'
        }
        print("恭喜您的帳號建立成功，您的身分證字號為",ID_number)
        return jsonify(return_obj)
    else:#帳號重複，傳回重複帳號 
        return_obj = {
            "status": 400,
            "data": '身分證字號或電子郵件已經重複，或發生其他問題，請更改其他名稱然後再試一次。'
        }
        print("帳號已經重複，或發生其他問題，請更改其他名稱然後再試一次。")
        return jsonify(return_obj)

# 註冊老師系統的SQL語法，已完成
@app.route("/register_teach" , methods=["POST"])
def register_teach():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    #joinDate為註冊新帳號加入的時間，已於SQL方處理完成，此區不需寫入資料進去資料庫
    ID_number = request_data['ID_number']
    change = request_data['change']
    name = request_data['name']
    phone = request_data['phone']
    school = request_data['school']
    #下1行資料為老師獨有
    expertise = request_data['expertise']

    change = int(change)

    sql = f"SELECT [ID_number] FROM [Topic_DB].[dbo].[Account_Number] WHERE id_number = '{ID_number}'"
    res = db.select(sql)

    sql2 = f"SELECT [email] FROM [Topic_DB].[dbo].[Account_Number] WHERE email = '{email}'"
    res2 = db.select(sql2)

    if res == [] and res2 == []:
        sql = "INSERT INTO [Topic_DB].[dbo].[Account_Number] ([ID_number],[email],[password],[change]) VALUES ('{0}', '{1}', '{2}', '{3}');\
        INSERT INTO [Topic_DB].[dbo].[Teach_DB] ([ID_number],[email],[name],[phone],[school],[expertise]) VALUES ('{0}','{1}','{4}','{5}','{6}','{7}')".format(
        ID_number,
        email,
        password,
        change,

        name,
        phone,
        school,
        expertise
        )
        
        result = db.query(sql)

        if(not(result)):
            return_obj = {
            "status": 400,
            "data": '請檢察其他資訊然後再試一次。'
            }
            print("請檢察其他資訊然後再試一次。")
            return jsonify(return_obj)
        return_obj = {
            "status": 200,
            "data": '恭喜您的帳號建立成功~!'
        }
        print("恭喜您的帳號建立成功，您的身分證字號為",ID_number)
        return jsonify(return_obj)
    else:
        return_obj = {
            "status": 400,
            "data": '身分證字號或電子郵件已經重複，或發生其他問題，請更改其他名稱然後再試一次。'
        }
        print("帳號已經重複，或發生其他問題，請更改其他名稱然後再試一次。")
        return jsonify(return_obj)

# 註冊業界人士系統的SQL語法，已完成
@app.route("/register_industry_participant" , methods=["POST"])
def register_industry_participant():
    request_data = request.get_json()
    email = request_data['email'] 
    password = request_data['password']
    #joinDate為註冊新帳號加入的時間，已於SQL方處理完成，此區不需寫入資料進去資料庫
    ID_number = request_data['ID_number'] 
    change = request_data['change'] 
    name = request_data['name']
    phone = request_data['phone']
    school = request_data['school']
    #下1行資料為業界人士獨有
    expertise = request_data['expertise']

    change = int(change)

    sql = f"SELECT [ID_number] FROM [Topic_DB].[dbo].[Account_Number] WHERE id_number = '{ID_number}'"
    res = db.select(sql)

    sql2 = f"SELECT [email] FROM [Topic_DB].[dbo].[Account_Number] WHERE email = '{email}'"
    res2 = db.select(sql2)

    if res == [] and res2 == []:
        sql = "INSERT INTO [Topic_DB].[dbo].[Account_Number] ([ID_number],[email],[password],[change]) VALUES ('{0}', '{1}', '{2}', '{3}');\
        INSERT INTO [Topic_DB].[dbo].[Industry_participant] ([ID_number],[email],[name],[phone],[expertise]) VALUES ('{0}','{1}','{4}','{5}','{6}')".format(
        ID_number,
        email,
        password,
        change,

        name,
        phone,
        expertise
        )
        
        result = db.query(sql)

        if(not(result)):
            return_obj = {
            "status": 400,
            "data": '請檢察其他資訊然後再試一次。'
            }
            print("請檢察其他資訊然後再試一次。")
            return jsonify(return_obj)
    
        return_obj = {
            "status": 200,
            "data": '恭喜您的帳號建立成功~!'
        }
        print("恭喜您的帳號建立成功，您的身分證字號為",ID_number)
        return jsonify(return_obj)
    else:
        return_obj = {
            "status": 400,
            "data": '身分證字號或電子郵件已經重複，或發生其他問題，請更改其他名稱然後再試一次。'
        }
        print("帳號已經重複，或發生其他問題，請更改其他名稱然後再試一次。")
        return jsonify(return_obj)


#登入系統的SQL語法，已全部完成
@app.route("/login" , methods=["POST"])
def login():
    request_data = request.get_json()
    input_id = request_data['input_id'] #身分證字號，或email
    password = request_data['password'] #使用者密碼
    
    
    #查詢帳號電子郵件或身分證，傳回res
    #先判斷使用者輸入資料為身分證字號或是電子郵件，如果是電子郵件字串內容會有@則判斷email，否則判斷身分證字號
    if '@' in input_id:
        sql = f"SELECT [email] FROM [Topic_DB].[dbo].[Account_Number] WHERE email = '{input_id}'"
        res = db.select(sql)
    else:
        sql = f"SELECT [ID_number] FROM [Topic_DB].[dbo].[Account_Number] WHERE ID_number = '{input_id}'"
        res = db.select(sql)
    

    #判斷如果res陣列的長度為0時，無此帳號，請使用者建立新的帳號
    if len(res) == 0:
        #下面5行為SQL回傳至JSON API的值
        return_obj = {
            "status": 400,
            "data": '查無此帳號，請確定輸入的身分證字號或電子郵件是否正確'
            }
        print("查無此帳號，請確定輸入的身分證字號或電子郵件是否正確")
        return jsonify(return_obj)
    else:
        #尋找是否有相同的密碼，如果有的話res陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，
        #查詢密碼，傳回res
        sql = f"SELECT [password] FROM [Topic_DB].[dbo].[Account_Number] WHERE password = '{password}'"
        res = db.select(sql)

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
            print("登入成功")
            return jsonify(return_obj)








#下2行為基本語法不可刪除
if __name__ == "__main__":
    app.run(debug=True)







#舊程式碼

# 單純的註冊系統的SQL語法，已經全部完成
# @app.route("/register" , methods=["POST"])
# def register():
#     request_data = request.get_json()
#     #以下為學生及老師共通性帳號及密碼，身分證重複會無法建立帳號
#     email = request_data['email'] #email帳號
#     password = request_data['password'] #使用者密碼
#     #joinDate為註冊新帳號加入的時間，已於SQL方處理完成，此區不需寫入資料進去資料庫
#     ID_number = request_data['ID_number'] #身分證字號(資料庫主鍵)
#     change = request_data['change'] #寫入資料庫系統change等於0是學生，等於1是老師，等於3是業界人士
#     name = request_data['name']
#     phone = request_data['phone']
#     #下1行資料為老師獨有
#     # expertise = request_data['expertise']
#     #下2行資料為學生獨有
#     department = request_data['department']
#     grade = ['grade']
    
#     change = int(change)
    
#     #尋找是否有相同的身分證，如果有的話res陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，有陣列內容回報身分證已經註冊禁止註冊帳號
#     sql = f"SELECT [ID_number] FROM [Topic_DB].[dbo].[Account_Number] WHERE id_number = '{ID_number}'"
#     res = db.select(sql)

#     #以下程式碼是註冊的使用者帳號相同
#     #判斷如果res內陣列的長度為0時，即可註冊，否則因身分證相同或其他問題無法註冊帳號
#     if res == []:
#         #change從JSON回傳為字串，必須轉成int型態才能使用
#         #進行註冊資料進入資料庫的語法
#         sql = "INSERT INTO [Topic_DB].[dbo].[Account_Number] ([change],[email],[password],[ID_number]) VALUES ('{0}', '{1}', '{2}', '{3}')".format(
#         change,
#         email,
#         password,
#         ID_number
#         )
#         #呼叫SQL副程式db.py檔案內的query副程式
#         result = db.query(sql)
#         if(not(result)):
#             return_obj = {
#             "status": 400,
#             "data": '請檢察其他資訊然後再試一次。'
#             #下一行為JSON格式範例"key:":{"key":'value' , "key2": 'value'}
#             #"data3": {"data2":'帳號建立成功~!'}
#             }
#             print("請檢察其他資訊然後再試一次。")
#             return jsonify(return_obj)
    
#         #下面5行為SQL回傳至JSON API的值
#         return_obj = {
#             "status": 200,
#             "data": '恭喜您的帳號建立成功~!'
#         }
#         print("恭喜您的帳號建立成功，您的身分證為",ID_number)
#         return jsonify(return_obj)
#     else:#帳號重複，傳回重複帳號 
#         return_obj = {
#             "status": 400,
#             "data": '身分證字號已經重複，或發生其他問題，請更改其他名稱然後再試一次。'
#         }
#         print("帳號已經重複，或發生其他問題，請更改其他名稱然後再試一次。\n重複的身分證為",ID_number)
#         return jsonify(return_obj)

# 註冊一個帳號的SQL語法(已全部完成)
# @app.route("/register" , methods=["POST"])
# def register():
#     request_data = request.get_json()
#     #以下為學生及老師共通性帳號及密碼，身分證重複會無法建立帳號
#     email = request_data['email'] #email帳號
#     password = request_data['password'] #使用者密碼
#     name = request_data['name'] #姓名
#     #joinDate為註冊新帳號加入的時間，已於SQL方處理完成，此區不需寫入資料進去資料庫
#     phone = request_data['phone'] #電話號碼
#     ID_number = request_data['ID_number'] #身分證字號
#     change = request_data['change'] #寫入資料庫系統change等於0是學生，等於1是老師

#     #以下為學生的資料寫入資料表的程式
#     school = request_data['school'] #學校名稱
#     department = request_data['department'] #科系名稱
#     grade = request_data['grade'] #年級
#     studentnumber = request_data['studentnumber'] #學生學號

#     #以下為老師的資料寫入資料表的程式
#     expertise = request_data['expertise'] #老師的專長


#     #尋找是否有相同的電子郵件，如果有的話res陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，有陣列內容回報電子郵件已經註冊禁止註冊帳號，先判斷change內的0為學生，否則為老師
#     if int(change) == 0:
#         sql = f"SELECT [email] FROM [Topic_DB].[dbo].[Student_DB] WHERE email = '{email}'"
#         res = db.select(sql)
#     else:
#         sql = f"SELECT [email] FROM [Topic_DB].[dbo].[Teach_DB] WHERE email = '{email}'"
#         res = db.select(sql)

#     #以下程式碼是註冊的使用者帳號相同
#     #判斷如果res內陣列的長度為0時，即可註冊，否則因電子郵件相同或其他問題無法註冊帳號
#     if len(res) == 0:
#         #如果change是0為註冊學生資料，否則為註冊老師資料，另外change從JSON回傳為字串，必須轉成int型態才能使用
#         if int(change) == 0:
#             print("測試學生")
#             #進行註冊學生資料進入資料庫的語法
#             sql = "INSERT INTO [Topic_DB].[dbo].[Student_DB] ([change],[email],[password],[name],[phone],[ID_number],[school],[department],[grade],[studentnumber]) VALUES ('{0}', '{1}', '{2}', '{3}','{4}','{5}','{6}','{7}','{8}','{9}')".format(
#             change,
#             email,
#             password,
#             name,
#             phone,
#             ID_number,
#             school,
#             department,
#             grade,
#             studentnumber
#             )
#             #呼叫SQL副程式db.py檔案內的query副程式
#             result = db.query(sql)
            
#             if(not(result)):
#                 print("123123123")
#                 return_obj = {
#                 "status": 400,
#                 "data": '請檢察其他資訊然後再試一次。'
#                 #下一行為JSON格式範例"key:":{"key":'value' , "key2": 'value'}
#                 #"data3": {"data2":'帳號建立成功~!'}
#                 }
#                 print("請檢察其他資訊然後再試一次。")
#                 return jsonify(return_obj)
        
#             #下面5行為SQL回傳至JSON API的值
#             return_obj = {
#                 "status": 200,
#                 "data": '恭喜學生您的帳號建立成功~!'
#             }
#             print("恭喜學生您的帳號建立成功，您的電子郵件地址為",email)
#             return jsonify(return_obj)
#         else:
#             #進行註冊老師資料進入資料庫的語法
#             print("測試老師")
#             sql = "INSERT INTO [Topic_DB].[dbo].[Teach_DB] ([change],[email],[password],[name],[phone],[ID_number],[expertise]) VALUES ('{0}', '{1}', '{2}', '{3}','{4}','{5}','{6}')".format(
#             change,
#             email,
#             password,
#             name,
#             phone,
#             ID_number,
#             expertise
#             )
#             #呼叫SQL副程式db.py檔案內的query副程式
#             result = db.query(sql)
#             if(not(result)):
#                 print("失敗")
#                 return_obj = {
#                 "status": 400,
#                 "data": '請檢察其他資訊然後再試一次。'
#                 #下一行為JSON格式範例"key:":{"key":'value' , "key2": 'value'}
#                 #"data3": {"data2":'帳號建立成功~!'}
#                 }
#                 print("請檢察其他資訊然後再試一次。")
#                 return jsonify(return_obj)
        
#             #下面5行為SQL回傳至JSON API的值
#             return_obj = {
#                 "status": 200,
#                 "data": '恭喜老師您的帳號建立成功~!'
#             }
#             print("恭喜老師您的帳號建立成功，您的電子郵件地址為",email)
#             return jsonify(return_obj)
#     else:#帳號重複，傳回重複帳號 
#         return_obj = {
#             "status": 400,
#             "data": '電子郵件或身分證字號已經重複，或發生其他問題，請更改其他名稱然後再試一次。'
#         }
#         print("帳號已經重複，或發生其他問題，請更改其他名稱然後再試一次。\n重複的電子郵件或身分證為",email,ID_number)
#         return jsonify(return_obj)

#登入系統的SQL語法，已全部完成
# @app.route("/login" , methods=["POST"])
# def login():
#     request_data = request.get_json()
#     email = request_data['email'] #email帳號
#     password = request_data['password'] #使用者密碼
    
#     #查詢學生帳號電子郵件，傳回res
#     sql = f"SELECT [email] FROM [Topic_DB].[dbo].[Student_DB] WHERE email = '{email}'"
#     res = db.select(sql)

#     #查詢老師帳號電子郵件，傳回res1
#     sql1 = f"SELECT [email] FROM [Topic_DB].[dbo].[Teach_DB] WHERE email = '{email}'"
#     res1 = db.select(sql1)

#     #判斷如果res或res1內陣列的長度為0時，無此帳號，請使用者建立新的帳號
#     print(res ,"學生")
#     print(res1,"老師")

#     if (len(res) == 0) and (len(res1) == 0):
#         #下面5行為SQL回傳至JSON API的值
#         return_obj = {
#             "status": 400,
#             "data": '查無此帳號，請確定輸入的Email是否正確'
#             }
#         print("查無此帳號，請確定輸入的Email是否正確，你輸入的Email是",email)
#         return jsonify(return_obj)
#     else:
#         #尋找是否有相同的密碼，如果有的話res(學生)或res1(老師)陣列會產生內容，沒有則為0，在下面的if判斷判斷是否有陣列內容，
#         #查詢學生帳號密碼，傳回res
#         sql = f"SELECT [password] FROM [Topic_DB].[dbo].[Student_DB] WHERE password = '{password}'"
#         res = db.select(sql)

#         #查詢老師帳號密碼，傳回res1
#         sql1 = f"SELECT [password] FROM [Topic_DB].[dbo].[Teach_DB] WHERE password = '{password}'"
#         res1 = db.select(sql1)
#         #判斷如果res內陣列的長度為0時，密碼錯誤，請使用者確認輸入密碼是否正確
#         if (len(res) == 0) and (len(res1) == 0):
#             return_obj = {
#                 "status": 400,
#                 "data": '密碼錯誤，請確定輸入的密碼是否正確'
#             }
#             print("密碼錯誤，您輸入的密碼為",password)
#             return jsonify(return_obj)
#         else:
#             return_obj = {
#                 "status": 200,
#                 "data": '登入成功'
#             }
#             print("登入成功，您的電子郵件地址為",email)
#             return jsonify(return_obj)