import qrcode
code = qrcode.QRCode(
    version =1,
    box_size = 100,
    border = 3
)
code.add_data("https://www.youtube.com/@CodeCube")
code.make(fit=True)

image = code.make_image(fill_color="blue",back_color="lavender")
image.save("qr.png")
print("Bitti!")