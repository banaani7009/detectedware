import os
from multiprocessing import Process
import tkinter as tk
CONFIG_DIR = "configs"

REQUIRED_CONFIGS = {
    "checkrun.cfg",
    "config2.cfg",
    "config3.cfg",
    "config4.cfg",
    "config5.cfg",
}

existing_files = {
    f.name for f in os.scandir(CONFIG_DIR)
    if f.is_file()
}

missing = REQUIRED_CONFIGS - existing_files

if not missing:
    print("Integrity check passed.")
else:
    print("Missing configs:", missing)





def loop_a():
    while 1:
        app = tk.Tk()
        
        

        tk.mainloop()

def loop_b():
    while 1:
        print("b")

if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()
