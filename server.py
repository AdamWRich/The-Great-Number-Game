from flask import Flask, render_template, request, redirect, session
import random
import leaderboard_users
app = Flask(__name__)
app.secret_key = "Billy jean is not my lover"

class Users:
    def __init__(self, guesses, username, num):
        self.list = {'num': num, 'username': username, 'guesses':guesses}
        begin.add_to_leaderboard(self.list)



if __name__ == "__main__":
    global var
    begin = leaderboard_users.Leaderboard_class()

    leaderboard= leaderboard_users.Leaderboard_class.leaderboard

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
        new_user = Users(session['guesses'], session['username'], session['num'])
        return render_template("leaderboard.html", leaderboard=sorted(leaderboard, key=lambda user: user['guesses']))
        

    @app.route('/play_again')
    def reset ():
        session.clear()
        return redirect("/")



if __name__=="__main__":
    app.run(debug=True)



# uncomment line 27 in order to see the secret number printed in the console!