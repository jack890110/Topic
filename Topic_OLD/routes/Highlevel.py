''' Python宣告使用的套件方式，不可刪除 '''
from flask import Blueprint
from flask import  render_template

''' 此為基本語法不可刪除 '''
highlevel_api = Blueprint('highlevel_api', __name__)

@highlevel_api.route("/")
def highlevel():
    return render_template("/member_center/member_center.html")