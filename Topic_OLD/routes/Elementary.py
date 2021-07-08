''' Python宣告使用的套件方式，不可刪除 '''
from flask import Blueprint
from flask import  render_template

''' 此為基本語法不可刪除 '''
elementary_api = Blueprint('elementary_api', __name__)

@elementary_api.route("/")
def elementary():
    return render_template("/elementary/elementary.html")