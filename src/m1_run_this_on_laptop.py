"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Carter Myers.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


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
    root.title("Robot Boi, Winter 2018-19")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root,padding=10,borderwidth=5,relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame,arm_frame,control_frame,sensor_frame,soundsystem_frame,color_frame,infrared_proximity_sensor_frame,camera_frame = get_shared_frames(main_frame, mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_shared_frames(teleop_frame,arm_frame,control_frame,sensor_frame,soundsystem_frame,color_frame,infrared_proximity_sensor_frame,camera_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()






def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_arm = shared_gui.get_control_frame(main_frame,mqtt_sender)
    sensor_frame = shared_gui.get_sensor_frame(main_frame,mqtt_sender)
    soundsystem_frame = shared_gui.get_soundsystem_frame(main_frame,mqtt_sender)
    color_frame = shared_gui.get_color_sensor_frame(main_frame,mqtt_sender)
    infrared_proximity_sensor_frame = shared_gui.get_infrared_proximity_sensor_frame(main_frame, mqtt_sender)
    m1_personal_infrared_frame = get_m1_personal_infrared_frame(main_frame, mqtt_sender)
    camera_frame = shared_gui.get_camera_frame(main_frame, mqtt_sender)

    return teleop_frame,arm_frame,control_arm,sensor_frame,soundsystem_frame,color_frame,infrared_proximity_sensor_frame,camera_frame


def grid_shared_frames(teleop_frame, arm_frame, control_frame,sensor_frame, soundsystem_frame,color_frame,infrared_proximity_sensor_frame, camera_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    sensor_frame.grid(row=3,column=0)
    soundsystem_frame.grid(row=4,column=0)
    color_frame.grid(row=0, column=1)
    infrared_proximity_sensor_frame.grid(row=1, column=1)
    camera_frame.grid(row=2, column=1)

def get_m1_personal_infrared_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="m1 Personal")
    beep_according_to_distance = ttk.Button(frame, text="Beeps at rate based on how far from object")
    beep_label = ttk.Label(frame, text="Initial Beep Speed")
    beep_entry = ttk.Entry(frame, width=8)
    rate_label = ttk.Label(frame, text="Rate of Increase")
    rate_entry = ttk.Entry(frame, width=8)

    # Grid the widgets:
    frame_label.grid(row=1, column=1)
    beep_according_to_distance.grid(row=2, column=0)
    beep_label.grid(row=4, column=1)
    rate_entry.grid(row=3, column=2)
    rate_label.grid(row=4, column=2)
    beep_entry.grid(row=3, column=1)

    # Set the Button callbacks:
    beep_according_to_distance["command"] = lambda: handle_beep_according_to_distance(mqtt_sender, beep_entry, rate_entry)

    return frame

def handle_beep_according_to_distance(mqtt_sender, beep_entry, rate_entry):
    print("Will beep at: ", beep_entry.get())
    mqtt_sender.send_message('beep_according_to_distance', [beep_entry.get(), rate_entry.get()])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()