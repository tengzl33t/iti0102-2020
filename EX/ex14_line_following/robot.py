"""Ebanij robot."""
from PiBot import PiBot

robot = PiBot()

while robot.get_third_line_sensor_from_right() < 300 and robot.get_third_line_sensor_from_left() < 300:
    robot.set_wheels_speed(10)
    robot.sleep(0.05)

    if robot.get_second_line_sensor_from_right() > 0:
        robot.set_left_wheel_speed(2)
        robot.sleep(0.05)
        robot.set_left_wheel_speed(0)

    if robot.get_second_line_sensor_from_left() > 0:
        robot.set_right_wheel_speed(2)
        robot.sleep(0.05)
        robot.set_right_wheel_speed(0)


robot.set_wheels_speed(0)
robot.done()
