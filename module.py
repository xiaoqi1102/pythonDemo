
from PIL import Image

im = Image.open('./img/test.png')

print(im.format,im.size)

im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')