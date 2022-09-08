# This is a simple Python code for QR Code generation.

# Requires installation of modules:
# $ pip install PyQRCode
# $ pip install pypng

from pyqrcode import QRCode
import wifi_qrcode_generator


def genQR(destination):
    qr = QRCode(destination)
    qr.show()


def wifiQR(name, password):
    # wifi_qrcode_generator.wifi_qrcode('network name', False, 'WPA', 'password').show()
    wqr = wifi_qrcode_generator.wifi_qrcode(name, False, 'WPA', password)
    wqr.show()


if __name__ == '__main__':

    while True:
        ans = input("Will your Qr Code be for a WiFi Connection? (y/n)")
        if ans == "y" or ans == "Y" or ans == "Yes" or ans == "yes":
            wifiQR(input("\nExample: Arris-123 \nEnter Network Name: "),
                   input("\nExample: myPassword1234 \nEnter Network Password: ")
                   )
            break
        elif ans == "n" or ans == "N" or ans == "No" or ans == "no":
            genQR(input("Please insert the absolute path destination for QR Code:"))
            break
        else:
            print("Invalid input:", ans, "\n\nPlease enter a valid input. \nEx. y -> YES \n\t   or \n\tn -> NO\n")
            continue
