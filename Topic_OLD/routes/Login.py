''' Python宣告使用的套件方式，不可刪除 '''
from flask import Blueprint
from flask import  render_template ,request

''' 此為基本語法不可刪除 '''
login_api = Blueprint('login_api', __name__)
register_api = Blueprint('register_api', __name__)

@login_api.route("/")
def login():
    return render_template("/member_center/member_center.html")

# @register_api.route("/member_center/register")
# def register():
#     return render_template("/member_center/login/register.html")