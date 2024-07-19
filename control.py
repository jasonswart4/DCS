import pygetwindow as gw
import keyboard
import time

class Game:
    def __init__(self):
        self.keyboard = keyboard

    def focus_dcs_window(self):
        """Bring DCS window to the foreground."""
        windows = gw.getWindowsWithTitle('Digital Combat Simulator')
        if windows:
            dcs_window = windows[0]
            dcs_window.activate()
            time.sleep(1)  # Wait for the window to be focused

    def unpause_game(self):
        """Press 'Esc' to unpause the game."""
        self.focus_dcs_window()
        self.keyboard.press_and_release('esc')
        time.sleep(0.1)  # Allow time for the action to register

class Airplane:
    def __init__(self, game):
        self.keyboard = keyboard
        self.game = game
        self.directions = {
            'centre': [76],               # Numpad 5
            'down_left': [54, 79],        # RShift + Numpad 1
            'down': [54, 80],             # RShift + Numpad 2
            'down_right': [54, 81],        # RShift + Numpad 3
            'left': [54, 75],             # RShift + Numpad 4
            'right': [54, 77],            # RShift + Numpad 6
            'up_left': [54, 71],          # RShift + Numpad 7
            'up': [54, 72],                # RShift + Numpad 8
            'up_right': [54, 73]          # RShift + Numpad 9
        }

    def increase_throttle(self, duration=1):
        """Press '=' to increase throttle for the specified duration."""
        self.game.focus_dcs_window()
        self.keyboard.press('=')
        time.sleep(duration)
        self.keyboard.release('=')

    def decrease_throttle(self, duration=1):
        """Press '-' to decrease throttle for the specified duration."""
        self.game.focus_dcs_window()
        self.keyboard.press('-')
        time.sleep(duration)
        self.keyboard.release('-')

    def toggle_wheelbrake(self, press=True):
        """Press and hold 'w' to apply wheel brake, release 'w' to release brake."""
        self.game.focus_dcs_window()
        if press:
            self.keyboard.press('w')
            print("Wheel brake applied")
        else:
            self.keyboard.release('w')
            print("Wheel brake released")
    
    def pilot_look(self, direction='centre'):
        """Press keys to look in the specified direction."""
        self.game.focus_dcs_window()
        keys = self.directions.get(direction)
        if keys:
            for key in keys:
                self.keyboard.press(key)
            time.sleep(0.1)
            for key in keys:
                self.keyboard.release(key)
        else:
            print(f"Unknown direction: {direction}")

    def test_controls(self):
        """Test sequence: Hold wheel brake, increase throttle for 2 seconds, decrease throttle for 2 seconds."""
        self.toggle_wheelbrake(True)  # Hold wheel brake
        time.sleep(1)  # Ensure the brake is held

        # Hold the wheel brake and perform throttle adjustments
        try:
            self.increase_throttle(1)  # Increase throttle for 2 seconds
            self.decrease_throttle(1)  # Decrease throttle for 2 seconds
        finally:
            self.toggle_wheelbrake(False)  # Ensure the wheel brake is released