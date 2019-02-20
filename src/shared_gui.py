"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Michael Johnson, Carter Meyers, Nasser Hegar.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time
import m3_extra as m3



def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame

def get_color_sensor_frame(window,mqtt_sender):
    """
    Construct frame on the given window, where th frame has button objecs for which color to follow
    which intesity to follow, and an entry box for the color and intenity
    """

    #Construct frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    #Construct the widgets on the frame

    frame_label = ttk.Label(frame, text="Color Senor")
    color_label = ttk.Label(frame, text="Color")
    intensity_label = ttk.Label(frame, text="Intensity")

    color_entry_box = ttk.Entry(frame,width=8)
    intensity_entry_box = ttk.Entry(frame, width=8)

    follow_color_button = ttk.Button(frame, text="Follow Color")
    follow_intensity_button = ttk.Button(frame, text="Follow Intensity")
    find_color_button = ttk.Button(frame, text="Find Color")

    #grid widgets
    frame_label.grid(row=0, column=0)
    color_label.grid(row=1, column=0)
    intensity_label.grid(row=1, column=3)

    color_entry_box.grid(row=1, column=2)
    intensity_entry_box.grid(row=1, column=4)

    follow_color_button.grid(row=2, column=2)
    follow_intensity_button.grid(row=2,column=4)
    find_color_button.grid(row=3,column=2)

    #set button callbacks
    follow_color_button["command"] = lambda: handle_follow_color(mqtt_sender, color_entry_box)
    follow_intensity_button["command"] = lambda: handle_follow_intensity(mqtt_sender, intensity_entry_box)
    find_color_button["command"] = lambda: handle_find_color(mqtt_sender, color_entry_box)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_sensor_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sensors")
    time_sensor = ttk.Button(frame, text="Amount of time robot moves(s)")
    distance_sensor = ttk.Button(frame, text="Distance robot moves(in)")
    speed_label = ttk.Label(frame, text="Robot Speed")
    speed_entry = ttk.Entry(frame,width=8)
    time_entry = ttk.Entry(frame, width=8)
    distance_entry = ttk.Entry(frame,width=8)

    # Grid the widgets:
    frame_label.grid(row=0,column=1)
    time_sensor.grid(row=2, column=0)
    distance_sensor.grid(row=2,column=2)
    speed_label.grid(row=4,column=1)
    time_entry.grid(row=1,column=0)
    distance_entry.grid(row=1,column=2)
    speed_entry.grid(row=3,column=1)


    # Set the Button callbacks:
    time_sensor["command"] = lambda: handle_time(mqtt_sender,time_entry,speed_entry)
    distance_sensor["command"] = lambda: handle_inches(mqtt_sender,distance_entry,speed_entry)

    return frame

def get_infrared_proximity_sensor_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Infrared Sensor")
    go_forward_until_distance_is_less_than = ttk.Button(frame, text="Goes until robot is close")
    go_backward_until_distance_is_greater_than = ttk.Button(frame, text="Goes back until robot is far away.")
    go_until_distance_is_within = ttk.Button(frame, text="Goes until robot is within given range of object.")
    speed_label = ttk.Label(frame, text="Robot Speed")
    speed_entry = ttk.Entry(frame,width=8)
    delta_entry = ttk.Entry(frame, width=8)
    distance_entry = ttk.Entry(frame,width=8)

    # Grid the widgets:
    frame_label.grid(row=0,column=1)
    go_forward_until_distance_is_less_than.grid(row=2, column=0)
    go_backward_until_distance_is_greater_than.grid(row=3,column=0)
    go_until_distance_is_within.grid(row=2, column=2)
    speed_label.grid(row=4,column=1)
    distance_entry.grid(row=1,column=0)
    delta_entry.grid(row=1,column=2)
    speed_entry.grid(row=3,column=1)


    # Set the Button callbacks:
    go_backward_until_distance_is_greater_than["command"] = lambda: \
        handle_go_backward_until_distance_is_greater_than(mqtt_sender,distance_entry,speed_entry)
    go_forward_until_distance_is_less_than["command"] = lambda: \
        handle_go_forward_until_distance_is_less_than(mqtt_sender,distance_entry,speed_entry)
    go_until_distance_is_within["command"] = lambda: \
        handle_go_until_distance_is_within(mqtt_sender, delta_entry, distance_entry, speed_entry)

    return frame

