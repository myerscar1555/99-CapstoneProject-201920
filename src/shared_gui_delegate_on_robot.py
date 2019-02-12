"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Michael Johnson, Carter Meyers, Nasser Hegar.
  Winter term, 2018-2019.
"""


class DelegateThatRecieves(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot

        #  self.is_time_to_stop

    def forward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed),
                                   int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go((-1 * int(left_wheel_speed)), (-1 * int(right_wheel_speed)))

    def right(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), -1 * int(right_wheel_speed))

    def left(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(- 1 * int(left_wheel_speed), int(right_wheel_speed))

    def stop(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))


    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, desired_arm_position):
        self.robot.arm_and_claw.move_arm_to_position(int(desired_arm_position))

    def go_straight_for_inches_using_time(self, time, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(time, speed)

    def go_straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches, speed)


    #  def quit(self):
    #     print("got quit")
    #   handle_quit()
