import re

'''
bar(?=bar)     finds the 1st bar ("bar" which has "bar" after it)
bar(?!bar)     finds the 2nd bar ("bar" which does not have "bar" after it)
(?<=foo)bar    finds the 1st bar ("bar" which has "foo" before it)
(?<!foo)bar    finds the 2nd bar ("bar" which does not have "foo" before it)
'''
strongpass_regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.{8,})')
