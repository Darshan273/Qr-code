
import qrcode
from PIL import Image

# UPI payment details
upi_id = "darshanjain2202@oksbi"
payee_name = "Darshan Jain"
amount = "100.00"

# Create UPI URL
upi_url = f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR"

# Create QR Code object with style options
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(upi_url)
qr.make(fit=True)

# Custom color QR
img = qr.make_image(fill_color="darkblue", back_color="lightyellow")
img = img.convert("RGB")

# Save styled QR code
img.save("styled_upi_qr.png")

print("Styled UPI QR code saved as 'styled_upi_qr.png'")
