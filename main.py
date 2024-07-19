from control import Game, Airplane
import time

if __name__ == "__main__":
    game = Game()
    airplane = Airplane(game)

    # Test unpausing the game
    game.unpause_game()