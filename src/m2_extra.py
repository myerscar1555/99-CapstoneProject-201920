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
    teleop_frame, stack_frame, follow_frame, recycle_frame, fun_frame, scared_frame = get_shared_frames(main_frame, mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, stack_frame, follow_frame, recycle_frame, fun_frame, scared_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

# This is all of my self-made frames, where it creates them, grids them, and has the handler for sending data to the mqtt

def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    stack_frame = trash_stack(main_frame, mqtt_sender)
    follow_frame = Follow_Eva(main_frame, mqtt_sender)
    recycle_frame = recycle(main_frame, mqtt_sender)
    fun_frame = bored_WallE(main_frame, mqtt_sender)
    scared_frame = run_and_hide(main_frame, mqtt_sender)

    return (teleop_frame, stack_frame, follow_frame, recycle_frame, fun_frame, scared_frame)


def trash_stack(main_frame,mqtt_sender):
    frame = ttk.Frame(main_frame, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Trash Moving")
    stack_blocks = ttk.Button(frame, text="Move the trash to another spot")
    speed_label = ttk.Label(frame, text='Speed of Wall-E')
    speed_entry = ttk.Entry(frame, width=8)


    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    stack_blocks.grid(row=2, column=0)
    speed_label.grid(row=6, column=0)
    speed_entry.grid(row=6, column=1)


    # Set the Button callbacks:
    stack_blocks["command"] = lambda: handle_stack_blocks(mqtt_sender, speed_entry)

    return frame


def handle_stack_blocks(mqtt_sender,speed_entry):
    print("Wall-E will move blocks at speed", speed_entry.get())
    mqtt_sender.send_message('stack_blocks', [speed_entry.get()])



def Follow_Eva(main_frame,mqtt_sender):
    frame = ttk.Frame(main_frame, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Follow Eva")
    follow_eva = ttk.Button(frame, text="Follow Eva")
    speed_label = ttk.Label(frame, text='Speed of Wall-E')
    speed_entry = ttk.Entry(frame, width=8)
    distance_label = ttk.Label(frame, text='Distance that Wall-E will follow (inches)')
    distance_entry = ttk.Entry(frame, width=8)


    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    follow_eva.grid(row=2, column=0)
    speed_label.grid(row=6, column=0)
    speed_entry.grid(row=6, column=1)
    distance_label.grid(row=7, column=0)
    distance_entry.grid(row=7, column=1)


    # Set the Button callbacks:
    follow_eva["command"] = lambda: handle_follow_eva(mqtt_sender, speed_entry, distance_entry)

    return frame


def handle_follow_eva(mqtt_sender,speed_entry, distance_entry):
    print("Wall-E will follow Eva at speed", speed_entry.get(), "and distance", distance_entry.get())
    mqtt_sender.send_message('follow_eva', [speed_entry.get(), distance_entry.get()])


def recycle(main_frame,mqtt_sender):
    frame = ttk.Frame(main_frame, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Recycle Time")
    recycle_button = ttk.Button(frame, text="Recycle or Throw away")


    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    recycle_button.grid(row=2, column=0)


    # Set the Button callbacks:
    recycle_button["command"] = lambda: handle_recycle(mqtt_sender)

    return frame


def handle_recycle(mqtt_sender):
    print("Wall-E will now recycle or throw away objects")
    mqtt_sender.send_message('recycle')


def bored_WallE(main_frame,mqtt_sender):
    frame = ttk.Frame(main_frame, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Wall-E is bored")
    fun_button = ttk.Button(frame, text="Give Wall-E something to do")
    fun_slider = tkinter.Scale(frame, orient='horizontal')
    fun_label = ttk.Label(frame, text="Wall-E speed")



    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    fun_button.grid(row=3, column=0)
    fun_slider.grid(row=2, column=1)
    fun_label.grid(row=2, column=0)
    fun_slider.set(50)



    # Set the Button callbacks:
    fun_button["command"] = lambda: handle_fun(mqtt_sender, fun_slider.get())

    return frame


def handle_fun(mqtt_sender, fun_slider):
    print("Wall-E will now make his own fun")
    mqtt_sender.send_message('walle_fun', [fun_slider])


def run_and_hide(main_frame,mqtt_sender):
    frame = ttk.Frame(main_frame, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Wall-E is scared")
    scared_button = ttk.Button(frame, text="Make Wall-E run and hide")



    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    scared_button.grid(row=3, column=0)



    # Set the Button callbacks:
    scared_button["command"] = lambda: handle_scared(mqtt_sender)

    return frame


def handle_scared(mqtt_sender):
    print("Wall-E will now run and hide")
    mqtt_sender.send_message('run_and_hide')

def grid_frames(teleop_frame, stack_frame, follow_frame, recycle_frame, fun_frame, scared_frame):
    teleop_frame.grid(row=0,column=0)
    stack_frame.grid(row=1, column=0)
    follow_frame.grid(row=0, column=1)
    recycle_frame.grid(row=1, column=1)
    fun_frame.grid(row=0, column=2)
    scared_frame.grid(row=1, column=2)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()