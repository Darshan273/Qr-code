import qrcode

# Data to encode
data = input("enter a data to you want to encode in qr code: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # size of the QR code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (min=4)
)

qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")


# Display the QR code
img.show()