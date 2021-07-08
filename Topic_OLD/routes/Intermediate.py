''' Python宣告使用的套件方式，不可刪除 '''
from flask import Blueprint
from flask import  render_template

''' 此為基本語法不可刪除 '''
intermediate_api = Blueprint('intermediate_api', __name__)

@intermediate_api.route("/")
def intermediate():
    return render_template("/intermediate/intermediate.html")