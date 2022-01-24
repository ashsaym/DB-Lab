import ibm_db


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


def addJourney(startort, zielort, fahrtdatumzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel, beschreibung):
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        inser_sql = "INSERT INTO fahrt (startort, zielort, fahrtdatumzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel, beschreibung) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        stmt = ibm_db.prepare(db, inser_sql)
        try:
            ibm_db.execute(stmt, (
            startort, zielort, fahrtdatumzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel, beschreibung))
            ibm_db.close(db)
            return True
        except:
            ibm_db.close(db)
            return False
