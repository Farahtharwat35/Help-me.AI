import customtkinter
import controller


# todo set value send nothing
# todo edit window to be in center
# todo handle exceptions


def run(runfile):
    module = __import__('Gesture_Recogniser')
    with open(runfile, "r") as rnf:
        exec(rnf.read())


def create_screen(button_name):
    global label
    global button1
    global button2
    global button_label
    global whatsapp_button
    global navigate_button
    global control_button
    global anghami_button
    global screenshot_button
    global back_button

    if button_name == "Start":
        label = customtkinter.CTkLabel(master=root, text="Help me.AI", font=('Cooper Black', 80), text_color="#1B4769")
        label.pack(pady=100, padx=10)
        button1 = customtkinter.CTkButton(master=root, text="Start", width=120, height=60,
                                          fg_color="#1B4769", command=lambda: run("Gesture_Recogniser.py"))
        button1.place(relx=0.44, rely=0.6)
        button2 = customtkinter.CTkButton(master=root, text="Customize", width=120, height=60,
                                          fg_color="#1B4769", command=lambda: create_screen("Customize"))
        button2.place(relx=0.44, rely=0.8)

    if button_name == "Customize":
        label.destroy()
        button1.destroy()
        button2.destroy()

        button_label = customtkinter.CTkLabel(root, text="Options", font=("Cooper Black", 30), text_color="#1B4769")
        button_label.place(x=30, y=30)

        whatsapp_button = customtkinter.CTkButton(root, text="Whatsapp", font=("Georgia", 14), width=100, height=100,
                                                  fg_color="#1B4769", command=lambda: create_window("Whatsapp"))
        whatsapp_button.place(x=350, y=100)

        navigate_button = customtkinter.CTkButton(root, text="Navigate", font=("Georgia", 14), width=100, height=100,
                                                  fg_color="#1B4769", command=lambda: create_window("Navigate"))
        navigate_button.place(x=500, y=100)

        control_button = customtkinter.CTkButton(root, text="Control", font=("Georgia", 14), width=100, height=100,
                                                 fg_color="#1B4769", command=lambda: create_window("Control"))
        control_button.place(x=500, y=250)

        anghami_button = customtkinter.CTkButton(root, text="Anghami", font=("Georgia", 14), width=100, height=100,
                                                 fg_color="#1B4769", command=lambda: create_window("Anghami"))
        anghami_button.place(x=350, y=250)

        screenshot_button = customtkinter.CTkButton(root, text="ScreenShot", font=("Georgia", 14), width=100,
                                                    height=100,
                                                    fg_color="#1B4769", command=lambda: create_window("ScreenShot"))
        screenshot_button.place(x=425, y=400)

        back_button = customtkinter.CTkButton(root, text="Back", font=("Georgia", 14), width=100, height=30,
                                              fg_color="#1B4769", command=lambda: create_screen("Back"))
        back_button.place(x=50, y=550)

    if button_name == "Back":
        button_label.destroy()
        whatsapp_button.destroy()
        navigate_button.destroy()
        control_button.destroy()
        anghami_button.destroy()
        screenshot_button.destroy()
        back_button.destroy()

        label = customtkinter.CTkLabel(master=root, text="Help me.AI", font=('Cooper Black', 80), text_color="#1B4769")
        label.pack(pady=100, padx=10)
        button1 = customtkinter.CTkButton(master=root, text="Start", width=120, height=60,
                                          fg_color="#1B4769", command=lambda: run("Gesture_Recogniser.py"))
        button1.place(relx=0.44, rely=0.6)
        button2 = customtkinter.CTkButton(master=root, text="Customize", width=120, height=60,
                                          fg_color="#1B4769", command=lambda: create_screen("Customize"))
        button2.place(relx=0.44, rely=0.8)


