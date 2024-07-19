from control import *

class Procedures:
    def __init__(self, airplane: Airplane):
        self.airplane = airplane

    def pilot_check_controls(self):
        self.airplane.pilot_look('left')
        self.airplane.pilot_look('left')

if __name__ == "__main__":
    game = Game()
    airplane = Airplane(game)
    procedures = Procedures(airplane)

    game.unpause_game()

    procedures.pilot_check_controls()
