import qrcode


img = qrcode.make("https://github.com/meganadeleh")
img.save("GitHub.png")

print("✅ QR Code saved")
