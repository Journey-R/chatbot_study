# HTTP 메소드별 CRUD 동작 -------------------------------------------------------------
# POST :    Create -> 서버 리소스 생성
#                     URI 접속으로 작동 결과 확인 불가 -> 웹 앱을 만들어야 테스트 가능
# GET  :    Read   -> 서버 리소스 읽기
#                     URI 접속으로 작동 결과 확인 가능
# PUT  :    Update -> 서버 리소스 수정
# DELETE :  Delete -> 서버 리소스 삭제
# --------------------------------------------------------------------------------------

# REST API 테스트 Tool -----------------------------------------------------------------
# 1. Talend API Tester 확장 프로그램 추가 : chrome 웹 스토어
# 2. POST Test : Talend API Tester에서 method, URI 및 body 입력 후 'Send'
# 3. GET Test : Talend API Tester에서 method, URI 입력 후 'Send'
# --------------------------------------------------------------------------------------

# 참조
# request : client로부터 HTTP 요청(requset)를 받았을 때 요청 정보를 확인할 수 있는 모듈
# jsonify : 데이터 객체를 JSON 응답으로 변환해주는 Flask의 유틸리티 함수
from flask import Flask, request, jsonify
app = Flask(__name__)

# 서버 리소스
# 웹 서버의 리소스를 표현하기 위해 생성한 리스트 객체
# 아래 코드에서는 GET, POST 메소드로 호출된 REST API를 통해 해당 리소스에 객체를 추가하고 불러오도록 구현
resource = []

# 사용자 정보 조회
# user_id에 맞는 사용자 정보를 조회하는 GET메소드의 REST API 정의
# route 데커레이터 파라미터의 methods : default = GET, 생략 가능
@app.route('/user/<int:user_id>', methods = ['GET'])
def get_user(user_id) :
    for user in resource :
        if user['user_id'] is user_id :
            return jsonify(user)
    return jsonify(None)

# 사용자 추가
# 사용자 정보를 추가하는 POST 메서드의 REST API
# add_user() : HTTP 요청시 Body에 포함된 JSON 데이터를 서버 리소스에 추가한 후 현재 저장된 전체 리소스 데이터를 JSON으로 변환하여 응답
# request.get_json() : HTTP 요청 Body의 JSON 객체를 dict형으로 가져옴
# jsonify() : resource 리스트를 JSON 응답 형태로 반환
@app.route('/user', methods = ['POST'])
def add_user():
    user = request.get_json() # HTTP 요청의 body에서 json 데이터를 불러옴
    resource.append(user) # 리소스 리스트에 추가
    return jsonify(resource)

if __name__ == '__main__' :
    app.run()
