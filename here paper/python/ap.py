import qrcode

# Data to encode
data = "https://msuresult.github.io/result/"  # Replace this with any URL or text

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of border (boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("my_qr_code.png")

print("QR code generated and saved as 'my_qr_code.png'")
