from capture import capture_screen
from control import unpause_game, test_controls
import cv2

def main():
    unpause_game()
    test_controls()

    # Uncomment the following lines for continuous screen capture and control
    # while True:
    #     frame = capture_screen()
    #     # basic_control()  # Replace with rule_based_control(frame) for rule-based control
    #     cv2.imshow('Screen', frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()