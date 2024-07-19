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