import json
from datetime import datetime as dt
from flask import Flask,render_template,request,redirect,flash,url_for

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

clubs = loadClubs()
print(clubs[0]['email'])

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
nb_points = 12
todayData = dt.today().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def score():
    return render_template('score.html', clubs = clubs)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    if club:
        club_email = club[0]
        return render_template('welcome.html',club=club_email,competitions=competitions)
    else:
        return render_template('index.html', error = "Désolé, cet email n'a pas été trouvé"), 403


@app.route('/book/<competition>/<club>')
def book(competition,club):
    try:
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
    
        if foundClub and foundCompetition:
                if foundCompetition['date'] > todayData:
                    return render_template('booking.html',club=foundClub,competition=foundCompetition)
                else:
                    return  render_template('booking.html',club=foundClub,competition=foundCompetition, error="Date limite d'achat dépassé, cliquez ici pour revenir en arrière :"), 403
    except : 
        return redirect(url_for('index')), 403


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    pts = int(club["points"])

    if placesRequired <= 12 and placesRequired>0:
        if placesRequired <= int(competition['numberOfPlaces']) and pts*3 >= placesRequired and pts-placesRequired*3>=0  :
            competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
            club["points"] = pts - placesRequired*3
            pts = pts - placesRequired*3 
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)
        else:
            return render_template('welcome.html', club=club, competitions=competitions, error = "Not enoought point for buy"), 403
    else:
        return render_template('welcome.html', club=club, competitions=competitions, error = "Impossible to buy more than 12 places and less than 1"), 403


# TODO: Add route for points display

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)