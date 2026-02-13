try:
    import psutil
    print("loaded psutil")
    import time
    print("loaded time")
except:
    print("fatal error")
    time.sleep(10)
    exit

from cfg_reader import read_checkrun_cfg




sleeper = int(10)

while True:
  def is_process_running(process_name):
      for proc in psutil.process_iter(['name']):
          if proc.info['name'] == process_name:
              return True
      return False

  if is_process_running('mainscript.py'):
      print("main running")
  else:
      print("main not running")
#futureproofing for now, to be utilized later
  if is_process_running('blahblah.py'):
      print("running")
  else:
      print("not running")
      pass
  
  if is_process_running('blahblah.py'):
      print("running")
  else:
      print("not running")
      pass
  
  if is_process_running('blahblah.py'):
      print("running")
  else:
      print("not running")
      pass