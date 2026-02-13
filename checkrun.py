try:
    import psutil
    print("loaded psutil")
    import time
    print("loaded time")
    import threading
    print("loaded threading")
    import sys
    print("loaded sys")
except:
    print("fatal error")
    time.sleep(10)





sleeper = int(2)


def get_proc_list(process_name):
    print(f"waited for {sleeper} seconds")
    
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            print("found " + process_name)
            return True
    return False

switch = int(1)

while True:
    time.sleep(sleeper)
    if switch == 1:
        try:
            t1 = threading.Thread(target=get_proc_list, args=('Notepad.exe',))
            t2 = threading.Thread(target=get_proc_list, args=('Notepad2.exe',))
            t1.start()
            t2.start()
        except:
            print ("error" + str(sys.exc_info()[0]))
            pass
    else:
        print("disabled")
        time.sleep(2)
        