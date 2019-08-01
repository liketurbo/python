import datetime
import time

my_birthday = datetime.datetime(1996, 1, 25)

current_date = datetime.datetime.now()
current_date = datetime.datetime.fromtimestamp(time.time())

thousand_days = datetime.timedelta(days=1000)
after_thousand_days = current_date + thousand_days

str_after_thousand_days = after_thousand_days.strftime(
    '%d/%m/%Y %A %H:%M:%S:%f')

print(datetime.datetime.strptime(
    str_after_thousand_days, '%d/%m/%Y %A %H:%M:%S:%f') == after_thousand_days)
