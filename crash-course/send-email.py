import smtplib

# Simple Mail Transfer Protocol (SMTP)
smtp_obj = smtplib.SMTP('smtp.mail.ru', 587)

# Establishing connection with server
res = smtp_obj.ehlo()

# Enable encryption
smtp_obj.starttls()

# Logging
smtp_obj.login('andrey.lukin.1986@bk.ru', 'Sswwf3i0NDyo4Pv')

# Sending email
smtp_obj.sendmail('andrey.lukin.1986@bk.ru',
                  'theliketurbo@gmail.com', 'Subject: Test\nI am maybe spam.')

# Disconnecting
smtp_obj.quit()
