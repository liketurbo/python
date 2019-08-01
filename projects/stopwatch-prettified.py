import time
import pyperclip

print('Press ENTER to begin. Afterwards press ENTER for new lap. Press Ctrl-C to quit.')

# After pressing ENTER it starts
input()

print('Started.')

start_time = time.time()
last_time = start_time

lap_num = 1

output = []
try:
  while True:
    input()

    lap_time = round(time.time() - last_time, 2)
    total_time = round(time.time() - start_time, 2)

    # output.append('Lap #' + str(lap_num).rjust(2) + ':' +
    #               str(total_time).rjust(6) + ' (' + str(lap_time).rjust(6) + ')')
    # print(output[-1])
    output.append('Lap #{:>2}:{:>6} ({:>6})'.format(
        lap_num, total_time, lap_time))
    print(output[-1], end='')

    lap_num += 1
    last_time = time.time()
except KeyboardInterrupt:
  print('\n\nDone')

print('Results copied to cliboard.')
pyperclip.copy('\n'.join(output))
