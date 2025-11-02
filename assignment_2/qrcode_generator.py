import qrcode

img = qrcode.make('Some data here')

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Number of pixels per "box" of the QR code
    border=4,  # Thickness of the border (in boxes)
)

# Add data to the QR code
qr.add_data("https://www.bioxsystems.com/")
qr.make(fit=True)

# Create an image from the QR code data
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("example_qrcode.png")