import imapclient
import webbrowser
import re
import pyzmail
from bs4 import BeautifulSoup

imap_obj = imapclient.IMAPClient('imap.mail.ru')
imap_obj.login('andrey.lukin.1986@bk.ru', 'Sswwf3i0NDyo4Pv')

imap_obj.select_folder('INBOX')

uids = imap_obj.search()
raw_messages = imap_obj.fetch(uids, ['BODY[]', 'FLAGS'])

links = []
for raw_msg in raw_messages.values():
  pyz_msg = pyzmail.PyzMessage.factory(raw_msg[b'BODY[]'])

  if pyz_msg.html_part:
    msg_soup = BeautifulSoup(
        pyz_msg.html_part.get_payload().decode(pyz_msg.html_part.charset), features="lxml")
    # elem = msg_soup.find('a', text='Unsubscribe')
    elem = msg_soup.find(lambda tag: tag.name ==
                         'a' and re.match(r'unsubscribe', tag.text, re.I))

    if elem:
      links.append(elem['href'])

imap_obj.logout()

for link in links:
  webbrowser.open(link)
