import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import time
import shared_gui_delegate_on_robot
import rosebot

# -------------------------------------------------------------------------
# Construct and connect the MQTT Client:
# -------------------------------------------------------------------------
mqtt_sender = com.MqttClient()
mqtt_sender.connect_to_ev3()


def growl(mqtt_sender):
    shared_gui.handle_phrase(mqtt_sender,"Roar. Be Afraid")

def quick_attack(mqtt_sender):
    shared_gui.handle_go_forward_until_distance_is_less_than(mqtt_sender,10,100)
    shared_gui.handle_backward(-100,-100,mqtt_sender)
    time.sleep(2)
    shared_gui.handle_stop(mqtt_sender)

def tackle(mqtt_sender):
    shared_gui.handle_go_forward_until_distance_is_less_than(mqtt_sender,5,50)
    shared_gui.handle_backward(-50, -50, mqtt_sender)
    time.sleep(2)
    shared_gui.handle_stop(mqtt_sender)

def defense_curl(mqtt_sender):
    shared_gui.handle_forward(100,100,mqtt_sender)


def scratch(mqtt_sender):
    shared_gui.handle_raise_arm(mqtt_sender)
    shared_gui.handle_lower_arm(mqtt_sender)

