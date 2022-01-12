import flask
import ibm_db_dbi
from flask import Flask, render_template, request, redirect, session
import ibm_db

app = Flask(__name__)
app.secret_key = "any random string"


@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Online Ride Share"
    return render_template('index.html', title=title)


def getUser():
    Users = list()
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT * FROM benutzer;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            Users.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LenUser = len(Users)
    ibm_db.close(db)
    return Users, LenUser


def addNewUser(email, name):
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        inser_sql = "INSERT INTO benutzer (name, email) VALUES(?, ?)"
        stmt = ibm_db.prepare(db, inser_sql)
        try:
            ibm_db.execute(stmt, (name, email))
            ibm_db.close(db)
            return True
        except:
            ibm_db.close(db)
            return False


@app.route('/User', methods=['GET', 'POST'])
def addUser():
    newUserStatus = None
    title = "Add User | Online Ride Share"
    if flask.request.method == 'GET':
        Users = getUser()
        return render_template('user_create.html', title=title, Users=Users[0], LenUser=Users[1],
                               newUserStatus=newUserStatus)
    if flask.request.method == 'POST':
        Users = getUser()
        req = request.form
        email = req.get("email")
        name = req.get("name")
        newUserStatus = addNewUser(email, name)
        return render_template('user_create.html', title=title, Users=Users[0], LenUser=Users[1],
                               newUserStatus=newUserStatus)


if __name__ == '__main__':
    app.run()
