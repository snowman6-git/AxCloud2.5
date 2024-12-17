from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware

import os, hashlib, random
from uuid import uuid4
from lib.SGears import secret_key, Linked
#===================================================================
app = FastAPI()
class idpw(BaseModel):
    id: str
    pw: str
def uuid_gen(): return str(uuid4())
app.add_middleware(SessionMiddleware, secret_key=secret_key())
linked = Linked() #uid와 session의 인증과 추가 역할
#===================================================================


@app.get("/") #메인페이지니까 가능하면 vue보내주는 방향으로 변경할것
def main(request: Request):
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
    
    #발급
    uid = idpw.id
    usession_id = uuid_gen()

    linked.new(uid, usession_id)

    request.session["uid"] = idpw.id
    request.session['usession'] = usession_id
    return 200

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    os.system("fastapi dev run.py --port 3160")