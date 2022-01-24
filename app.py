import flask
import ibm_db
from flask import Flask, render_template, request
from showSQL import *
from addSQL import *

app = Flask(__name__)
app.secret_key = "any random string"


@app.route('/', methods=['GET', 'POST'])
def index():
    title = "Online Ride Share"
    return render_template('index.html', title=title)


@app.route('/User', methods=['GET', 'POST'])
def UserPage():
    newUserStatus = None
    title = "User Page | Online Ride Share"
    if flask.request.method == 'GET':
        Users = showUser()
        return render_template('user_create.html', title=title, Users=Users[0], LenUser=Users[1],
                               newUserStatus=newUserStatus)
    if flask.request.method == 'POST':
        Users = showUser()
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
    Users = showUser()
    if flask.request.method == 'GET':
        DrivingLicences = showDrivinLicence()
        return render_template('driving_licence.html', title=title, DrivingLicences=DrivingLicences[0],
                               LenDrivingLicences=DrivingLicences[1],
                               newDrivingLicence=newDrivingLicence, Users=Users[0], LenUser=Users[1])
    if flask.request.method == 'POST':
        Users = showUser()
        DrivingLicences = showDrivinLicence()
        req = request.form
        driver = req.get("driver")
        date = str(req.get("expireDate") + ('-23.59.59.000000'))

        newDrivingLicence = addLicence(driver, date)
        return render_template('driving_licence.html', title=title, DrivingLicences=DrivingLicences[0],
                               LenDrivingLicences=DrivingLicences[1],
                               newDrivingLicence=newDrivingLicence, Users=Users[0], LenUser=Users[1])


@app.route('/Rides', methods=['GET', 'POST'])
def RidesPage():
    Status = None
    title = "Rides Page | Online Ride Share"
    Users = showUser()
    if flask.request.method == 'GET':
        TempList = showRides()
        return render_template('ride_page.html', title=title, TempList=TempList[0],
                               LenTemp=TempList[1],
                               Status=Status, Users=Users[0], LenUser=Users[1])


@app.route('/Journey', methods=['GET', 'POST'])
def Journey():
    Status = None
    title = "Rides Page | Online Ride Share"
    Users = showUser()
    TempRide = showRides()
    TempList = showJourney()
    if flask.request.method == 'GET':
        return render_template('journey.html', title=title, TempList=TempList[0],
                               LenTemp=TempList[1], TempRide=TempRide[0],
                               LenRide=TempRide[1],
                               Status=Status, Users=Users[0], LenUser=Users[1])
    if flask.request.method == 'POST':
        req = request.form
        startort = req.get("startort")
        zielort = req.get("zielort")
        fahrtdatum = req.get("fahrtdatum")
        fahrtzeit = req.get("fahrtzeit").replace(':', '.') + '.00.000000'
        maxPlaetze = req.get("maxPlaetze")
        fahrtkosten = req.get("fahrtkosten")
        anbieter = req.get("anbieter")
        transportmittel = req.get("transportmittel")
        beschreibung = req.get("beschreibung")
        fahrtdatumzeit = fahrtdatum + '-' + fahrtzeit
        print(startort, zielort, fahrtdatum, fahrtzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel,
              beschreibung)
        Status = addJourney(startort, zielort, fahrtdatumzeit, maxPlaetze, fahrtkosten, anbieter, transportmittel,
                            beschreibung)
        return render_template('journey.html', title=title, TempList=TempList[0],
                               LenTemp=TempList[1], TempRide=TempRide[0],
                               LenRide=TempRide[1],
                               Status=Status, Users=Users[0], LenUser=Users[1])


@app.route('/Review', methods=['GET', 'POST'])
def ReviewPage():
    Status = None
    title = "Review Page | Online Ride Share"
    Users = showUser()
    if flask.request.method == 'GET':
        TempList = showReview()
        return render_template('review_page.html', title=title, TempList=TempList[0],
                               LenTemp=TempList[1],
                               Status=Status, Users=Users[0], LenUser=Users[1])


if __name__ == '__main__':
    app.run()
