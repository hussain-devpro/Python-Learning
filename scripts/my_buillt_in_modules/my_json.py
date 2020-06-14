import json
with open('../data_files/input.json', 'r') as inputFile:
    obj = json.load(inputFile)
    print("Hello "+ obj['name'])