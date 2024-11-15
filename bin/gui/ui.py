# 
# Author: Chase Quinn
# 
# This file is a part of xPass
# This file contains the main gui class export for all components
# 

# TTKBootstrap import
import ttkbootstrap as ttk

# TKinter import
import tkinter as tk

# Local imports
from .components.initial_setup import initial_setup
from .components.login import login_ui
from ..storage.storage import Storage

def create_gui():
    # Main GUI Window
    window = ttk.Window(themename="litera")
    window.title("xPass")
    window.geometry("600x400")
    window.minsize(600, 400)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    # Initial Setup Frame
    # Allows to hide this menu after setup
    initial_setup_frame = tk.Frame(window)
    initial_setup_frame.columnconfigure(0, weight=1)
    initial_setup_frame.rowconfigure(0, weight=1)
    initial_setup_frame.grid(column=0, row=0, sticky="nsew")

    # Login Frame
    # Allows to hide this menu after login
    login_frame = tk.Frame(window)
    login_frame.columnconfigure(0, weight=1)
    login_frame.rowconfigure(0, weight=1)
    login_frame.grid(column=0, row=0, sticky="nsew")

    # Call UI Functions
    initial_setup(initial_setup_frame)
    login_ui(login_frame)

    # Check if storage exists
    if Storage.check_for_storage():
        login_frame.tkraise()
    else:
        initial_setup_frame.tkraise()

    window.mainloop()