def create_window(button_name):
    if button_name == "Control":
        window1 = customtkinter.CTkToplevel(root, fg_color="#AAC7D8")
        window1.geometry("500x300")
        window1.resizable(False, False)
        window1.title(button_name)
        window1.attributes('-topmost', True)
        window1.geometry("+{}+{}".format(653, 300))

        button_label = customtkinter.CTkLabel(window1, text=button_name, font=("Georgia", 24), text_color="#1B4769")
        button_label.place(x=10, y=10)

        open_Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                                    values=(
                                                        "HIGH-FIVE", "PEACE", "ONE", "SPIDERMAN", "CALL", "PERFECTO"))
        open_Gesturebox.set("")
        open_Gesturebox.place(x=150, y=40)

        label_openGesture = customtkinter.CTkLabel(window1, text="Open Gesture:",
                                                   font=("Georgia", 14), text_color="#1B4769")
        label_openGesture.place(x=50, y=40)

        Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                               values=("HIGH-FIVE", "PEACE", "ONE", "SPIDERMAN", "CALL", "PERFECTO"))
        Gesturebox.set("")
        Gesturebox.place(x=150, y=80)

        label_Gesture = customtkinter.CTkLabel(window1, text="Gesture:", font=("Georgia", 14), text_color="#1B4769")
        label_Gesture.place(x=50, y=80)

        function_box = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                                 values=("Volume Up", "Volume Down", "Scroll Up", "Scroll Down",
                                                         "Open Program"))
        function_box.set("")
        function_box.place(x=150, y=120)

        label_function = customtkinter.CTkLabel(window1, text="Function:", font=("Georgia", 14), text_color="#1B4769")
        label_function.place(x=50, y=120)

        textbox = customtkinter.CTkEntry(master=window1, placeholder_text="Program name",
                                         width=250, height=55, border_color="#1B4769")
        textbox.place(x=150, y=160)

        save_button = customtkinter.CTkButton(window1, text="Save", fg_color="#1B4769",
                                              command=lambda: controller.update_gesture(open_Gesturebox.get(),
                                                                                        Gesturebox.get(), button_name,
                                                                                        function_box.get(),
                                                                                        textbox.get()))
        save_button.place(x=250, y=250, anchor="center")

    if button_name == "Navigate":
        window1 = customtkinter.CTkToplevel(root, fg_color="#AAC7D8")
        window1.geometry("500x300")
        window1.resizable(False, False)
        window1.title(button_name)
        window1.attributes('-topmost', True)
        window1.geometry("+{}+{}".format(653, 300))

        button_label = customtkinter.CTkLabel(window1, text=button_name, font=("Georgia", 24), text_color="#1B4769")
        button_label.place(x=10, y=10)

        open_Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                                    values=(
                                                        "HIGH-FIVE", "PEACE", "ONE", "SPIDERMAN", "CALL", "PERFECTO"))
        open_Gesturebox.set("")
        open_Gesturebox.place(x=150, y=60)

        label_openGesture = customtkinter.CTkLabel(window1, text="Open Gesture:",
                                                   font=("Georgia", 14), text_color="#1B4769")
        label_openGesture.place(x=50, y=60)

        Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                               values=("HIGH-FIVE", "PEACE", "ONE", "SPIDERMAN", "CALL", "PERFECTO"))
        Gesturebox.set("")
        Gesturebox.place(x=150, y=100)

        label_Gesture = customtkinter.CTkLabel(window1, text="Gesture:", font=("Georgia", 14), text_color="#1B4769")
        label_Gesture.place(x=50, y=100)

        textbox = customtkinter.CTkEntry(master=window1, placeholder_text="Type form/to dest",
                                         width=250, height=55, border_color="#1B4769")
        textbox.place(x=150, y=140)

        save_button = customtkinter.CTkButton(window1, text="Save", fg_color="#1B4769",
                                              command=lambda: controller.update_gesture(open_Gesturebox.get(),
                                                                                        Gesturebox.get(), button_name,
                                                                                        "", textbox.get()))
        save_button.place(x=250, y=240, anchor="center")

    if button_name == "Anghami":
        window1 = customtkinter.CTkToplevel(root, fg_color="#AAC7D8")
        window1.geometry("500x300")
        window1.resizable(False, False)
        window1.title(button_name)
        window1.attributes('-topmost', True)
        window1.geometry("+{}+{}".format(653, 300))

        button_label = customtkinter.CTkLabel(window1, text=button_name, font=("Georgia", 24), text_color="#1B4769")
        button_label.place(x=10, y=10)

        open_Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                                    values=(
                                                        "HIGH-FIVE", "PEACE", "ONE", "SPIDERMAN", "CALL", "PERFECTO"))
        open_Gesturebox.set("")
        open_Gesturebox.place(x=150, y=60)

        label_openGesture = customtkinter.CTkLabel(window1, text="Open Gesture:",
                                                   font=("Georgia", 14), text_color="#1B4769")
        label_openGesture.place(x=50, y=60)

        Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                               values=("HIGH-FIVE", "PEACE", "ONE", "SPIDERMAN", "CALL", "PERFECTO"))
        Gesturebox.set("")
        Gesturebox.place(x=150, y=100)

        label_Gesture = customtkinter.CTkLabel(window1, text="Gesture:", font=("Georgia", 14), text_color="#1B4769")
        label_Gesture.place(x=50, y=100)

        textbox = customtkinter.CTkEntry(master=window1, placeholder_text="Playlist name",
                                         width=250, height=55, border_color="#1B4769")
        textbox.place(x=150, y=140)

        save_button = customtkinter.CTkButton(window1, text="Save", fg_color="#1B4769",
                                              command=lambda: controller.update_gesture(open_Gesturebox.get(),
                                                                                        Gesturebox.get(), button_name,
                                                                                        "", textbox.get()))
        save_button.place(x=250, y=240, anchor="center")

    if button_name == "ScreenShot":
        window1 = customtkinter.CTkToplevel(root, fg_color="#AAC7D8")
        window1.geometry("500x300")
        window1.resizable(False, False)
        window1.title(button_name)
        window1.attributes('-topmost', True)
        window1.geometry("+{}+{}".format(653, 300))

        button_label = customtkinter.CTkLabel(window1, text=button_name, font=("Georgia", 24), text_color="#1B4769")
        button_label.place(x=10, y=10)

        open_Gesturebox = customtkinter.CTkComboBox(master=window1, width=150, height=40, border_color="#1B4769",
                                                    values=(
                                                        "HIGH-FIVE", "PEACE", "ONE", "SPIDERMAN", "CALL", "PERFECTO"))
        open_Gesturebox.set("")
        open_Gesturebox.place(x=175, y=100)

        label_openGesture = customtkinter.CTkLabel(window1, text="Open Gesture:", font=("Georgia", 14),
                                                   text_color="#1B4769")
        label_openGesture.place(x=75, y=103)

        save_button = customtkinter.CTkButton(window1, text="Save", fg_color="#1B4769",
                                              command=lambda: controller.update_gesture(open_Gesturebox.get(), "",
                                                                                        button_name, "", ""))
        save_button.place(x=250, y=240, anchor="center")

    if button_name == "Whatsapp":
        window1 = customtkinter.CTkToplevel(root, fg_color="#AAC7D8")
        window1.geometry("500x300")
        window1.resizable(False, False)
        window1.title(button_name)
        window1.attributes('-topmost', True)
        window1.geometry("+{}+{}".format(653, 300))

        button_label = customtkinter.CTkLabel(window1, text=button_name, font=("Georgia", 24), text_color="#1B4769")
        button_label.place(x=10, y=10)

        open_Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                                    values=(
                                                        "HIGH-FIVE", "PEACE", "ONE", "CALL", "PERFECTO"))
        open_Gesturebox.set("")
        open_Gesturebox.place(x=150, y=40)

        label_openGesture = customtkinter.CTkLabel(window1, text="Open Gesture:",
                                                   font=("Georgia", 14), text_color="#1B4769")
        label_openGesture.place(x=50, y=40)

        Gesturebox = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                               values=("HIGH-FIVE", "PEACE", "ONE", "CALL", "PERFECTO"))
        Gesturebox.set("")
        Gesturebox.place(x=150, y=80)

        label_Gesture = customtkinter.CTkLabel(window1, text="Gesture:", font=("Georgia", 14), text_color="#1B4769")
        label_Gesture.place(x=50, y=80)

        function_box = customtkinter.CTkComboBox(master=window1, border_color="#1B4769",
                                                 values=("Search Contact", "Send Message", "Open Mic"))
        function_box.set("")
        function_box.place(x=150, y=120)

        label_function = customtkinter.CTkLabel(window1, text="Function :", font=("Georgia", 14), text_color="#1B4769")
        label_function.place(x=50, y=120)

        textbox = customtkinter.CTkEntry(master=window1, width=250, height=55, border_color="#1B4769",
                                         placeholder_text="Contact/Type message")
        textbox.place(x=150, y=160)

        save_button = customtkinter.CTkButton(window1, text="Save", fg_color="#1B4769",
                                              command=lambda: controller.update_gesture(open_Gesturebox.get(),
                                                                                        Gesturebox.get(), button_name,
                                                                                        function_box.get(),
                                                                                        textbox.get()))
        save_button.place(x=250, y=250, anchor="center")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk(fg_color="#AAC7D8")
root.geometry("900x600")
root.resizable(False, False)
root.title("Help me.AI")
root.geometry("+{}+{}".format(380, 150))
create_screen("Start")


root.mainloop()
