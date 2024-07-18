import pygetwindow as gw
import time
import keyboard  # Import keyboard library for key combinations
from pynput.keyboard import Controller, Key  # Re-import Key module

keyboard_controller = Controller()

def focus_dcs_window():
    """Bring DCS window to the foreground."""
    windows = gw.getWindowsWithTitle('Digital Combat Simulator')
    if windows:
        dcs_window = windows[0]
        dcs_window.activate()
        time.sleep(1)  # Wait for the window to be focused

def unpause_game():
    """Press 'Esc' to unpause the game."""
    focus_dcs_window()
    keyboard_controller.press(Key.esc)
    keyboard_controller.release(Key.esc)

def increase_throttle():
    """Press 'L Shift + =' to increase throttle."""
    keyboard.press('=')
    time.sleep(1)  # Add a small delay to ensure key press is registered
    keyboard.release('=')

def decrease_throttle():
    """Press 'L Shift + -' to decrease throttle."""
    keyboard.press('-')
    time.sleep(1)  # Add a small delay to ensure key press is registered
    keyboard.release('-')

def toggle_wheelbrake(press=True):
    """Press and hold 'w' to apply wheel brake, release 'w' to release brake."""
    if press:
        keyboard_controller.press('w')
    else:
        keyboard_controller.release('w')

def test_controls():
    """Test sequence: Hold wheel brake, increase throttle for 2 seconds, decrease throttle for 2 seconds."""
    toggle_wheelbrake(True)  # Hold wheel brake
    time.sleep(1)  # Ensure the brake is held

    # Hold the wheel brake and perform throttle adjustments
    try:
        for _ in range(2):  # Increase throttle for 2 seconds
            increase_throttle()
            time.sleep(0.1)
        for _ in range(2):  # Decrease throttle for 2 seconds
            decrease_throttle()
            time.sleep(0.1)
    finally:
        toggle_wheelbrake(False)  # Ensure the wheel brake is released