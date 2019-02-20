# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
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

def handle_get_pet(mqtt_sender, number_entry):
    print("Gets pet", number_entry.get(), "times before running away")
    mqtt_sender.send_message('get_pet', [number_entry.get()])

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

def handle_follow_mouse(mqtt_sender):
    print("Follows a mouse around")
    mqtt_sender.send_message('follow_mouse')