import imapclient
import pyzmail

# Internet Message Access Protocol (IMAP)
imap_obj = imapclient.IMAPClient('imap.mail.ru')
imap_obj.login('andrey.lukin.1986@bk.ru', 'Sswwf3i0NDyo4Pv')

# Selecting folder
imap_obj.select_folder('INBOX')

# Searching for email
uids = imap_obj.search(['SEEN'])
raw_messages = imap_obj.fetch(uids, ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(raw_messages[1][b'BODY[]'])
print(message.get_subject())
print(message.get_address('from'))
print(message.get_address('to'))

if message.text_part:
  print(message.text_part.get_payload().decode(message.text_part.charset))

if message.html_part:
  print(message.html_part.get_payload().decode(message.text_part.charset))

imap_obj.logout()
