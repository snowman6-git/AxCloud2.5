from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

import os, hashlib, random
from uuid import uuid4
from lib.SGears import secret_key, text_to_hash, Linked, DBM
#===================================================================
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class idpw(BaseModel):
    id: str
    pw: str
class file_infos(BaseModel):
    name: str
def uuid_gen(): return str(uuid4())
app.add_middleware(SessionMiddleware, secret_key=secret_key())

linked = Linked() #uid와 session의 인증과 추가 역할
db = DBM() #테스트용 sqlite3 차후에 숙달되면 꼭 mysql쓰도록 하기
#===================================================================


@app.get("/") #메인페이지니까 가능하면 vue보내주는 방향으로 변경할것
def main(request: Request):
    # uid = idpw.id
    # usession_id = uuid_gen()
    # request.session["uid"] = idpw.id
    # request.session['usession'] = usession_id
    return 200
    # uid = request.session.get('uid')
    # usession_id = request.session.get('usession')
    # # print(uid, usession_id)
    # key_check = linked.is_real(uid, usession_id)
    # if key_check:
    #     return {
    #         "uid" : uid,
    #         "usession" : usession_id,
    #         "is_real?" : key_check,
    #     }
    # else: return "need login"

#파일저장 ============================================
@app.post("/upload") #나중에 이름 바꿀수 있으면 변경
def upload(request: Request, file: file_infos):
    uid = request.session.get('uid')
    usession_id = request.session.get('usession')

    #실제로 파일을 올렸을때의 코드
    if linked.is_real(uid, usession_id):
        print("Chein OK!")

        db.run(f"CREATE TABLE IF NOT EXISTS File_infos(uid text, filehash text, filename text, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
        db.run(f"INSERT INTO File_infos(uid, filehash, filename) Values('{uid}', '{text_to_hash(file.name)}', '{file.name}');") #나중엔 실제 업로드 청크단위 저장 업데이트로 해싱한걸 넣기
        print(file.name)
        return {
            "uid" : uid,
            "filename" : file.name
        }
    else:
        return {
            "uid" : uid,
            "usession" : usession_id
        }

@app.post("/files") #나중에 이름 바꿀수 있으면 변경
def upload(request: Request):
    uid = request.session.get('uid')
    usession_id = request.session.get('usession')

    #디비로 쿼리해서 내가 가진게 뭔지 리턴할것 OK
    #차후 디비에 몇몇 항목추가할것
    #공개모드로 할땐 그냥 public이라는 테이블 넣어서 공유자, 비번, 파일hash이렇게 하는것도 좋아보임
    if linked.is_real(uid, usession_id):
        print("Chein OK!")
        sub = db.run(f"SELECT filename, created FROM File_infos WHERE uid = '{uid}'").fetchall() # '<- 이거 추가안하면 못찾음

        print(sub)
        
        return sub
        # return {
        #     "uid" : uid,
        # }
    else:
        return "NO"
#인증관련 ============================================
@app.get("/verify") #세션 점검용
def vertify(request: Request):
    uid = request.session.get('uid')
    usession_id = request.session.get('usession')
    # print(uid, usession_id)
    key_check = linked.is_real(uid, usession_id)
    if key_check:
        return {
            "uid" : uid,
            "usession" : usession_id,
            "is_real?" : key_check,
        }
    else: return "need login"

@app.post("/login") #나중에 이름 바꿀수 있으면 변경
def vertify(request: Request, idpw: idpw):
    #실제로 디비랑 상호작용하는 코드, 개발단게에선 제외
    print(idpw)
    #발급
    uid = idpw.id
    usession_id = uuid_gen()

    linked.new(uid, usession_id)

    request.session["uid"] = idpw.id
    request.session['usession'] = usession_id
    return 200
#인증관련 ============================================

if __name__ == '__main__':
    os.system("fastapi dev run.py --port 3160")