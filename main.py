# This is a simple Python code for QR Code generation.

# Requires installation of modules:
# $ pip install PyQRCode
# $ pip install pypng

from pyqrcode import QRCode


def genQR(destination):
    qr = QRCode(destination)
    qr.show()


if __name__ == '__main__':
    print("Insert the path destination for QR Code: ")
    genQR(input(""))
