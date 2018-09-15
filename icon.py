import json
import glob
from PIL import Image

jsonDatas = open('icons.json', "r")
iconDatas = json.loads(jsonDatas.read())
jsonDatas.close()

def getIconData(width):
    for iconData in iconDatas.values():
        if iconData['width'] == width:
            return iconData


files = glob.glob('input/*.png')

for f in files:
    img = Image.open(f)
    iconData = getIconData(img.width)
    for icon in iconData['contents']:
        imgResize = img.resize((icon['size'], icon['size']))
        imgResize.save('output/'+icon['name'])
        print( icon['name'] )
