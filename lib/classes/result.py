class Result:
    all = []
    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self.score = score
        Result.all.append(self)
    def get_player(self):
        return self._player
    def set_player(self, player):
        self._player = player
    player = property(get_player, set_player)

    def get_game(self):
        return self._game
    def set_game(self, game):
        self._game = game
    game = property(get_game, set_game)

    def get_score(self):
        return self._score
    def set_score(self, score):
        if(0<score<5000 and isinstance(score, int)):
            self._score = score
        else:
            raise Exception("Score must be an integer between 1 and 5000")
    score = property(get_score, set_score)
