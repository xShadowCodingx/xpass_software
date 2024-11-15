# 
# Author: Chase Quinn
# 
# This file is a part of xPass
# This file contains the storage class that handles all information
# 

import os, json

file_path = os.getcwd() + "/bin/storage/xpass.json"

class Storage:
    
    def check_for_storage():
        if os.path.exists(file_path):
            return True
        else:
            return False        
    
    def create_first_setup(username, password):
        initial_setup = {
            "user": {
                "username": username,
                "password": password
            },
            "passwords": []
        }

        with open(file_path, "w") as f:
            f.write(json.dumps(initial_setup, indent=4))
        f.close()
        print("Created")