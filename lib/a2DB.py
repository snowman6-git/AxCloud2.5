import sqlite3, hashlib, os
from datetime import datetime
from time import sleep
def sql_filter(s): return s.replace("'", "''")

LOCATION = os.path.join(os.path.dirname(__file__), ".")

# class MDB:
#     def __init__(self):
#         self.db = sqlite3.connect(f"{LOCATION}/main.db"
#         self.db_command = self.db.cursor()

    


#     @staticmethod
#     def find_and_load():
#         return MDB()

class DBM:
    def __init__(self):
        self.db = sqlite3.connect(f"{LOCATION}/main.db", check_same_thread=False)
        self.db_command = self.db.cursor()
    
    def vertify(self, id, pw):
        info = self.db_command.execute("SELECT * FROM idpw WHERE userID = ?", (id,)).fetchone()
        salt_bottle = hashlib.sha512((pw + "aa2+@:D").encode()).hexdigest()
        if id == info[1] and salt_bottle == info[2]:
            print(f"값이 동일하여 권한이 지급함\n{id}/{info[1]}\n{salt_bottle}\n{info[2]}")
            return True
        else:
            # print("vertify Fail!")
            # print(f"{id} / {info[1]}")
            # print(f"{salt_bottle} / {info[2]}")
            return False

    def delete(self, line, table="gulist"):
        self.db_command.execute(f"DELETE FROM {table} WHERE id = '{line}'")
        self.db.commit()
    def reply(self, target, writer, bonmoon, edit=False): #유저 프사는 다른 방식으로 호출하기/
        self.db_command.execute(f"""
        INSERT INTO 
        reply(id, writer, bonmoon, edit) 
        Values('{target}', '{writer}', '{sql_filter(bonmoon)}', '{edit}');
        """)
        self.db.commit()
    def like(self, id, user):
        if (self.db_command.execute(f"SELECT like FROM view WHERE viewer = '{user}' and id = {id};").fetchone()[0] == "0"):
            self.db_command.execute(f"UPDATE view SET like = 1 WHERE viewer = '{user}';")
            self.db.commit()
        else:
            print("이미 좋아요함")
            pass

    def save(self, tag, writer, ip, title, bonmoon, public=True):
        print("글 작성 시도중")
        print(writer)
        self.db_command.execute(f"INSERT INTO gulist(tag, writer, ip, title, bonmoon, public) Values('{tag}', '{sql_filter(writer)}', '{ip}', '{sql_filter(title)}', '{sql_filter(bonmoon)}', '{public}');")
        self.db.commit()
        print("글 작성 완료!")
        return True

    def new(self, id, pw):
        print(pw)
        if (self.db_command.execute("SELECT * FROM idpw WHERE userID = ?", (id,)).fetchone() == None):
            salt_bottle = hashlib.sha512((pw + "여기엔자신이사용하는예측불가능한비밀번호를하나덧대는것이좋습니다원래제가쓰는건지웠으니추론은하지마십쇼ㅋ").encode()).hexdigest()
            print(salt_bottle)
            self.db_command.execute(f"INSERT INTO idpw(uname, userID, userPW, email) Values('{id}', '{id}', '{salt_bottle}', 'None');")
            self.db.commit()
            return True
        else:
            print(f"the user: {id} is already Exit")
            return False

    def myinfo(self, uid):
        print(uid)
        uname = self.db_command.execute(f"SELECT uname FROM idpw WHERE userID = '{uid}'").fetchone()[0]# == None and uid != None
        if (uname):
            print(uname)
            return uname
        else:
            return False

        # sub = self.db_command.execute(f"SELECT json_object('like', sum(like), 'views', COUNT(*)) FROM view WHERE id = {line};").fetchone()
        # info = self.db_command.execute(f"SELECT json_object('id', id, 'writer', writer, 'ip', ip, 'title', title, 'bonmoon', bonmoon, 'public', public, 'time', created) FROM gulist WHERE id = {line};").fetchone()
        
        # # print(sub)
        # info = {
        #     "info" : info,
        #     "sub" : sub
        # }

        # # info = self.db_command.execute(f"SELECT * FROM gulist LIMIT {line}").fetchone()

    def readline(self, line, uid):
        #id/뷰어 리턴 | id와 viewer두 조건이 부합하는 행 조회
        if (self.db_command.execute("SELECT id, viewer FROM view WHERE id = ? and viewer = ?", (line, uid)).fetchone() == None and uid != None):
            self.db_command.execute(f"INSERT INTO view(id, viewer, ip, like) Values('{line}', '{uid}', 'x', '0');")
            self.db.commit()
        else:
            pass

        sub = self.db_command.execute(f"SELECT json_object('like', sum(like), 'views', COUNT(*)) FROM view WHERE id = {line};").fetchone()
        info = self.db_command.execute(f"SELECT json_object('id', id, 'writer', writer, 'ip', ip, 'title', title, 'bonmoon', bonmoon, 'public', public, 'time', created) FROM gulist WHERE id = {line};").fetchone()
        
        # print(sub)
        info = {
            "info" : info,
            "sub" : sub
        }

        # info = self.db_command.execute(f"SELECT * FROM gulist LIMIT {line}").fetchone()
        return info

    def recent(self):
        # rgul = self.db_command.execute("SELECT DISTINCT tag FROM gulist LIMIT 5;").fetchall()
        rgul = self.db_command.execute("SELECT json_object('title', title, 'time', max(created), 'tag', tag) AS max_value FROM gulist GROUP BY tag LIMIT 5;").fetchall()
        # rgul = self.db_command.execute("SELECT * FROM gulist WHERE tag IN (SELECT DISTINCT title FROM gulist LIMIT 5);").fetchall()
        return rgul
    

    def readlines(self, tag, start, end, target=None):
        if tag == "gul":
            gul = self.db_command.execute(f"SELECT json_object('id', id, 'writer', writer, 'ip', ip, 'title', title, 'bonmoon', bonmoon, 'public', public, 'time', created) FROM gulist WHERE tag = '{target}' ORDER BY created DESC LIMIT {end} OFFSET {start}").fetchall()
            # info = self.db_command.execute(f"SELECT * FROM gulist LIMIT {end} OFFSET {start};").fetchall()
            #게시글 ID | 좋아요 총합 | 조회수
            # views = self.db_command.execute(f"SELECT id, like, COUNT(*) AS count FROM view WHERE id IN (SELECT id FROM gulist LIMIT {end} OFFSET {start}) GROUP BY id;").fetchall()
            # likes = self.db_command.execute(f"SELECT like, SUM(like) AS like FROM view GROUP BY like;").fetchall()
            # likes = self.db_command.execute(f"SELECT like, TOTAL(like) AS like FROM view GROUP BY like;").fetchall()
            #아래의 쿼리로 통합
            # likes = self.db_command.execute(f"select id, like, sum(like), total(like) from view WHERE id = ?;", (line)).fetchall()
            sub = self.db_command.execute(f"SELECT json_object('id', id, 'like', sum(like), 'views', COUNT(*))FROM view WHERE id IN (SELECT id FROM gulist ORDER BY id DESC LIMIT {end} OFFSET {start}) GROUP BY id;").fetchall()
            # sub = self.db_command.execute(f"SELECT json_object('id', id, 'like', sum(like), 'views', COUNT(*)) FROM view WHERE id IN (SELECT id FROM gulist LIMIT {end} OFFSET {start}) GROUP BY id;").fetchall()
            # print(sub)
            info = {
                "info" : gul,
                "sub" : sub
            }
        if tag == "reply":
            info = self.db_command.execute(f"SELECT json_object('target', id, 'writer', writer, 'bonmoon', bonmoon, 'time', created) FROM reply WHERE id = {target} LIMIT {end} OFFSET {start};").fetchall()
            # info = self.db_command.execute(f"SELECT json_object('target', id, 'writer', writer, 'ip', ip, 'title', title, 'bonmoon', bonmoon, 'public', public, 'time', created) FROM reply LIMIT {end} OFFSET {start}").fetchall()
        return info



    def rank(self):
        # info = self.db_command.execute(f"SELECT id, SUM(like) AS total_likes FROM view GROUP BY id ORDER BY total_likes DESC LIMIT 3;").fetchall()
        # info = self.db_command.execute(f"SELECT tag, title, writer, bonmoon FROM gulist WHERE id IN (SELECT id FROM view GROUP BY id ORDER BY SUM(like) DESC LIMIT 3);").fetchall()
        
        info = self.db_command.execute(f"SELECT json_object('id', v.id, 'like', SUM(v.like), 'view', COUNT(*), 'tag', o.tag, 'title', o.title, 'writer', o.writer, 'bonmoon', o.bonmoon) AS total_likes FROM view v JOIN gulist o ON v.id = o.id GROUP BY v.id ORDER BY SUM(v.like) DESC LIMIT 3;").fetchall()
        return info

    def run(self, command):
        print(f"excute: {command}...")
        try:
            self.db_command.execute(command)
            self.db.commit()
            print(f"excute: {command}...OK!")
        except Exception as E:
            print(E)
    

    @staticmethod
    def find_and_load():
        return DBM()



