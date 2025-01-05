from typing import Union
from typing import List

from fastapi import FastAPI, Request, Response, UploadFile, File, Form
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse, HTMLResponse

import os, hashlib, random
from uuid import uuid4
from lib.SGears import secret_key, text_to_hash, Linked, DBM, HashHub, to_mb
#===================================================================
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173", #vuejs
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

# 차후 개선 요구
# class FileRecive(BaseModel): #업로드용 청크
#     filename: str = Form(...)
#     chunk: UploadFile = File(...)

def uuid_gen(): return str(uuid4())
app.add_middleware(SessionMiddleware, secret_key=secret_key())

hashhub = HashHub() #uid와 session의 인증과 추가 역할
linked = Linked() #uid와 session의 인증과 추가 역할
db = DBM() #테스트용 sqlite3 차후에 숙달되면 꼭 mysql쓰도록 하기
FILES = os.path.join(os.path.dirname(__file__), ".", "Files") #전역용 파일 저장 경로
#===================================================================
# db.run("DROP Table Files;")
# db.run(f"CREATE TABLE IF NOT EXISTS Files(uid text, filehash text, filename text, filesize text, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

@app.get("/") #메인페이지니까 가능하면 vue보내주는 방향으로 변경할것
def main():
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
file_hashes = {} #이따 해시 허브라는걸로 따로 만들기
# "c50dad24b4e2558a9e1832d461bcfd059f7c93ec28dc55eea61f3a5e13be8c27bb6899f6db203a542e839b6321185da4c3e19e2d06a3ca885133ec852d0d2e7b"
@app.post("/upload")
async def upload(request: Request, filename: str = Form(...), chunk: UploadFile = File(...), chunk_now: int = Form(...), chunk_max: int = Form(...), size: str = Form(...), ):
    uid = request.cookies.get("uid")
    usession_id = request.cookies.get("usession")
    file_id = f"{uid}_{filename}"
    # file_hash = hashlib.sha512() #리셋되는거 막기 -> 걍 함수 만들죠?

    hashhub.new(file_id)
    
    while True:
        if linked.is_real(uid, usession_id):
            save = f"{FILES}/{filename}"
            print(f"{chunk_now} / {chunk_max}")
            content = await chunk.read(to_mb(10))  # 누가 프론트 수정할수도 있으니 리밋 걸 방법 찾기
            hashhub.hash_update(file_id, content)
            if chunk_now >= chunk_max:
                print("Checking File HASH")
                file_hash = hashhub.hash_result(file_id)
                db.run(f"INSERT INTO Files(uid, filehash, filename) Values('{uid}', '{file_hash}', '{filename}');") #업로더 | 파일해시(중복방지용) | 업로더가 정한 파일이름

            with open(save, "ab") as f:  # 파일에 청크 추가
                f.write(content)
            return 200
        else:
            return 403




@app.post("/files") #나중에 이름 바꿀수 있으면 변경
def upload(request: Request):
    # uid = request.session.get('uid')
    # usession_id = request.session.get('usession')
    uid = request.cookies.get("uid")
    usession_id = request.cookies.get("usession")
    #디비로 쿼리해서 내가 가진게 뭔지 리턴할것 OK
    #차후 디비에 몇몇 항목추가할것
    #공개모드로 할땐 그냥 public이라는 테이블 넣어서 공유자, 비번, 파일hash이렇게 하는것도 좋아보임
    if linked.is_real(uid, usession_id):
        print("Chein OK!")
        try: 
            sub = db.run(f"SELECT json_object('filename', filename, 'date', created) FROM Files WHERE uid = '{uid}'").fetchall() # '<- 이거 추가안하면 못찾음
            return sub
        except: return "NO"
        # print(sub)
    else:
        return "NO"

#인증관련 ============================================
@app.post("/verify") #세션 점검용 + 호출량 적으면 남은 용량 이런것도 주기
def vertify(request: Request):
    uid = request.cookies.get("uid")
    usession_id = request.cookies.get("usession")
    # print(uid, usession_id)
    key_check = linked.is_real(uid, usession_id)
    if key_check:
        return 200
        # return {
        #     "uid" : uid,
        #     "usession" : usession_id,
        #     "is_real?" : key_check,
        # }
    else:
        return 403

@app.post("/login") #나중에 이름 바꿀수 있으면 변경
def login(request: Request, response: Response, idpw: idpw):
    if idpw.id == "" or idpw.pw == "":
        return 403

    uid = idpw.id
    usession_id = uuid_gen()

    #디비로 확인하는코드

    linked.new(uid, usession_id)
    response.set_cookie(
        key="uid",
        value=uid,
        httponly=True,
        secure=False,
    )
    response.set_cookie(
        key="usession",
        value=usession_id,
        httponly=True,  # JavaScript에서 접근 불가
        # samesite='None', # 도메인이 달라도 가능하게 근데 쓰면 갱신 안됌 시발련
        secure=False,   # HTTPS 환경에서는 True로 설정
    )
    return {"code": "OK"}

#인증관련 ============================================
if __name__ == '__main__':
    os.system("fastapi dev run.py --port 3160")