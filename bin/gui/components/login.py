# 
# Author: Chase Quinn
# 
# This file is a part of xPass
# This file contains the login ui
# 

import tkinter as tk

def login_ui(root):
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
    top_center_container.grid(column=0, row=0, sticky="nsew")

    # The Form Widgets
    form_label = tk.Label(center_container, text="xPass")
    form_label.pack(pady = 10)
    form_label_username = tk.Label(center_container, text="Username")
    form_label_username.pack(pady = 3)
    form_entry_username = tk.Entry(center_container)
    form_entry_username.pack(pady = 3)
    form_label_password = tk.Label(center_container, text="Password")
    form_label_password.pack(pady = 3)
    form_entry_password = tk.Entry(center_container, show="*")
    form_entry_password.pack(pady = 3)
    form_submit = tk.Button(center_container, text="Login", command=lambda: print("Ey"))
    form_submit.pack(pady = 20)

    return main_container