import json

data = {
    'name': 'Zophie',
    'is_cat': True,
    'mice_caught': 0,
    'feline_IQ': None
}
string_data = json.dumps(data)
dict_data = json.loads(string_data)

print(dict_data)
