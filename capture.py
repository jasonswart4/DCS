import mss
import numpy as np
import cv2

def capture_screen(region=None):
    with mss.mss() as sct:
        monitor = sct.monitors[1] if region is None else region
        img = np.array(sct.grab(monitor))
        return img[:, :, :3]  # Drop alpha channel

def show_screen():
    while True:
        frame = capture_screen()
        cv2.imshow('Screen', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_screen()
