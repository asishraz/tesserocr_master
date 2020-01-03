#converting the image into black and white

from PIL import Image

#opening the image and making an object called column
column = Image.open('receipt_1.jpg')

#converitng the image into greyscale mode, i.e. "L", other modes are "RGB" and "CMYK"
gray = column.convert('L')

#tuning the image, ranging from 0 to 255
blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')

#saving the above black and white converted image
blackwhite.save("receipt_bw.jpg")
