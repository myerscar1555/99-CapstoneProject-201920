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
        self.robot.drive_system.go_straight_for_inches_using_time(int(time), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def beep(self, number_of_beeps):
        for k in range(int(number_of_beeps)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self,frequency, duration):
        self.robot.sound_system.tone_maker.play_tone(int(frequency), int(duration)).wait()

    def tone_sequence(self, tones):
        self.robot.sound_system.tone_maker.play_tone_sequence(int(tones)).wait()

    def speak(self, phrase):
        self.robot.sound_system.speech_maker.speak(phrase).wait()

    def spin_clockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, area)

    def spin_counterclockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)

    def find_color(self, color):

        self.robot.drive_system.go_straight_until_color_is(color,20)

    def follow_color(self,color):
        #self.robot.go(20)
        self.robot.drive_system.go_straight_until_color_is_not(color,20)

    def find_intensity(self,intensity):
        #self.robot.go(20)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity),20)

    def go_backward_until_distance_is_greater_than(self, distance, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(distance,speed)

    def go_forward_until_distance_is_less_than(self, distance, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(distance),int(speed))

    def go_until_distance_is_within(self, distance, speed):
        self.go_until_distance_is_within(distance,speed)

    def beep_according_to_distance(self, beep_rate, beep_rate_increase):
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 48:
                self.robot.drive_system.go(50, 50)
                self.robot.sound_system.beeper.beep().wait(beep_rate / (distance * beep_rate_increase))
                if distance < 2:
                    self.robot.drive_system.stop()
                    break
            else:
                self.robot.drive_system.left_motor.turn_on(50)
                self.robot.drive_system.right_motor.turn_on(-50)

    #  def quit(self):
    #    print("got quit")
    #   handle_quit()
