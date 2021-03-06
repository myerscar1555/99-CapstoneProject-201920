"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Michael Johnson, Carter Meyers, Nasser Hegar.
  Winter term, 2018-2019.
"""
import time
import rosebot

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

    def go_straight_for_inches_using_time(self, seconds, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(int(seconds), int(speed))

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

    def spin_clockwise_until_sees_object(self, speed):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed))

    def spin_counterclockwise_until_sees_object(self, speed):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed))

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
        self.robot.drive_system.go_forward_until_distance_is_less_than(distance, speed)

    def go_until_distance_is_within(self, distance, speed):
        self.go_until_distance_is_within(distance,speed)

    def beep_according_to_distance(self, beep_rate, beep_rate_increase):
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 60:
                self.robot.drive_system.go(50, 50)
                self.robot.sound_system.beeper.beep()
                time.sleep(int(beep_rate) / ((60 - int(distance)) * int(beep_rate_increase)))
                if distance < 4:
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    self.robot.arm_and_claw.lower_arm()
                    break
            else:
                self.robot.drive_system.left_motor.turn_on(50)
                self.robot.drive_system.right_motor.turn_on(-50)

    def tone_until_distance_is_less_than(self, distance_entry, speed_entry, frequency_entry, rate_entry):
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 60:
                self.robot.drive_system.go(int(speed_entry), int(speed_entry))
                print(distance)
                self.robot.sound_system.tone_maker.play_tone(int(frequency_entry) + ((60 - int(distance))*int(rate_entry)), 500).wait()
                if distance < int(distance_entry):
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    self.robot.arm_and_claw.lower_arm()
                    break
            else:
                self.robot.drive_system.left_motor.turn_on(50)
                self.robot.drive_system.right_motor.turn_on(-50)

    def pick_up_object(self, distance_entry, speed_entry):
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            self.robot.drive_system.go(int(speed_entry),int(speed_entry))
            blink_rate = .1
            blink_rate_increase = .05

            if distance < 80:

                self.robot.led_system.left_led.turn_on()
                self.robot.led_system.left_led.turn_off()
                time.sleep((blink_rate) / (80 - int(distance)) * blink_rate_increase )
                self.robot.led_system.right_led.turn_on()
                self.robot.led_system.right_led.turn_off()
                print(distance)
                if distance < int(distance_entry):
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    self.robot.arm_and_claw.lower_arm()
                    break

    def search_for_object(self,delta_entry,speed_entry):
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < int(delta_entry):
                self.robot.sound_system.speech_maker.speak("I found alpha")
                self.robot.drive_system.stop()
                break
            else:
                self.robot.drive_system.left_motor.turn_on(int(speed_entry))
                self.robot.drive_system.right_motor.turn_on(-int(speed_entry))

    #    print("got quit")
    #   handle_quit()

###############################################################################
# Robot drives forward and knocks off a number of objects as specified by the
# User in the GUI and can vary its force by a slider in the GUI
###############################################################################
    def knock_off_object(self, aggression_slider, number_entry):
        while True:
            for k in range(int(number_entry)):
                self.robot.drive_system.go_straight_for_inches_using_encoder(12, 50)
                self.robot.drive_system.go(-50 - (int(aggression_slider) * 50), 50 + (int(aggression_slider) * 50))
                time.sleep(6)
            self.robot.stop()
            break

###############################################################################
# Robot drives up to the door and meows to be let in. Won't stop until the door
# is open.
###############################################################################
    def meow_at_door(self, number_entry):
        self.robot.drive_system.go(100, 100)
        count = 0
        num = 0
        times = 0
        while True:
            count = count + 50
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance <= 20:
                num = num + 1
                self.robot.drive_system.stop()
                self.robot.sound_system.tone_maker.play_tone(1000 + count, 1000)
                if count >= 1000:
                    count = 0
            elif num != 0:
                self.robot.drive_system.go_straight_for_inches_using_encoder(44, 100)
                self.robot.drive_system.go(50, -50)
                time.sleep(3)
                self.robot.drive_system.stop()
                times = times + 1
                num = 0
                if times == int(number_entry):
                    break

###############################################################################
# Robot picks up bowl, and brings it to the user and asks for food
###############################################################################
    def ask_for_food(self):
        count = 0
        self.robot.arm_and_claw.raise_arm()
        self.robot.drive_system.go(-50, 50)
        time.sleep(3)
        self.robot.drive_system.stop()
        self.robot.drive_system.go_straight_for_inches_using_encoder(48, 100)
        while True:
            self.robot.sound_system.speech_maker.speak("Brother may I have some oats")
            count = count + 1
            if count >= 1:
                break

###############################################################################
# Robot lets you pet it a certain number of times before running away. The
# number of times is specified by the user in the GUI
###############################################################################
    def get_pet(self, number_entry):
        count = 0
        while True:
            if self.robot.sensor_system.touch_sensor.is_pressed() == True:
                self.robot.sound_system.speech_maker.speak("Thank you sir")
                count = count + 1
                if count >= int(number_entry):
                    self.robot.drive_system.go(-100, -100)
                    time.sleep(3)
                    self.robot.drive_system.stop()
                    break

###############################################################################
# Robot catches a mouse by using the camera to identify it
###############################################################################
    def follow_mouse(self):
        while True:
            b = self.robot.sensor_system.camera.get_biggest_blob()
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if (b.width * b.height) >= 25:
                self.robot.drive_system.go(100, 100)
                if distance <= 5:
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    self.robot.arm_and_claw.lower_arm()
                    break

    #The robot turns and searches for an enemy to attack within a range, in inches, that the user has decided
    def search_for_enemy(self, distance_entry):
        distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        while ( distance > distance_entry):
            self.robot.drive_system.go(30, -30)
            time.sleep(.5)
            self.robot.drive_system.stop()
            time.sleep(.2)
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        self.robot.sound_system.speech_maker.speak("Rattata found an enemy")

    #The robot growls at it's enemy in order to intimidate them and have their attack lowered
    def growl(self):
        self.robot.sound_system.speech_maker.speak("Growl. Be Afraid")
        self.robot.sound_system.speech_maker.speak("The enemy's attack has been lowered")

    #The robot charges quickly at it's enemy to deal damage to them. Afterwards the robot backs off ready to attack again
    def quick_attack(self,scale_entry):
        self.robot.drive_system.go_forward_until_distance_is_less_than(10,scale_entry)
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 10:
            self.robot.sound_system.speech_maker.speak("Rattata missed!")
        else:
            self.robot.sound_system.speech_maker.speak("Rattata dealt 10 damage!")
        self.robot.drive_system.go_backward_until_distance_is_greater_than(70,100)

    #The robot spins for however long the user tells it to so that it's defense increases
    def defense_curl(self,curl_entry):
        self.robot.drive_system.go(100,-100)
        time.sleep(curl_entry)
        self.robot.drive_system.stop()
        self.robot.sound_system.speech_maker.speak("Rattata's defense increased")

    #A common move in Pokemon is scratch. Rattata learns this move and will scratch the enemy in front of them with his claw
    def scratch(self, scratches_entry):
        self.robot.drive_system.go_forward_until_distance_is_less_than(10,50)
        for _ in range(scratches_entry):
            self.robot.arm_and_claw.raise_arm()
            self.robot.arm_and_claw.lower_arm()
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 10:
            self.robot.sound_system.speech_maker.speak("Rattata missed!")
        else:
            self.robot.sound_system.speech_maker.speak("Rattata dealt " + str(5* scratches_entry) + " damage! It's not very effective")

# This code will pick up a block, move the block 12 inches in front of Wall-E then lay the bock back down

    def stack_blocks(self, speed):
        while True:

            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 60:
                self.robot.drive_system.go(int(speed), int(speed))
                print(distance)
                if distance < int(7):
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    self.go_straight_for_inches_using_encoder(12, int(speed))
                    self.robot.arm_and_claw.lower_arm()
                    break
            else:
                self.robot.drive_system.left_motor.turn_on(50)
                self.robot.drive_system.right_motor.turn_on(-50)


# This code makes it so that Wall-E will follow Eva until he gets too close and stops.
    def follow_eva(self, speed, distance):
        while True:
            ir_distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if round(ir_distance) > int(distance):
                self.robot.sound_system.speech_maker.speak("eva")
                self.robot.drive_system.go(int(speed), int(speed))
                if round(ir_distance) <= int(distance):
                    self.robot.drive_system.stop()
                    break

# This code makes it so that the robot will now pick up a block, turn around about 90 degrees
    # and then it will lay the block down in the 'recycling' pile

    def recycle(self):
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 60:
                self.robot.drive_system.go(50, 50)
                print(distance)
                if distance < int(7):
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    self.robot.drive_system.go(50, -50)
                    time.sleep(2)
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.lower_arm()
                    break
            else:
                self.robot.drive_system.left_motor.turn_on(50)
                self.robot.drive_system.right_motor.turn_on(-50)


# This code will give Wall-E something fun to do, in this case it will make him run in a square

    def walle_fun(self, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(24, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1.5)
        self.robot.drive_system.go_straight_for_inches_using_encoder(24, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1.5)
        self.robot.drive_system.go_straight_for_inches_using_encoder(24, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1.5)
        self.robot.drive_system.go_straight_for_inches_using_encoder(24, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1.5)
        self.robot.drive_system.stop()

# The run and hide code will make Wall-E get scared when he sees something too close,
    # run backwards, go to the side, then go further back
    def run_and_hide(self):
        while True:
            distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if distance < 10:
                self.robot.sound_system.speech_maker.speak("NO, LEAVE ME BE")
                self.robot.drive_system.go(-100, -100)
                time.sleep(5)
                self.robot.drive_system.go(-50, 50)
                time.sleep(1.5)
                self.robot.drive_system.go(100, 100)
                time.sleep(2)
                self.robot.drive_system.go(-50, 50)
                time.sleep(1.5)
                self.robot.drive_system.go(100, 100)
                time.sleep(5)
                self.robot.drive_system.stop()
                break


