from PIL import Image, ImageFilter

img = Image.open('imgs/img1.jpg')
# Rotate
img = img.rotate(90)

# Convert to BW
img = img.convert(mode='L')

# Blur the image
img = img.filter(ImageFilter.GaussianBlur(4))

img.show()