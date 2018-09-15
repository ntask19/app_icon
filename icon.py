import json

jsonDatas = open('icons.json', "r")
iconDatas = json.loads(jsonDatas.read())
jsonDatas.close()
