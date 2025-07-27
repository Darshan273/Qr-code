import qrcode

# Replace with your UPI payment info
upi_id =input("Enter your UPI ID: ")
payee_name =input("Enter the payee name: ")
amount =float(input("Enter the amount to pay: "))

# Construct UPI URL
upi_url = f"upi://pay?pa={upi_id}&pn={payee_name}&am={amount}&cu=INR"

# Generate QR code
qr = qrcode.make(upi_url)

# Save the QR code image
#qr.save("upi_qr_code.png")
#print("UPI QR code saved as 'upi_qr_code.png'")

qr.show()  # Display the QR code image