db = DBM()
# db.rank()
# for i in range(10, 1, -1):
#     db.save(tag="자유", writer="aaa", ip="127.0.0.1", title=f"자유테스트: {i}", bonmoon="/", public=True)
#     sleep(1)

# db.recent()

# 리셋
# db.run("DELETE FROM gulist;")
# db.run("DELETE FROM reply;")
# db.run("DELETE FROM view;")
# db.run("DELETE FROM idpw;")
# db.run("DELETE FROM sqlite_sequence WHERE name='gulist';") #오토카운트 제거


# "14", "snowman6", "14번 글의 댓글을 테스트하다"
# db.run(f"DROP Table reply;")#테이블 전체삭제

# db.run(f"CREATE TABLE IF NOT EXISTS reply(id text, writer text, bonmoon text, edit text, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

# def save(self, tag, writer, ip, title, bonmoon, public=True):
# db.save(tag="익명", writer="aaa", ip="127.0.0.1", title="중복테스트", bonmoon="/", public=True)
# db.run(f"DROP Table reply;")


# 공개여부는 넣든말든 알아서 하셈, 글삭튀 방지로 삭제시 열이 사라지는게 아니라 권한없음 페이지로 돌리는 방식
# self.db_command.execute("CREATE TABLE gulist();")

# db.run(f"CREATE TABLE IF NOT EXISTS gulist(id INTEGER PRIMARY KEY AUTOINCREMENT, tag text, writer text, ip text, title text, bonmoon text, public yes, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")

