from PIL import  Image, ImageFilter

im = Image.open('./img/19.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('./img/blur.jpg', 'jpeg')