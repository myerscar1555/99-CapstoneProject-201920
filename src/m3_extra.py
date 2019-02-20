import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui

# -------------------------------------------------------------------------
# Construct and connect the MQTT Client:
# -------------------------------------------------------------------------
mqtt_sender = com.MqttClient()
mqtt_sender.connect_to_ev3()


def growl(mqtt_sender,phrase):
    shared_gui.handle_phrase(mqtt_sender,"Roar. Be Afraid")

def quick_attack(mqtt_sender,distance_entry):
    shared_gui.h
    pass

def tackle():
    pass

def defense_curl():
    shared_gui.handle
    pass

def scratch():
    pass