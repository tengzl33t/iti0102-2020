"""Ebanij robot."""
from PiBot import PiBot

robot = PiBot()

last_sensor_num = robot.get_line_sensors()
# Drive towards object
while robot.get_rotation() != 180:
    robot.set_left_wheel_speed(9)
    robot.sleep(0.05)

robot.set_left_wheel_speed(0)
robot.set_wheels_speed(-50)

while last_sensor_num[-1] > 200:
    last_sensor_num = robot.get_line_sensors()
    robot.sleep(0.1)

robot.set_wheels_speed(2)
robot.sleep(2)
robot.set_wheels_speed(0)
