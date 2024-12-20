import os, sqlite3

KEY = os.path.join(os.path.dirname(__file__), "..", "key")
LOCATION = os.path.join(os.path.dirname(__file__), ".")

class DBM:
    def __init__(self):
        self.db = sqlite3.connect(f"{LOCATION}/main.db", check_same_thread=False)
        self.db_command = self.db.cursor()
    

class Linked():
    def __init__(self):
        self.__uchein = {} #uid와 useesionid를 딕셔너리로 엮는 유저체인
    def new(self, uid, usession_id):
        self.__uchein[uid] = usession_id #인증을 위한 userID + uuid4 쌍 저장
    def is_real(self, uid, usession_id):
        chein_sessionid = self.__uchein.get(uid)
        print(uid, usession_id, chein_sessionid)
        if chein_sessionid == None: return False #차후 로직의 추가 가능성이 있으니 미리 빈값은 거른다
        print(
            f"""
            수신 세션id: {usession_id}
            실제 보유id: {chein_sessionid}
            """
        )
        if chein_sessionid == usession_id: #요청받은 uid로 실제 저장된 딕셔너리에도 동일한 usession_id인지 대조
            return True
        # elif ulink_sessionid != usession_id: #uid와 usession이 다르다면
        else:
            return False





def secret_key():
    try:
        with open(f"{KEY}/ax25.txt") as value: return value.read()
    except:
        with open(f"{KEY}/example.txt") as value: return value.read()

