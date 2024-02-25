# Write your code here :-)
import pyqrcode
url=pyqrcode.create ("www.python.org")    # line to the web site
url.svg("python.svg", scale=10)           # generating the QR code
print(url.terminal(quiet_zone=1))
