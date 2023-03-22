#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    g1= Game("game1")
    g2= Game("game2")
    p1 = Player("player1")
    p2 = Player("player2")
    r1 = Result(p1,g1,1)
    r2 = Result(p1,g1,2)
    r3 = Result(p1,g1,3)
    p1.add_result(g2,600)
    print(Result.all)

    print(p1.played_game(g1))
    print(p1.num_times_played(g1))

    

    

    # ipdb.set_trace()