def get_soundsystem_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    #Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="SoundSystem")
    beep_label = ttk.Button(frame, text="Number of beeps")
    tone_label = ttk.Button(frame, text="Tone Frequency")
    phrase_label = ttk.Button(frame, text="Phrase")
    beep_entry = ttk.Entry(frame,width=8)
    tone_entry = ttk.Entry(frame,width=8)
    phrase_entry = ttk.Entry(frame,width=10)

    #Grid the widgets:
    frame_label.grid(row=0,column=1)
    beep_label.grid(row=2, column=1)
    tone_label.grid(row=2,column=3)
    phrase_label.grid(row=4,column=2)
    beep_entry.grid(row=1, column=1)
    tone_entry.grid(row=1,column=3)
    phrase_entry.grid(row=3,column=2)

    #Set the button callbacks:
    beep_label["command"] = lambda: handle_number_of_beeps(mqtt_sender, beep_entry)
    tone_label["command"] = lambda: handle_frequency(mqtt_sender, tone_entry)
    phrase_label["command"] = lambda: handle_phrase(mqtt_sender, phrase_entry)


    return frame


def Drive_System(window, mqtt_sender):


    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Move With Time and Sensors")

    frame_label.grid()

    go_straight_seconds = ttk.Button(frame, text="Go Straight for Seconds")
    inches_using_time = ttk.Button(frame, text="Go Straight for inches Using time")
    inches_using_sensor = ttk.Button(frame, text="Go Straight for inches Using time")

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")
    time_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    time_entry.insert(0, "100")
    inches_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    inches_entry.insert(0, "100")

    go_straight_seconds.grid(row=0, column=0)
    inches_using_time.grid(row=1, column=1)
    inches_using_sensor.grid(row=2, column=2)

    go_straight_seconds["command"] = lambda: mqtt_sender.send_message("Straight for Seconds")


def get_camera_frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Using the Camera")

    frame_label.grid()

    counterclockwise = ttk.Button(frame, text="Turn CounterClockwise until sees object")
    clockwise = ttk.Button(frame, text="Turn Clockwise until sees object")
    m1_feature9 = ttk.Button(frame, text="m1 feature 9")
    m2_feature9 = ttk.Button(frame, text="m2 feature 9")
    m3_feature9 = ttk.Button(frame, text="m3 feature 9")

    speed_label = ttk.Label(frame, text='Enter Speed:')
    speed_entry = ttk.Entry(frame, width=8)
    speed_label.grid(row=2, column=0)
    speed_entry.grid(row=3, column=0)

    beep_label = ttk.Label(frame, text='Enter beeps:')
    beep_entry = ttk.Entry(frame, width=8)
    beep_label.grid(row=7, column=0)
    beep_entry.grid(row=8, column=0)

    rate_label = ttk.Label(frame, text='Enter rate:')
    rate_entry = ttk.Entry(frame, width=8)
    rate_label.grid(row=9, column=0)
    rate_entry.grid(row=10, column=0)

    distance_label = ttk.Label(frame, text='Enter Distance:')
    distance_entry = ttk.Entry(frame, width=8)
    distance_label.grid(row=11, column=0)
    distance_entry.grid(row=12, column=0)

    frequency_label = ttk.Label(frame, text='Enter Frequency:')
    frequency_entry = ttk.Entry(frame, width=8)
    frequency_label.grid(row=13, column=0)
    frequency_entry.grid(row=14, column=0)

    counterclockwise.grid(row=0, column=0)
    clockwise.grid(row=1, column=0)
    m1_feature9.grid(row=4, column=0)
    m2_feature9.grid(row=5,column=0)
    m3_feature9.grid(row=6,column=0)

    clockwise["command"] = lambda: handle_spin_clockwise_until_sees_object(mqtt_sender, speed_entry)
    counterclockwise["command"] = lambda: handle_search_for_object(mqtt_sender,beep_entry, speed_entry)
    m1_feature9["command"] = lambda: handle_beep_according_to_distance(mqtt_sender, beep_entry, rate_entry)
    m2_feature9["command"] = lambda: handle_tone_until_distance_is_less_than(mqtt_sender, distance_entry, speed_entry, frequency_entry, rate_entry)
    m3_feature9["command"] = lambda: handle_m3_feature_9(mqtt_sender, distance_entry, speed_entry)

    return frame

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


