from flask import Blueprint
import pybo.naverApi as nA
from flask import request

bp = Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/blog')
def blog():
    key = request.args.get('keyword')
    result = nA.naver_blog(key)

    return {'result' : result}