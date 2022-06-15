import qrcode
from PIL import Image


Logo_link = 'reslogo.jpg'

logo = Image.open(Logo_link)

basewidth = 100

wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

url = 'https://leslievrosales.com/linkspage/'

QRcode.add_data(url)

QRcode.make()

QRcolor = 'Purple'

QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

QRimg.save('Leslie_QR.png')

print('QR code generated!')
