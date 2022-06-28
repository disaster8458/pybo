from pybo.models import Question, Answer
from datetime import datetime
from pybo import db

def test():
    q = Question(subject='질문 1입니다.', content='질문1에 대한 내용입니다.', create_date=datetime.now())
    db.session.add(q)
    db.session.commit()

def test1():
    for i in range(10) :
        i = str(i+1)
        q = Question(subject='질문 '+i+'입니다.', content='질문'+i+'에 대한 내용입니다.', create_date=datetime.now())
        db.session.add(q)
    db.session.commit()

def getall_question():
    # result = Question.query.all()
    #
    # for i in result :
    #     print(i.subject)
    result = Question.query.get(1)
    db.session.delete(result)
    db.session.commit()