# Mini Project 9

# Install the following package before proceeding:
# !pip install pyqrcode pypng

# Import the following module:
import pyqrcode

# Define the data:
# We need some text that we want to convert as our QR Code. 
# Since I am creating the QR Code for my github profile, 
# I will "https://github.com/milaan9" as data here. Let's store inside a variable.
data = "https://github.com/KUNAL-7908"

# Create qrcode:
# Now that we have the data with us, we can move forward and 
# make use of the package we just imported. Let's create an variable.
# We will use the create method (as it results in a cleaner looking code) on data.
qr = pyqrcode.create(data)

# Save the qrcode in png format with proper scaling:
# Now let's store it in .png format with proper scaling.
qr.png("githubID.png", scale= 5)