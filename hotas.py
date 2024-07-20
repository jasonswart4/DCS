import pyvjoy
import time

def check_vjoy_installation():
    """Check if vJoy is installed and configured correctly."""
    try:
        j = pyvjoy.VJoyDevice(1)
        j.reset()
        print("vJoy device 1 initialized successfully.")
    except Exception as e:
        print("Failed to initialize vJoy device. Ensure vJoy is installed and configured correctly.")
        print("Error:", e)
        return False
    return True

def set_pitch(j, value):
    """Set the pitch axis. Value should be between -1 and 1."""
    scaled_value = int((value + 1) * 0x4000)
    j.set_axis(pyvjoy.HID_USAGE_Y, scaled_value)
    print(f"Pitch set to {value}")

def set_roll(j, value):
    """Set the roll axis. Value should be between -1 and 1."""
    scaled_value = int((value + 1) * 0x4000)
    j.set_axis(pyvjoy.HID_USAGE_X, scaled_value)
    print(f"Roll set to {value}")

def set_throttle(j, value):
    """Set the throttle axis. Value should be between 0 and 1."""
    scaled_value = int(value * 0x8000)
    j.set_axis(pyvjoy.HID_USAGE_Z, scaled_value)
    print(f"Throttle set to {value}")

def main():
    if not check_vjoy_installation():
        return

    j = pyvjoy.VJoyDevice(1)
    set_pitch(j, 0)
    set_roll(j, 0)

    # Test all axes with example values
    set_pitch(j, 0.5)
    time.sleep(1)
    set_pitch(j, -0.5)
    time.sleep(1)

    set_roll(j, 0.5)
    time.sleep(1)
    set_roll(j, -0.5)
    time.sleep(1)

    
    set_pitch(j, 0)
    set_roll(j, 0)

if __name__ == "__main__":
    time.sleep(5)
    main()

