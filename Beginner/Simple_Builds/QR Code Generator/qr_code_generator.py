"""
Beginner Level - Simple Project
Dice Roller Game
By StriX ProDev
"""

# python3 -m venv venv
# source venv/bin/activate   # for Mac/Linux
# or on Windows:
# venv\Scripts\activate

# Install dependencies
# You need two Python packages:
# qrcode → for generating QR codes
# pillow → for image rendering (fixes the "No module named PIL" error)

# pip install qrcode[pil] pillow


# Step 1: Ask user for input
# Step 2: Create QR Code object
# Step 3: Add data to the QR code
# Step 4: Convert into an image
# Step 5: Save the image

'''
import qrcode


data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename (without extension): ").strip()


qr = qrcode.QRCode(
    version=1,        # size of the QR code (1 = smallest, 40 = largest)
    box_size=10,      # pixel size of each box
    border=4          # white border size
)

qr.add_data(data)
qr.make(fit=True)


image = qr.make_image(fill_color="black", back_color="white")


filename = f"{filename}.png"
image.save(filename)

print(f"✅ QR Code saved as {filename}")

'''

import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enetr the filename: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color = 'black', back_color = 'white')
image.save(filename)
print(f'QR Code Saved as {filename}')

