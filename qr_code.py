import qrcode

data = input('Enter name or URL: ').strip()
# space thibboth ain krnw -> strip()
file_name = input('Enter your file name: ').strip()

qr = qrcode.QRCode(border=4, box_size=10)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')

image.save(file_name)
print(f'QR code saved in {file_name}')
