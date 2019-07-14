import requests

try:
  res = requests.get(
      'https://student.sechenov.ru/upload/iblock/da5/309%20%D0%BE%D1%82%2006.04.1995.pdf')
  res.raise_for_status()

  file = open('./dist/some-file.pdf', 'wb')
  for chunk in res.iter_content(100000):
    file.write(chunk)
  file.close()
except Exception as err:
  print(err)
