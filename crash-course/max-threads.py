def get_max_threads():
  ''' Returns the number of available threads on a linux/win based system '''
  if sys.platform == 'win32':
    return (int)(os.environ['NUMBER_OF_PROCESSORS'])
  else:
    return (int)(os.popen('grep -c cores /proc/cpuinfo').read())
