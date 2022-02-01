import ibm_db


def showUser():
    Users = list()
    db = ibm_db.connect(
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
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
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT fahrerlaubnis.nummer, benutzer.name, fahrerlaubnis.ablaufdatum FROM fahrerlaubnis INNER JOIN benutzer ON fahrerlaubnis.fahrer=benutzer.bid;"
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
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
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
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT fahrt.fid,fahrt.startort,fahrt.zielort,fahrt.fahrtdatumzeit,fahrt.maxPlaetze,fahrt.fahrtkosten,fahrt.status,fahrt.beschreibung,benutzer.name as bName, transportmittel.name as tName, transportmittel.icon FROM fahrt LEFT JOIN benutzer ON fahrt.anbieter=benutzer.bid LEFT JOIN transportmittel ON fahrt.transportmittel=transportmittel.tid WHERE fahrt.anbieter > 0;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList


def showOffenJourney():
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT fahrt.fid,fahrt.startort,fahrt.zielort,fahrt.fahrtdatumzeit,fahrt.maxPlaetze,fahrt.fahrtkosten,fahrt.status,fahrt.beschreibung,benutzer.name as bName, transportmittel.name as tName, transportmittel.icon FROM fahrt LEFT JOIN benutzer ON fahrt.anbieter=benutzer.bid LEFT JOIN transportmittel ON fahrt.transportmittel=transportmittel.tid WHERE fahrt.status = 'offen';"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList


def showGeschlossenJourney():
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT fahrt.fid,fahrt.startort,fahrt.zielort,fahrt.fahrtdatumzeit,fahrt.maxPlaetze,fahrt.fahrtkosten,fahrt.status,fahrt.beschreibung,benutzer.name as bName, transportmittel.name as tName, transportmittel.icon FROM fahrt LEFT JOIN benutzer ON fahrt.anbieter=benutzer.bid LEFT JOIN transportmittel ON fahrt.transportmittel=transportmittel.tid WHERE fahrt.status = 'geschlossen';"
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
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
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


def showJourneyReview():
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT benutzer.name,fahrt.startort,fahrt.zielort,fahrt.fahrtdatumzeit as fTime,bewertung.textnachricht,bewertung.erstellungsdatum as bTime,bewertung.rating FROM schreiben LEFT JOIN benutzer ON schreiben.benutzer=benutzer.bid LEFT JOIN fahrt ON schreiben.fahrt =fahrt.fid LEFT JOIN bewertung ON schreiben.bewertung =bewertung.beid  WHERE SCHREIBEN.BENUTZER > 0;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList


def showAllReservation():
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT benutzer.email,fahrt.startort,fahrt.zielort,fahrt.fahrtdatumzeit as fTime,fahrt.status FROM reservieren LEFT JOIN benutzer ON reservieren.kunde=benutzer.bid LEFT JOIN fahrt ON reservieren.fahrt =fahrt.fid  WHERE reservieren.kunde > 0;"
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList


def showUserReservation(email):
    tempList = list()
    db = ibm_db.connect(
        "DATABASE=SHARER;HOSTNAME=cronus.is.inf.uni-due.de;PORT=50002;PROTOCOL=TCPIP;UID=dbp002;PWD=upehu3ez;", "", "")
    if db:
        sql = "SELECT benutzer.email,fahrt.startort,fahrt.zielort,fahrt.fahrtdatumzeit as fTime,fahrt.status FROM reservieren LEFT JOIN benutzer ON reservieren.kunde=benutzer.bid LEFT JOIN fahrt ON reservieren.fahrt =fahrt.fid  WHERE benutzer.email = '{}';".format(email)
        stmt = ibm_db.exec_immediate(db, sql)
        result = ibm_db.fetch_assoc(stmt)
        while result:
            tempList.append(result)
            result = ibm_db.fetch_assoc(stmt)
    LentempList = len(tempList)
    ibm_db.close(db)
    return tempList, LentempList
