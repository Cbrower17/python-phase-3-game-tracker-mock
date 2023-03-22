# from classes.result import Result

class Player:
    def __init__(self,username):
        self.username = username
    # properties time
    def get_username(self):
        return self._username
    def set_username(self,username):
        if(isinstance(username,str) and 1<len(username)<=16):
            self._username = username
        else:
            raise Exception ("Invalid username, must be a string, 2-16 characters long")
    username = property(get_username, set_username)
    #relational methods time
    def played_game(self, game):
        from .result import Result
        games = [result.game for result in Result.all if result.player == self]
        return game in games
    def num_times_played(self,game):
        from classes.result import Result
        count = 0
        for result in Result.all:
            if result.player == self:
                count += 1
        return count
    def add_result(self,game, score):
        from classes.result import Result
        new_result = Result(self, game, score)
        return new_result
