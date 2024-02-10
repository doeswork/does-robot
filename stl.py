import os
from datetime import datetime

# Determine the current time and format it
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"now-{current_time}.txt"

# Determine the home directory path
home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, file_name)

# Write to the file
with open(file_path, 'w') as file:
    file.write("This file was created by stl.py at " + current_time)
