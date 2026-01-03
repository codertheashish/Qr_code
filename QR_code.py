import qrcode

print("Enter your URL (Google Drive link or any link):")
data = input("Paste URL here: ")

# QR generate
qr = qrcode.make(data)

# Saved
file_name = "generated_qr.png"
qr.save(file_name)

print(f"Your QR Code is ready ✅ Saved as: {file_name}")

