import json
import random
import os
import sys
import smtplib

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
emails = sys.argv[1:]

assigned = []
last_worked = None

os.makedirs('dist/chores', exist_ok=True)

if not os.path.exists('dist/chores/last-worked.json'):
  with open('dist/chores/last-worked.json', 'w') as last_worked_file:
    last_worked = []
    last_worked_file.write('[]')
else:
  with open('dist/chores/last-worked.json', 'r') as last_worked_file:
    last_worked = json.load(last_worked_file)

with open('dist/chores/last-worked.json', 'w') as last_worked_file:
  # Assigning task with excluding last worked guys
  for email in set(emails).difference(last_worked):
    if len(chores) == 0:
      break

    random_chore = random.choice(chores)
    chores.remove(random_chore)

    assigned.append((email, random_chore))
    last_worked.append(email)

  # If we still have tasks, we use some of last worked, with taken queue
  if len(chores) != 0:
    cycled = False

    for email in last_worked:
      for assigning in assigned:
        if email == assigning[0]:
          cycled = True  # Means that we cycled

      if len(chores) == 0 or cycled:
        break  # Means all chores distributed

      random_chore = random.choice(chores)
      chores.remove(random_chore)

      last_worked.pop(0)
      last_worked.append(email)

  last_worked_file.write(json.dumps(last_worked))

smtp_obj = smtplib.SMTP('smtp.mail.ru', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('andrey.lukin.1986@bk.ru', 'Sswwf3i0NDyo4Pv')

for email, choir in assigned:
  smtp_obj.sendmail('andrey.lukin.1986@bk.ru', email,
                    'I don\'t know who you are, but you assigned to do ' + choir)

smtp_obj.close()
