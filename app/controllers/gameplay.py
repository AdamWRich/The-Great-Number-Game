from flask import render_template, request, redirect, session
from app import app
from app.models.User import User
from app.models.leaderboard import Leaderboard_class
import random



@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    session['visits'] += 1
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    # print(session['num'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    if session['guess'] == session['num']:
        return render_template('correct.html', num=session['num'])
    elif session['guess'] > 100:
        return render_template("follow_rules.html")    
    elif session['guess'] < 1:
        return render_template("follow_rules.html")
    return redirect('/')

@app.route('/leaderboard', methods=['POST'])
def winners_circle():
    session['guesses'] = session['visits']
    session['username'] = request.form['username']
    new_user = User(session['guesses'], session['username'], session['num'])
    return render_template("leaderboard.html", leaderboard=sorted(Leaderboard_class.leaderboard, key=lambda user: user['guesses']))
    

@app.route('/play_again')
def reset ():
    session.clear()
    return redirect("/")