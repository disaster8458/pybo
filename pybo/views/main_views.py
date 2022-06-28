from flask import Blueprint, render_template, redirect, url_for
import testdb as td
from pybo.models import Question
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():

    return redirect(url_for('question.questionList'))

@bp.route('/hello')
def hello_pybo() :
    return 'hello, pybo'

@bp.route('/dbtest')
def dbtest() :
    td.getall_question()
    return '성공'

