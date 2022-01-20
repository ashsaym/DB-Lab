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


def showDrivinLicence():
    drivinLicence = list()
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT * FROM fahrerlaubnis;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            drivinLicence.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LendrivinLicence = len(drivinLicence)
    ibm_db.close(db)
    return drivinLicence, LendrivinLicence


def addLicence(fahrer, ablaufdatum):
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        inser_sql = "INSERT INTO fahrerlaubnis (fahrer, ablaufdatum ) VALUES(?, ?)"
        stmt = ibm_db.prepare(db, inser_sql)
        try:
            ibm_db.execute(stmt, (fahrer, ablaufdatum))
            ibm_db.close(db)
            return True
        except:
            ibm_db.close(db)
            return False


def showRides():
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT * FROM transportmittel;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList


def showJourney():
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT * FROM fahrt;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList


def addJourney(startort, zielort, fahrtdatumzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel, beschreibung):
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        inser_sql = "INSERT INTO fahrt (startort, zielort, fahrtdatumzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel, beschreibung) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        stmt = ibm_db.prepare(db, inser_sql)
        try:
            ibm_db.execute(stmt, (startort, zielort, fahrtdatumzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel, beschreibung))
            ibm_db.close(db)
            return True
        except:
            ibm_db.close(db)
            return False


@app.route('/User', methods=['GET', 'POST'])
def UserPage():
    newUserStatus = None
    title = "User Page | Online Ride Share"
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


@app.route('/DrivingLicence', methods=['GET', 'POST'])
def DrivingLicensePage():
    newDrivingLicence = None
    title = "Driving Licence Page | Online Ride Share"
    Users = getUser()
    if flask.request.method == 'GET':
        DrivingLicences = showDrivinLicence()
        return render_template('driving_licence.html', title=title, DrivingLicences=DrivingLicences[0],
                               LenDrivingLicences=DrivingLicences[1],
                               newDrivingLicence=newDrivingLicence, Users=Users[0], LenUser=Users[1])
    if flask.request.method == 'POST':
        Users = getUser()
        DrivingLicences = showDrivinLicence()
        req = request.form
        driver = req.get("driver")
        date = str(req.get("expireDate") + ('-23.59.59.000000'))
        print(driver, date)
        newDrivingLicence = addLicence(driver, date)
        return render_template('driving_licence.html', title=title, DrivingLicences=DrivingLicences[0],
                               LenDrivingLicences=DrivingLicences[1],
                               newDrivingLicence=newDrivingLicence, Users=Users[0], LenUser=Users[1])


@app.route('/Rides', methods=['GET', 'POST'])
def RidesPage():
    Status = None
    title = "Rides Page | Online Ride Share"
    Users = getUser()
    if flask.request.method == 'GET':
        TempList = showRides()
        return render_template('ride_page.html', title=title, TempList=TempList[0],
                               LenTemp=TempList[1],
                               Status=Status, Users=Users[0], LenUser=Users[1])


@app.route('/Journey', methods=['GET', 'POST'])
def Journey():
    Status = None
    title = "Rides Page | Online Ride Share"
    Users = getUser()
    if flask.request.method == 'GET':
        TempList = showJourney()
        print(TempList)
        return render_template('journey.html', title=title, TempList=TempList[0],
                               LenTemp=TempList[1],
                               Status=Status, Users=Users[0], LenUser=Users[1])


if __name__ == '__main__':
    app.run()
