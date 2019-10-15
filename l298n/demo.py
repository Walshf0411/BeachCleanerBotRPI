from l298n import l298n
import time

def main():
    pin1 = 24
    pin2 = 25
    pin3 = 8
    pin4 = 7
    motor = l298n(pin1, pin2, pin3, pin4)

    time.sleep(1)
    motor.start()
    motor.move_backward()
    motor.move_left()
    motor.move_forward()
    motor.move_right()
    motor.move_forward()
    motor.stop()

main()
