from game import Game

game = Game("Player1", "Player2")


def test_play1(self):
    game = Game("Player1", "Player2")
    assert game.play(11) == "Wrong Cell Number"

def test_play2(self):
    game = Game("Player1", "Player2")
    assert game.isTurn == 1

