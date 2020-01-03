#converting the image into black and white

from PIL import Image
column = Image.open('receipt_1.jpg')
gray = column.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
blackwhite.save("receipt_bw.jpg")