def handle_pick_up_object(mqtt_sender,distance_entry,speed_entry):
    mqtt_sender.send_message('pick_up_object',
                             [distance_entry.get(),speed_entry.get()])

def handle_search_for_object(mqtt_sender,delta_entry,speed_entry):
    mqtt_sender.send_message('search_for_object', [delta_entry.get(),speed_entry.get()])



def get_m2_personal_infrared_frame(main_frame,mqtt_sender):
    frame = ttk.Frame(main_frame, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Michael Personal")
    beep_according_to_distance = ttk.Button(frame, text="Frequency raises at rate based on how far from object")
    beep_label = ttk.Label(frame, text="Initial Frequency")
    frequency_entry = ttk.Entry(frame, width=8)
    rate_label = ttk.Label(frame, text="Rate of Increase (between 1 and 10)")
    rate_entry = ttk.Entry(frame, width=8)
    speed_label = ttk.Label(frame, text='Speed of robot')
    speed_entry = ttk.Entry(frame, width=8)
    distance_label = ttk.Label(frame, text='Distance to stop')
    distance_entry = ttk.Entry(frame, width=8)


    # Grid the widgets:
    frame_label.grid(row=1, column=1)
    beep_according_to_distance.grid(row=2, column=0)
    beep_label.grid(row=3, column=0)
    rate_entry.grid(row=4, column=1)
    rate_label.grid(row=4, column=0)
    frequency_entry.grid(row=3, column=1)
    speed_label.grid(row=6, column=0)
    speed_entry.grid(row=6, column=1)
    distance_label.grid(row=7, column=0)
    distance_entry.grid(row=7, column=1)

    # Set the Button callbacks:
    beep_according_to_distance["command"] = lambda: handle_tone_until_distance_is_less_than(mqtt_sender, distance_entry, speed_entry, frequency_entry, rate_entry)

    return frame

def build_rattata(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Top Percentile Rattata")
    quick_attack_button = ttk.Button(frame, text="quick attack and speed")
    defense_curl_button = ttk.Button(frame, text="defense curl")
    scratch_button = ttk.Button(frame, text="scratch")
    growl_button = ttk.Button(frame, text="growl")

    scratches_entry = ttk.Entry(frame,width=8)
    curl_entry = ttk.Entry(frame,width=8)

    quick_attack_slider = ttk.Scale(frame)

    # Grid the widgets:
    frame_label.grid(row=0,column=1)
    quick_attack_button.grid(row=1, column=0)
    defense_curl_button.grid(row=4,column=2)
    curl_entry.grid(row=3,column=2)
    scratch_button.grid(row=4, column=0)
    scratches_entry.grid(row=3,column=0)
    quick_attack_slider.grid(row=2,column=0)
    growl_button.grid(row=1,column=2)


    # Set the Button callbacks:
    quick_attack_button["command"] = lambda: handle_quick_attack(mqtt_sender,quick_attack_slider)
    defense_curl_button["command"] = lambda: handle_defense_curl(mqtt_sender,curl_entry)
    scratch_button["command"] = lambda: handle_scratch(mqtt_sender,scratches_entry)
    #tackle_button["command"] = lambda: handle_tackle(mqtt_sender)
    growl_button["command"] = lambda: handle_growl(mqtt_sender)

    return frame


def get_knock_off_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Knock Off")
    knock_off_table = ttk.Button(frame, text="Pushes objects off of surfaces")
    number_label = ttk.Label(frame, text="Items to knock off")
    number_entry = ttk.Entry(frame, width=8)
    aggression_label = ttk.Label(frame, text="Aggression of push")
    aggression_slider = ttk.Scale(frame)


    # Grid the widgets:
    frame_label.grid(row=1, column=1)
    knock_off_table.grid(row=2, column=1)
    number_entry.grid(row=3, column=0)
    number_label.grid(row=4, column=0)
    aggression_slider.grid(row=3, column=2)
    aggression_label.grid(row=4, column=2)

    # Set the Button callbacks:
    knock_off_table["command"] = lambda: handle_knock_off(mqtt_sender, aggression_slider, number_entry)

    return frame

def get_meow_at_door_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Meow at Door")
    meow_at_door = ttk.Button(frame, text="Meows at door until you let it out")
    number_label = ttk.Label(frame, text="Times to want in/out")
    number_entry = ttk.Entry(frame, width=8)


    # Grid the widgets:
    frame_label.grid(row=1, column=1)
    meow_at_door.grid(row=2, column=1)
    number_entry.grid(row=3, column=0)
    number_label.grid(row=4, column=0)

    # Set the Button callbacks:
    meow_at_door["command"] = lambda: handle_meow_at_door(mqtt_sender, number_entry)

    return frame

def get_ask_for_food_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Ask for food")
    ask_for_food = ttk.Button(frame, text="Asks for more food until you give it some")


    # Grid the widgets:
    frame_label.grid(row=1, column=1)
    ask_for_food.grid(row=2, column=1)

    # Set the Button callbacks:
    ask_for_food["command"] = lambda: handle_ask_for_food(mqtt_sender)

    return frame

def get_petting_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Get Pet")
    get_pet = ttk.Button(frame, text="Meows at door until you let it out")
    number_label = ttk.Label(frame, text="Times to get pet before running away")
    number_entry = ttk.Entry(frame, width=8)


    # Grid the widgets:
    frame_label.grid(row=1, column=1)
    get_pet.grid(row=2, column=1)
    number_entry.grid(row=3, column=0)
    number_label.grid(row=4, column=0)

    # Set the Button callbacks:
    get_pet["command"] = lambda: handle_get_pet(mqtt_sender, number_entry)

    return frame

def get_follow_mouse_frame(window,mqtt_sender):
    frame = ttk.Frame(window, padding=5, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Follow Mouse")
    follow_mouse = ttk.Button(frame, text="Follows a mouse around")


    # Grid the widgets:
    frame_label.grid(row=1, column=1)
    follow_mouse.grid(row=2, column=1)

    # Set the Button callbacks:
    follow_mouse["command"] = lambda: handle_follow_mouse(mqtt_sender)

    return frame

def handle_tone_until_distance_is_less_than(mqtt_sender,distance_entry, speed_entry, frequency_entry, rate_entry):
    print("will go until closer than: ", distance_entry.get())
    mqtt_sender.send_message('tone_until_distance_is_less_than', [distance_entry.get(), speed_entry.get(), frequency_entry.get(), rate_entry.get()])

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("backward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("backward", [(left_entry_box.get()), (right_entry_box.get())])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("left", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("left", [(left_entry_box.get()), (right_entry_box.get())])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("right", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("right", [(left_entry_box.get()), (right_entry_box.get())])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("stop")
    mqtt_sender.send_message("stop", [0, 0])


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("raise_arm")
    mqtt_sender.send_message("raise_arm", [])


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("lower_arm")
    mqtt_sender.send_message("lower_arm", [])


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("calibrate_arm")
    mqtt_sender.send_message("calibrate_arm")


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("move arm to position", arm_position_entry.get())
    mqtt_sender.send_message("move_arm_to_position", [arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()


###############################################################################
# Handlers for Buttons in the TeleOperation frame.
###############################################################################
def handle_time(mqtt_sender,seconds_entry_box,speed_entry_box):

    print("moving for", seconds_entry_box.get(), 'seconds')
    mqtt_sender.send_message("go_straight_for_inches_using_time",
                             [seconds_entry_box.get(), speed_entry_box.get()])

def handle_inches(mqtt_sender,inches_entry_box,speed_entry_box):

    print("moving for distance", inches_entry_box.get())
    mqtt_sender.send_message("go_straight_for_inches_using_encoder",
                [inches_entry_box.get(),speed_entry_box.get()])

###############################################################################
# Handlers for Buttons in the TeleOperation frame.
###############################################################################
def handle_number_of_beeps(mqtt_sender,beep_entry):
    print("I am beeping ", beep_entry.get(), " times")
    mqtt_sender.send_message("beep", [beep_entry.get()])

def handle_frequency(mqtt_sender,tone_entry):
    print("The tone is ", tone_entry.get())
    mqtt_sender.send_message("tone", [tone_entry.get(), 500])

def handle_phrase(mqtt_sender, phrase_entry):
    print(phrase_entry.get())
    mqtt_sender.send_message('speak', [phrase_entry.get()])


###############################################################################
# Handlers for Buttons in the ColorSensor frame.
###############################################################################
def handle_find_color(mqtt_sender,color_entry):
    print("will stop at color: ", color_entry.get())
    mqtt_sender.send_message('find_color', [color_entry.get()])


def handle_follow_color(mqtt_sender,color_entry):
    print("will follow line of color", color_entry.get())
    mqtt_sender.send_message('follow_color', [color_entry.get()])

def handle_follow_intensity(mqtt_sender, intensity_entry):
    print("will follow intensity:", intensity_entry.get())
    mqtt_sender.send_message('follow_intensity', intensity_entry.get())


###############################################################################
# Handlers for Buttons in the Infrared Proximity Sensor frame.
###############################################################################
def handle_go_forward_until_distance_is_less_than(mqtt_sender,distance_entry, speed_entry):
    print("will go until closer than: ", distance_entry.get())
    mqtt_sender.send_message('go_forward_until_distance_is_less_than',
                             [int(distance_entry.get()), int(speed_entry.get())])

def handle_go_backward_until_distance_is_greater_than(mqtt_sender,distance_entry, speed_entry):
    print("will go backward until further than", distance_entry.get())
    mqtt_sender.send_message('go_backward_until_distance_is_greater_than', [distance_entry.get(), speed_entry.get()])

def handle_go_until_distance_is_within(mqtt_sender, delta_entry, distance_entry, speed_entry):
    print("will go until distance is between:", distance_entry.get(), "and", distance_entry.get() + delta_entry.get())
    mqtt_sender.send_message('go_until_distance_is_within', [delta_entry.get(), distance_entry.get(), speed_entry.get()])


###############################################################################
# Handlers for Buttons in the Camera frame.
###############################################################################
def handle_spin_clockwise_until_sees_object(mqtt_sender, speed_entry):
    print("Spins clockwise until sees object")
    mqtt_sender.send_message('spin_clockwise_until_sees_object', [speed_entry.get()])


def handle_spin_counterclockwise_until_sees_object(mqtt_sender, speed_entry):
    print("Spins counterclockwise until sees object")
    mqtt_sender.send_message('spin_counterclockwise_until_sees_object', [speed_entry.get()])

def handle_m3_feature_9(mqtt_sender, distance_entry, speed_entry):
    mqtt_sender.send_message('search_for_object',[70,speed_entry.get()])
    mqtt_sender.send_message('pick_up_object', [distance_entry.get(), speed_entry.get()])



###############################################################################
# Handlers for Buttons in the Carter's personal frame.
###############################################################################

def handle_knock_off(mqtt_sender, aggression_slider, number_entry):
    print("knocks off", number_entry.get(), "items")
    mqtt_sender.send_message('knock_off_object', [aggression_slider.get(), number_entry.get()])

def handle_meow_at_door(mqtt_sender, number_entry):
    print("Wants in/out", number_entry.get(), "times")
    mqtt_sender.send_message('meow_at_door', [number_entry.get()])

def handle_ask_for_food(mqtt_sender):
    print("Asks for food to be filled")
    mqtt_sender.send_message('ask_for_food')

def handle_get_pet(mqtt_sender, number_entry):
    print("Gets pet", number_entry.get(), "times before running away")
    mqtt_sender.send_message('get_pet', [number_entry.get()])

def handle_follow_mouse(mqtt_sender):
    print("Follows a mouse around")
    mqtt_sender.send_message('follow_mouse')

###############################################################################
# Handlers for Buttons in the Nasser's personal frame.
###############################################################################

def handle_quick_attack(mqtt_sender,scale_entry):
    print("Rattata used quick attack")
    mqtt_sender.send_message('quick_attack', [scale_entry.get() * 100])

def handle_growl(mqtt_sender):
    print("Rattata used growl")
    mqtt_sender.send_message('growl')

def handle_defense_curl(mqtt_sender,spin_entry):
    print("Rattata used defense curl")
    mqtt_sender.send_message('defense_curl',[int(spin_entry.get())])

def handle_scratch(mqtt_sender,scratch_entry):
    print("Rattata used scratch")
    mqtt_sender.send_message('scratch', [int(scratch_entry.get())])