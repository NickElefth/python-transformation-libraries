from PIL import Image
import os

img = Image.open('imgs/img1.jpg')
size = (300,300)
# save us png
# img.save('img1.jpg')

def make_dir(path):
    try:
        os.mkdir(path)
    except:
        pass

make_dir('_300')
for f in os.listdir('imgs'):
    image_path = os.path.join('imgs/', f)
    img = Image.open(image_path)

    img.thumbnail(size)
    img_name, img_ext = os.path.splitext(f)
    img.save('_300/{}_300.{}'.format(img_name, img_ext))

# img.show()