from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware

import os, hashlib, random
from uuid import uuid4
from lib.SGears import secret_key
#===================================================================
app = FastAPI()
class idpw(BaseModel):
    id: str
    pw: str
def uuid_gen(): return str(uuid4())
app.add_middleware(SessionMiddleware, secret_key=secret_key())
#===================================================================

@app.get("/")
def main(request: Request):
    return {
        "uid" : request.session.get('uid'),
        "usession" : request.session.get('usession'),
    }

@app.post("/verify")
def vertify(request: Request, idpw: idpw):
    #실제로 디비랑 상호작용하는 코드, 개발단게에선 제외
    request.session["uid"] = idpw.id
    request.session['usession'] = uuid_gen()
    return 200

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    os.system("fastapi dev run.py --port 3160")