import ibm_db


def showUser():
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


def showReview():
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=MYAPP;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT * FROM bewertung;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList
