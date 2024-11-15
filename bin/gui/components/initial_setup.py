# 
# Author: Chase Quinn
# 
# This file is a part of xPass
# This file contains the initial setup ui
# 

import os
import tkinter as tk
import ttkbootstrap as ttk

from ...storage.storage import Storage

def initial_setup(root):
    # The main container
    main_container = tk.Frame(root, bg="white")
    main_container.grid(column=0, row=0, sticky="nsew")
    main_container.columnconfigure(0, weight=1)
    main_container.columnconfigure(1, weight=1)
    main_container.columnconfigure(2, weight=1)
    main_container.rowconfigure(0, weight=1)
    main_container.rowconfigure(1, weight=1)
    main_container.rowconfigure(2, weight=1)

    # The center container
    center_container = tk.Frame(main_container)
    center_container.grid(column=1, row=1, sticky="nsew")
    center_container.columnconfigure(0, weight=1)
    center_container.rowconfigure(0, weight=1)
    center_container.rowconfigure(1, weight=1)
    center_container.rowconfigure(2, weight=1)
    center_container.rowconfigure(3, weight=1)
    center_container.rowconfigure(4, weight=1)

    # Top Center Container
    top_center_container = tk.Frame(main_container)
    top_center_container.grid(column=1, row=0, sticky="nsew")
    top_center_container.columnconfigure(0, weight=1)
    top_center_container.rowconfigure(0, weight=1)

    # The Form Widgets
    form_label_two = tk.Label(center_container, text="Initial Setup")
    form_label_two.pack(pady = 6)
    form_label_username = tk.Label(center_container, text="Username")
    form_label_username.pack(pady = 3)
    form_entry_username = tk.Entry(center_container)
    form_entry_username.pack(pady = 3)
    form_label_password = tk.Label(center_container, text="Password")
    form_label_password.pack(pady = 3)
    form_entry_password = tk.Entry(center_container, show="*")
    form_entry_password.pack(pady = 3)
    form_label_verify_password = tk.Label(center_container, text="Verify Password")
    form_label_verify_password.pack(pady = 3)
    form_entry_verify_password = tk.Entry(center_container, show="*")
    form_entry_verify_password.pack(pady = 3)

    # Form Function
    def form_submit():
        if len(form_entry_password.get()) >= 8:
            if len(form_entry_username.get()) >= 5:
                if form_entry_password.get() == form_entry_verify_password.get():
                    Storage.create_first_setup(form_entry_username.get(), form_entry_password.get())
                    root.destroy()
                else:
                    print("passwords do not match")
            else:
                print("username too short")
        else:
            error_form_label = ttk.Label(top_center_container, text="Password is too short", bootstyle="inverse-danger")
            error_form_label.pack(pady = 3)

    form_submit = tk.Button(center_container, text="Submit", command=form_submit)
    form_submit.pack(pady = 20)

    return main_container