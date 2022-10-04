import server


class Leaderboard_class:
    leaderboard = []

    def __init__(self):
        self.name = 'leaderboard'
    
    def add_to_leaderboard(self, session):
        Leaderboard_class.leaderboard.append(session)
        return self