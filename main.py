from control import *

def main():
    game = Game()
    airplane = Airplane()

    game.unpause_game()
    airplane.test_controls()

if __name__ == "__main__":
    game = Game()
    airplane = Airplane(game)

    # Test unpausing the game
    game.unpause_game()

    # Test airplane controls
    airplane.test_controls()
