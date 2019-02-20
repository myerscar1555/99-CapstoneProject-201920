# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

def stack_blocks(self, speed):
    while True:
        distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if distance < 60:
            self.robot.drive_system.go(int(speed), int(speed))
            print(distance)
            if distance < int(14):
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                self.robot.arm_and_claw.lower_arm()
                break
        else:
            self.robot.drive_system.left_motor.turn_on(50)
            self.robot.drive_system.right_motor.turn_on(-50)

def follow_eva(self, speed, distance):
    while True:
        ir_distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if ir_distance > distance:
            self.robot.sound_system.speech_maker.speak("EVA")
            self.robot.drive_system.go(int(speed), int(speed))
            if ir_distance < distance:
                self.robot.drive_system.stop()

def recycle(self):
    while True:
        distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if distance < 60:
            self.robot.drive_system.go(50, 50)
            print(distance)
            if distance < int(14):
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                self.robot.drive_system.go(50, -50)
                time.sleep(1)
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.lower_arm()
                break
        else:
            self.robot.drive_system.left_motor.turn_on(50)
            self.robot.drive_system.right_motor.turn_on(-50)




def walle_fun(self, speed):
        self.robot.drive_system.go_for_inches(12, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1)
        self.robot.drive_system.go_for_inches(12, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1)
        self.robot.drive_system.go_for_inches(12, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1)
        self.robot.drive_system.go_for_inches(12, int(speed))
        self.robot.drive_system.go(50, -50)
        time.sleep(1)
        self.robot.drive_system.stop()




def run_and_hid(self):
    while True:
        distance = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if distance < 10:
            self.robot.sound_system.speech_maker.speak("NO, LEAVE ME BE. I mean WALL E")
            self.robot.drive_system.go(-100, -100)
            self.robot.drive_system.go(-25, 25)
            time.sleep(2)
            self.robot.drive_system.go(100, 100)
            time.sleep(.5)
            self.robot.drive_system.go(-50, 50)
            time.sleep(1)
            self.robot.drive_system.go(100, 100)
            time.sleep(1)
            self.robot.drive_system.stop()


