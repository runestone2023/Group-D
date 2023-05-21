import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Define App class
class App(Frame):

    # Define __init__ method
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.initUI()
        parent.bind("a", lambda event: self.press_a())
        parent.bind("w", lambda event: self.press_w())
        parent.bind("s", lambda event: self.press_s())
        parent.bind("d", lambda event: self.press_d())
        parent.bind("b", lambda event: self.press_b())
        parent.bind("r", lambda event: self.press_r())
        parent.bind("f", lambda event: self.press_f())
        parent.bind("g", lambda event: self.press_g())
        parent.bind("h", lambda event: self.press_h())
        parent.bind("q", lambda event: check_exit())

    # Define initUI method for creating widgets on window
    def initUI(self):

        # Add tab list
        tab_list = ttk.Notebook(window)
        tab_controller = ttk.Frame(tab_list)
        tab_analysis = ttk.Frame(tab_list)

        # Add name for each tab
        tab_list.add(tab_controller, text="Controller")
        tab_list.add(tab_analysis, text="Analysis")
        tab_list.pack(fill=BOTH, expand=True)

        # Load background image
        bg_path = os.path.abspath("Assets/Minewsweeper Logo.png")
        bg_open = Image.open(bg_path)
        bg_image = ImageTk.PhotoImage(bg_open)

        # Background of tab Controller (covered by another frame -> invisible)
        bg_tab_controller_label = Label(tab_controller, image=bg_image, bg="white")
        bg_tab_controller_label.image = bg_image
        bg_tab_controller_label.place(x=0, y=0, relheight=1, relwidth=1)

        # Frame of Controller Zone in tab Controller
        controller_zone = tk.Frame(tab_controller, height=240, bg="grey")
        controller_zone.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=FALSE)

        # Frame of Observation Zone (maybe show data from camera sensor) in tab Controller
        observation_zone = tk.Frame(tab_controller, height=480, bg="white")
        observation_zone.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=TRUE)

        # Frame of tab Analysis
        analysis = tk.Frame(tab_analysis, height=240, bg="white")
        analysis.pack(fill=tk.BOTH, expand=True)

        #Configure the grid of controller zone
        controller_zone.columnconfigure(0, weight=1)
        controller_zone.columnconfigure(1, weight=1)
        controller_zone.columnconfigure(2, weight=1)
        controller_zone.columnconfigure(3, weight=3)
        controller_zone.columnconfigure(4, weight=1)
        controller_zone.columnconfigure(5, weight=3)
        controller_zone.columnconfigure(6, weight=1)
        controller_zone.columnconfigure(7, weight=3)
        controller_zone.columnconfigure(8, weight=1)

        # Background for tab Analysis
        bg_tab_analysis_label = Label(tab_analysis, image=bg_image, bg="white")
        bg_tab_analysis_label.image = bg_image
        bg_tab_analysis_label.place(x=0, y=0, relheight=1, relwidth=1)

        # Create "Turn Up" button
        up_button_path = os.path.abspath("Assets/Up_Icon.png")
        up_button_open = Image.open(up_button_path).resize((50,50))
        up_button_image = ImageTk.PhotoImage(up_button_open)
        up_button_label = tk.Label(image=up_button_image, bg="white")
        up_button_label.image = up_button_image
        up_button = Button(controller_zone, command=self.press_w, image=up_button_image, height=50, width=50).grid(row=0, column=1, padx=10, pady=10)

        # Create "Turn Down" button
        down_button_path = os.path.abspath("Assets/Down_Icon.png")
        down_button_open = Image.open(down_button_path).resize((50,50))
        down_button_image = ImageTk.PhotoImage(down_button_open)
        down_button_label = tk.Label(image=down_button_image, bg="white")
        down_button_label.image = down_button_image
        down_button = Button(controller_zone, command=self.press_s, image=down_button_image, height=50, width=50).grid(row=2, column=1, padx=10, pady=10)

        # Create "Turn Left" button
        left_button_path = os.path.abspath("Assets/Left_Icon.png")
        left_button_open = Image.open(left_button_path).resize((50,50))
        left_button_image = ImageTk.PhotoImage(left_button_open)
        left_button_label = tk.Label(image=left_button_image, bg="white")
        left_button_label.image = left_button_image
        left_button = Button(controller_zone, command=self.press_a, image=left_button_image, height=50, width=50).grid(row=1, column=0, padx=10, pady=10)

        # Create "Turn Right" button
        right_button_path = os.path.abspath("Assets/Right_Icon.png")
        right_button_open = Image.open(right_button_path).resize((50,50))
        right_button_image = ImageTk.PhotoImage(right_button_open)
        right_button_label = tk.Label(image=right_button_image, bg="white")
        right_button_label.image = right_button_image
        right_button = Button(controller_zone, command=self.press_d, image=right_button_image, height=50, width=50).grid(row=1, column=2, padx=10, pady=10)

        # Create "Beep" button
        beep_button_path = os.path.abspath("Assets/Beep_Icon.png")
        beep_button_open = Image.open(beep_button_path).resize((50,50))
        beep_button_image = ImageTk.PhotoImage(beep_button_open)
        beep_button_label = Label(image=beep_button_image, bg="white")
        beep_button_label.image = beep_button_image
        beep_button = Button(controller_zone, command=self.press_b, image=beep_button_image, height=50, width=50).grid(row=0, column=4)

        # Create "Toggle Drill" button
        drill_button_path = os.path.abspath("Assets/Drill_Icon.png")
        drill_button_open = Image.open(drill_button_path).resize((50,50))
        drill_button_image = ImageTk.PhotoImage(drill_button_open)
        drill_button_label =Label(image=drill_button_image, bg="white")
        drill_button_label.image = drill_button_image
        drill_button = Button(controller_zone, command=self.press_r, image=drill_button_image, height=50, width=50).grid(row=0, column=6)

        # Create "Read Color Data" button
        scan_button_path = os.path.abspath("Assets/Scan_Icon.png")
        scan_button_open = Image.open(scan_button_path).resize((50, 50))
        scan_button_image = ImageTk.PhotoImage(scan_button_open)
        scan_button_label =Label(image=scan_button_image, bg="white")
        scan_button_label.image = scan_button_image
        scan_button = Button(controller_zone, command=self.press_f, image=scan_button_image, height=50, width=50).grid(row=0, column=8)

        # Create "Grab" button
        grab_button_path = os.path.abspath("Assets/Grab_Icon.png")
        grab_button_open = Image.open(grab_button_path).resize((50, 50))
        grab_button_image = ImageTk.PhotoImage(grab_button_open)
        grab_button_label =Label(image=grab_button_image, bg="white")
        grab_button_label.image = grab_button_image
        grab_button = Button(controller_zone, command=self.press_g, image=grab_button_image, height=50, width=50).grid(row=2, column=4)

        # Create "Release" button
        release_button_path = os.path.abspath("Assets/Release_Icon.png")
        release_button_open = Image.open(release_button_path).resize((50, 50))
        release_button_image = ImageTk.PhotoImage(release_button_open)
        release_button_label =Label(image=release_button_image, bg="white")
        release_button_label.image = release_button_image
        release_button = Button(controller_zone, command=self.press_h, image=release_button_image, height=50, width=50).grid(row=2, column=6)

        # Create "Exit" button
        exit_button_path = os.path.abspath("Assets/Exit_Icon.png")
        exit_button_open = Image.open(exit_button_path).resize((50, 50))
        exit_button_image = ImageTk.PhotoImage(exit_button_open)
        exit_button_label =Label(image=exit_button_image, bg="white")
        exit_button_label.image = exit_button_image
        exit_button = Button(controller_zone, command=check_exit, image=exit_button_image, height=50, width=50).grid(row=2, column=8)

        # Button description
        beep_text_label = Label(controller_zone, text="Beep", bg="grey").grid(row=0, column=3, sticky=E)
        drill_text_label = Label(controller_zone, text="Toggle Drill", bg="grey").grid(row=0, column=5, sticky=E)
        scan_text_label = Label(controller_zone, text="Read Color Data", bg="grey").grid(row=0, column=7, sticky=E)
        grab_text_label = Label(controller_zone, text="Grab", bg="grey").grid(row=2, column=3, sticky=E)
        release_text_label = Label(controller_zone, text="Release", bg="grey").grid(row=2, column=5, sticky=E)
        exit_text_label = Label(controller_zone, text="Exit", bg="grey").grid(row=2, column=7, sticky=E)

        # Label for Notice
        notice_label = Label(observation_zone,text="Add screen of camera sensor here!", font="bold", justify="center", bg="white")
        notice_label.pack(fill=BOTH, side=TOP, expand=TRUE)

# Event when press "a" key
    def press_a(parent):
        print("a")

# Event when press "w" key
    def press_w(parent):
        print("w")

# Event when press "s" key
    def press_s(parent):
        print("s")

# Event when press "d" key
    def press_d(parent):
        print("d")

# Event when press "b" key
    def press_b(parent):
        print("b")

# Event when press "r" key
    def press_r(parent):
        print("r")

# Event when press "f" key
    def press_f(parent):
        print("f")

# Event when press "g" key
    def press_g(parent):
        print("g")

# Event when press "h" key
    def press_h(parent):
        print("h")

# Define check_exit method for checking exit
def check_exit():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.quit()
# Create app window
window = Tk()
window.title("Minesweeper Controller")
window.geometry("1280x710")
window.protocol("WM_DELETE_WINDOW", check_exit)
app = App(window)
window.mainloop()