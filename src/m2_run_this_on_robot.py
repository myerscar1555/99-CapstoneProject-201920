"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Michael Johnson.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as dingding


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    big_boy_robot_code()

def big_boy_robot_code():
    robot = rosebot.RoseBot()
    delegate_that_recieves = dingding.DelegateThatRecieves(robot)
    mqtt_reciever = com.MqttClient(delegate_that_recieves)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(0.01)

def proximity_frequency(self, frequency, duration, rate):

    while True:
        rosebot.ToneMaker.play_tone(self, (frequency * rate), duration)
        if rosebot.InfraredProximitySensor.get_distance_in_inches(self) < .5:
            break




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()