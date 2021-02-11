# Flask -------------------------------------------------------------
# python 기반의 경량화된 Framework (Django 대비)
# 구현이 간단하고, 웹 서비스 구현에 있어 자유도가 높아 REST API 서버 개발에 많이 사용
# ---------------------------------------------------------------------

# 참조 : flask 패키지
from flask import Flask

# Flask 인스턴스 객체 생성
# Flask 클래스의 생성자로 현재 실행되는 App의 모듈명 전달
# __name__ : 파이썬 전역 변수, 현재 실행되는 App의 모듈명이 자동으로 들어감
app = Flask(__name__)

# 브라우저 상에서 특정 URI(URL과 URN이 이에 속함)을 호출했을 때 실행되는 함수 정의
# -> 이 함수의 결과값이 웹 브라우저에 출력되기 때문에 View 함수라고도 함
# 라우트(route) : Flask에서 제공되는 호출 URI 처리하는 함수와 연결 방법
# -> @app.route() 데커레이터 사용 : 인자에 해당 뷰 함수와 연결될 URL 저장
@app.route('/')   # URI
def hello() :     # 실행되는 View함수
    return 'Hello Flask'

# 테스트로 만들어본 index 페이지
@app.route('/index')
def index() :
    return 'Index Page:) Yeah'

# <name> : URI에서 사용되는 동적 변수 name(데이터 타입 생략 시, default = string)
# -> http://127.0.0.1/info/KEI로 접속할 경우, name = KEI
@app.route('/info/<name>')
def get_name(name) :
    return 'hello {}'.format(name)

# <int:id> : URI에서 사용되는 동적 변수 int형 id
@app.route('/user/<int:id>')
def get_user(id) :
    return 'user id is {}'.format(id)

# 하나의 View 함수에 여러 개의 URI 지정
@app.route('/json/<int:dest_id>/<message>')
@app.route('/JSON/<int:dest_id>/<message>')
def send_message(dest_id, message) :
    json = {
        'bot_id' : dest_id,
        'message' : message
    }
    return json

# 메인 모듈로 실행하는 경우에만 Flask 서버를 실행
# run()함수의 파라미터로 서버주와 포트를 설정할 수 있다.
# main 모듈로 실행했기 때문에 __name__에는 '__main__' 문자열이 저장
if __name__ == '__main__' :
    app.run()   # app.run(host = '127.0.0.1', port = '5000')

