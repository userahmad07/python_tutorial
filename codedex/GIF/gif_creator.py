import imageio.v3 as iio

images = ['Screenshot.png', 'Screenshot1.png']

img = []

for i in images:
    img.append(iio.imread(i))

iio.imwrite('colab.gif', img , duration=500, loop=0)