#Python宣告使用的套件為Flask及匯入其他Python檔案方式，不可刪除
from flask import Flask, render_template , request , make_response, jsonify
#匯入MS SQL套件
import pymssql

#form routes.XXX為多連結串接檔案，main.py此檔案為導引到小連結
#Login導引到登入/註冊的網站
from routes.Login import login_api
#Elementary導引到國小網站
from routes.Elementary import elementary_api
#Intermediate導引到國中網站
from routes.Intermediate import intermediate_api
#Highlevel導引到高中網站
from routes.Highlevel import highlevel_api

# from routes.Header import header_api


# 此為基本語法不可刪除
app = Flask(__name__)
# app.register_blueprint(XXX_api, url_prefix='/XXX')  此語法為嵌入其他Python檔案，XXX為上面import XXX_api取的名稱，url_prefix為網址列下一層顯示名稱
app.register_blueprint(login_api, url_prefix='/login')
app.register_blueprint(elementary_api, url_prefix='/elementary')
app.register_blueprint(intermediate_api, url_prefix='/intermediate')
app.register_blueprint(highlevel_api, url_prefix='/highlevel')


#Python指定網頁資料夾內的html檔案，HTML那邊寫法要改為指定資料夾不是使用相對或絕對位置
#導引至首頁，點擊Logo導引，避免發生錯誤
@app.route("/main")
def home():
#下3行程式為判斷使用者是否已經登入，如果已經登入在main.html的此處{% if is_login %}顯示到{% else %}程式碼內容，沒有登入的話則顯示{% else %}到{% endif %}的程式碼內容
    is_login = False
    if "is_login" in request.cookies and request.cookies['is_login'] == 'yes':
        is_login = True
    return render_template("main.html" ,is_login = is_login)

#導引至首頁
@app.route("/")
def home2():
#下3行程式為判斷使用者是否已經登入，如果已經登入在main.html的此處{% if is_login %}顯示到{% else %}程式碼內容，沒有登入的話則顯示{% else %}到{% endif %}的程式碼內容
    is_login = False
    if "is_login" in request.cookies and request.cookies['is_login'] == 'yes':
        is_login = True
    return render_template("main.html" ,is_login = is_login)


@app.route("/header")
def header():
    return render_template("header.html")

#登入系統試驗
@app.route("/loo" , methods=["POST"])
def loo():
    #連結後端的ID名稱為ID_number及password連動後端資料庫
    username = request.form['ID_number']
    password = request.form['password']
    #ID_numbe及password連動後端資料庫(尚未完成57~61行)
    if username == "a" and password == "a":
        response = make_response("yes")
        response.set_cookie("is_login", value="yes")
        return response
    else:
        return "no"


@app.route("/member_center/register")
def register():
    return render_template("/member_center/login/register.html")
    #註冊系統連結後端資料庫(尚未完成)

#下2行為基本語法不可刪除
if __name__ == "__main__":
    app.run(debug=True)