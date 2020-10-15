from PIL import Image

iname = 'pasto.jpg'
oname = '8-pasto.png'

img = Image.open(iname)
newimg = Image.convert('P', palette=Image.ADAPTIVE, colors=8)
newimg.save(oname)