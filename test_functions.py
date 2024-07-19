from control import Game, Airplane
import time

def test_pilot_look(game, airplane):
    directions = ['centre', 'left', 'centre', 'right', 'centre', 'up', 'centre', 'down', 'centre']
    for direction in directions:
        airplane.pilot_look(direction)
        time.sleep(0.1)
    print("pilot look tested")

def test_controls(game, airplane):
    airplane.test_controls()
    print("Controls tested")

def run_tests(tests):
    game = Game()
    airplane = Airplane(game)

    game.unpause_game()
    
    for test in tests:
        test(game, airplane)

if __name__ == "__main__":
    tests_to_run = [test_pilot_look, test_controls]
    run_tests(tests_to_run)
