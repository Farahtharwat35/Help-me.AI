import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("GUI")
root.geometry("1366x768")
root.resizable(width=False, height=False)

# image_file = "Artboard 1.png"
# try:
#     image = tk.PhotoImage(file=image_file)
# except tk.TclError as e:
#     print("Error loading image:", e)
#     root.quit()
# Load the background image
# PUT YOUR BACKGROUND HERE>>>>>>>>>
# bg_image = tk.PhotoImage(file="Artboard 1.png")
#
# # Create a label with the background image and add it to the main window
# bg_label = tk.Label(root, image=bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the five buttons
whatsapp_button = tk.Button(root, text="Whatsapp", width=20, height=5, command=lambda: create_window("Whatsapp"))
navigate_button = tk.Button(root, text="Navigate", width=20, height=5, command=lambda: create_window("Navigate"))
control_button = tk.Button(root, text="Control", width=20, height=5, command=lambda: create_window("Control"))
anghami_button = tk.Button(root, text="Anghami", width=20, height=5, command=lambda: create_window("Anghami"))
screenshot_button = tk.Button(root, text="screenShot", width=20, height=5, command=lambda: create_window("screenShot"))

# Center the five buttons on the main window
whatsapp_button.place(relx=0.5, rely=0.3, anchor="center")
navigate_button.place(relx=0.5, rely=0.4, anchor="center")
control_button.place(relx=0.5, rely=0.5, anchor="center")
anghami_button.place(relx=0.5, rely=0.6, anchor="center")
screenshot_button.place(relx=0.5, rely=0.7, anchor="center")

# Function to create a new window for each button
def create_window(button_name):
    new_window = tk.Toplevel(root)
    new_window.title(button_name)
    new_window.geometry("500x300")
    new_window.resizable(width=False, height=False)

    # Add the label, combo box, text box, and save button to the new window
    button_label = tk.Label(new_window, text=button_name, font=("Arial Bold", 14))
    button_label.place(x=10, y=10)

    combo_label = tk.Label(new_window, text="Open Gesture", font=("Arial Bold", 10))
    combo_label.place(x=10, y=50)

    combo_box = ttk.Combobox(new_window, width=15)
    combo_box["values"] = ("Value 1", "Value 2", "Value 3")
    combo_box.current(0)
    combo_box.place(x=120, y=50)

    gesture_label = tk.Label(new_window, text="Gesture", font=("Arial Bold", 12))
    gesture_label.place(x=10, y=100)

    gesture_box = ttk.Combobox(new_window, width=15)
    gesture_box["values"] = ("Gesture 1", "Gesture 2", "Gesture 3")
    gesture_box.current(0)
    gesture_box.place(x=120, y=100)

    function_label = tk.Label(new_window, text="Function", font=("Arial Bold", 12))
    function_label.place(x=250, y=100)

    function_box = ttk.Combobox(new_window, width=15)
    function_box["values"] = ("Function 1", "Function 2", "Function 3")
    function_box.current(0)
    function_box.place(x=360, y=100)

    text_box = tk.Text(new_window, height=5, width=50)
    text_box.place(x=10, y=150)

    save_button = tk.Button(new_window, text="Save")
    save_button.place(relx=0.5, rely=0.9, anchor="center")

# Run the main loop
root.mainloop()