# id = "console"
# salt_bottle = "test"

# db.run(f"INSERT INTO idpw(uname, userID, userPW, email) Values('{id}', '{id}', '{salt_bottle}', 'None');")


# db.run(f"INSERT INTO idpw(uname, userID, userPW, email) Values('{id}', '{id}', '{salt_bottle}', 'None');")




    # def create(self):
    #     self.db_command.execute("CREATE TABLE idpw(userID text, userPW text, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, email text);")


# conn = sqlite3.connect(f"{LOCATION}/main.db", check_same_thread=False)
# cursor = conn.cursor()
# post_id = 3
# # 조회수 계산 쿼리
# cursor.execute()
# count = cursor
# print(f"Post ID {post_id}의 조회수: {count}")

# # 연결 종료
# conn.close()

# mdb = MDB()
# mdb.run("INSERT INTO view(id, viewer, ip, like) Values('1', 'console', 'x', '3000');")
# mdb.run("drop table gulist;") #지정 테이블 전체 지우기

# a = mdb.run("SELECT COUNT(*) FROM view WHERE id = ?", (3,)).fetchone() #지정 테이블 전체 지우기
# a = mdb.run("SELECT COUNT(*)  FROM gulist WHERE writer = 'testuser';") #오토카운트 제거
# print(a)


# mdb.run("DELETE FROM sqlite_sequence WHERE name='gulist';") #오토카운트 제거
# mdb.run("DELETE FROM gulist;") #지정 테이블 전체 지우기
# mdb.run("VACUUM;") #아직 뭔지모르겠음
# mdb.new("console", "localhost", "테스트", "로컬 콘솔로 부터 추가됌")
# mdb.reply("14", "snowman6", "14번 글의 댓글을 테스트하다")
# for i in range(1, 200):
    # mdb.new("", "","","")
    # mdb.delete(line=i, table="gulist")