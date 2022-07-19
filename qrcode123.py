import qrcode

# crate instance of qrcode
qr=qrcode.QRCode(version=20, #it is the size of qr code take input from1 to 40 mean here are 40 version if high version used then high data module of qrcode generated
                 box_size=2, # size of each box in pixels
                 border=1 #thickness of the border
                 )

# now enter url for qrcode
data="https://www.youtube.com/channel/UCOwCT0UnrLwoRFFzHXIln3A"
qr.add_data(data)

# now fix the data module if url is fit or not
qr.make(fit=True) #it is fit the url to above define data module of qrcode

# noe define color for qrcode
img=qr.make_image(fill='black',back_color='white')

# now save the image
img.save("test3.png")