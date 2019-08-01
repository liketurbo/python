import threading
import time

print('Start of program.')


def takeANap():
  time.sleep(5)
  print('Wake up!')


threading_obj = threading.Thread(target=takeANap)
threading_obj.start()

print('End of program.')
