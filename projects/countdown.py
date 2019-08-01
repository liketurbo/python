import time
import subprocess

time_left = 5
while time_left > 0:
  print(time_left)
  time.sleep(1)
  time_left -= 1

subprocess.Popen(['start', './data/alarm.wav'], shell=True)
