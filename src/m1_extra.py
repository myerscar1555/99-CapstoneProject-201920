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
    root.title("Personal Project, Winter 2018-19")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root,padding=10,borderwidth=5,relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    knock_off_frame,meow_at_door_frame,ask_for_food_frame,petting_frame,follow_mouse_frame,teleop_frame,arm_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_shared_frames(knock_off_frame,meow_at_door_frame,ask_for_food_frame,petting_frame,follow_mouse_frame,teleop_frame,arm_frame)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()


def get_shared_frames(window, mqtt_sender):
    knock_off_frame = shared_gui.get_knock_off_frame(window, mqtt_sender)
    meow_at_door_frame = shared_gui.get_meow_at_door_frame(window, mqtt_sender)
    ask_for_food_frame = shared_gui.get_ask_for_food_frame(window, mqtt_sender)
    petting_frame = shared_gui.get_petting_frame(window, mqtt_sender)
    follow_mouse_frame = shared_gui.get_follow_mouse_frame(window, mqtt_sender)
    teleop_frame = shared_gui.get_teleoperation_frame(window, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(window, mqtt_sender)
    return knock_off_frame, meow_at_door_frame, ask_for_food_frame, petting_frame, follow_mouse_frame,teleop_frame,arm_frame

def grid_shared_frames(knock_off_frame, meow_at_door_frame, ask_for_food_frame, petting_frame, follow_mouse_frame, teleop_frame, arm_frame):
    knock_off_frame.grid(row=1, column=0)
    meow_at_door_frame.grid(row=2, column=1)
    ask_for_food_frame.grid(row=3, column=0)
    petting_frame.grid(row=4, column=1)
    follow_mouse_frame.grid(row=5, column=0)
    teleop_frame.grid(row=6,column=1)
    arm_frame.grid(row=6, column=0)

main()