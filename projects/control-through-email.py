import imapclient
import subprocess
import pyzmail
from os import path

imap_obj = imapclient.IMAPClient('imap.mail.ru')
imap_obj.login('andrey.lukin.1986@bk.ru', 'Sswwf3i0NDyo4Pv')

imap_obj.select_folder('INBOX', readonly=True)

uids = imap_obj.search(['UNSEEN'])
raw_messages = imap_obj.fetch(uids, ['BODY[]', 'FLAGS'])

for raw_msg in raw_messages.values():
  pyz_msg = pyzmail.PyzMessage.factory(raw_msg[b'BODY[]'])

  if pyz_msg.get_subject() == 'Torrent file':
    filename = pyz_msg.mailparts[2].filename
    content = pyz_msg.mailparts[2].get_payload()

    dist = path.join('dist', filename)

    with open(dist, 'wb') as torrent_file:
      torrent_file.write(content)

  qb_process = subprocess.Popen(
      ['C:\\Program Files\\qBittorrent\\qbittorrent.exe', dist])
  qb_process.wait()
