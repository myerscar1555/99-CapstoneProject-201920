"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Nasser Hegar.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import m3_extra as m3
from tkinter import *


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("Robot Rattata, Winter 2018-19")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root,padding=10,borderwidth=5,relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    #teleop_frame,arm_frame,control_frame,sensor_frame,soundsystem_frame,color_frame,infrared_frame = get_shared_frames(main_frame, mqtt_sender)
    #infrared_frame = build_infrared_frame(main_frame,mqtt_sender)
    final_frame = shared_gui.build_rattata(main_frame,mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    #grid_shared_frames(teleop_frame,arm_frame,control_frame,sensor_frame,soundsystem_frame,color_frame,infrared_frame)
    #grid_my_frames()
    grid_final_frame(final_frame)


    filename = PhotoImage(file='C:\\Users\\hegarnn\\Desktop\\rattata.png')
    rattata_img = ttk.Label(main_frame,image=filename)
    rattata_img.grid(row=0,column=2)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

#gets the frames we worked on in class and puts them into variables that are returned
def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_arm = shared_gui.get_control_frame(main_frame,mqtt_sender)
    sensor_frame = shared_gui.get_sensor_frame(main_frame,mqtt_sender)
    soundsystem_frame = shared_gui.get_soundsystem_frame(main_frame,mqtt_sender)
    color_frame = shared_gui.get_color_sensor_frame(main_frame,mqtt_sender)
    infrared_frame = shared_gui.get_infrared_proximity_sensor_frame(main_frame,mqtt_sender)

    return teleop_frame,arm_frame,control_arm,sensor_frame,soundsystem_frame,color_frame,infrared_frame

#grids the frames we worked on together in class
def grid_shared_frames(teleop_frame, arm_frame, control_frame,sensor_frame, soundsystem_frame,color_frame, infrared_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    sensor_frame.grid(row=3,column=0)
    soundsystem_frame.grid(row=4,column=0)
    color_frame.grid(row=0, column=1)
    infrared_frame.grid(row=1, column=1)

def grid_final_frame(final_frame):
    final_frame.grid(row=0,column=0)

#grids the frames for feature 9
def grid_my_frames(infrared_frame):
    infrared_frame.grid(row=0,column=0)

#builds the frame for feature 9
def build_infrared_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Infrared Sensor")
    #search_for_object  = ttk.Button(frame, text="search for object")
    get_object = ttk.Button(frame, text="Pick up object in front")
    search_for_object = ttk.Button(frame, text="search for object within range")
    speed_label = ttk.Label(frame, text="Robot Speed")
    speed_entry = ttk.Entry(frame,width=8)
    delta_entry = ttk.Entry(frame, width=8)
    distance_entry = ttk.Entry(frame,width=8)

    # Grid the widgets:
    frame_label.grid(row=0,column=1)
    #search_for_object.grid(row=2, column=0)
    get_object.grid(row=3,column=0)
    search_for_object.grid(row=2, column=2)
    speed_label.grid(row=4,column=1)
    distance_entry.grid(row=1,column=0)
    delta_entry.grid(row=1,column=2)
    speed_entry.grid(row=3,column=1)


    # Set the Button callbacks:
    get_object["command"] = lambda: \
        handle_pick_up_object(mqtt_sender,distance_entry,speed_entry)
    #search_for_object["command"] = lambda: \
    #    shared_gui.handle_go_forward_until_distance_is_less_than(mqtt_sender,distance_entry,speed_entry)
    search_for_object["command"] = lambda: \
        handle_search_for_object(mqtt_sender, delta_entry, speed_entry)

    return frame


#Gets the frame for rattata for the final project
def rattata_frame(main_frame,mqtt_sender):
    final_frame = shared_gui.build_rattata(main_frame,mqtt_sender)


'''
handlers for feature 9
'''
def handle_pick_up_object(mqtt_sender,distance_entry,speed_entry):
    mqtt_sender.send_message('pick_up_object',
                             [distance_entry.get(),speed_entry.get()])

def handle_search_for_object(mqtt_sender,delta_entry,speed_entry):
    mqtt_sender.send_message('search_for_object', [delta_entry.get(),speed_entry.get()])









# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()