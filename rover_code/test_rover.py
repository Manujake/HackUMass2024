#test_rover.py

import time
import rover_control as rover

try:
    # Move forward for 2 seconds
    rover.move_forward(80)
    time.sleep(2)
    rover.stop()
    time.sleep(1)

    # Turn right for 1.5 seconds
    rover.turn_right(60)
    time.sleep(1.5)
    rover.stop()
    time.sleep(1)

    # Move backward for 2 seconds
    rover.move_backward(80)
    time.sleep(2)
    rover.stop()
    time.sleep(1)

    # Turn left for 1.5 seconds
    rover.turn_left(60)
    time.sleep(1.5)
    rover.stop()

except KeyboardInterrupt:
    print("Interrupted by User")

finally:
    rover.cleanup()

