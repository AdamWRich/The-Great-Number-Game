from app.controllers import gameplay
from app.models import leaderboard

class User:
    def __init__(self, guesses, username, num):
        self.list = {'num': num, 'username': username, 'guesses':guesses}
        leaderboard.Leaderboard_class.add_to_leaderboard(self, self.list)
        