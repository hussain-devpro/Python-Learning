import json
with open('../../cfg/input.json', 'r') as inputFile:
    obj = json.load(inputFile)
    print("Hello "+ obj['name'])