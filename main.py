"""Aadhaar Card Pdf cracker

Steps:
    1. Enter Filelocation
    2. select circle
    3. Wait, if failed select another circle.
"""

from PyPDF2 import PdfFileReader
from itertools import product
from threading import Thread, active_count
import os
import time


def find(code):
    perms = ("".join(i) for i in product(pins, repeat=4))
    passwords = (`code` + extra for extra in perms)
    passwords = sorted(passwords)

    f = PdfFileReader(file(location, "rb"))
    for password in passwords:
        if f.decrypt(password):
            print "Password: {password}".format(password=password)
            os._exit(1)
    print "Thread completed"
    return

pins = [str(i) for i in range(10)]

def main(areacode):
    print areacode
    for code in areacode:
        thread = Thread(target=find, args=(code, ))
        thread.daemon = True
        thread.start()
        print "Thread started"

    while active_count > 0:
        time.sleep(1)
    raw_input("Password Not Found!!")

banner = """
Aadhaar Card Pdf cracker

Steps:
    1. Enter Filelocation
    2. select circle
    3. Wait, if failed select another circle.

circles:
    1. Delhi (11)
    2. Haryana (12 and 13)
    3. Punjab (14 to 16)
    4. Himachal Pradesh (17)
    5. Jammu & Kashmir (18 to 19)
    6. Uttar Pradesh and Uttaranchal (20 to 28)
    7. Rajasthan (30 to 34)
    8. Gujarat (36 to 39)
    9. Maharashtra (40 to 44)
    10. Madhya Pradesh and Chattisgarh (45 to 49)
    11. Andhra Pradesh (50 to 53)
    12. Karnataka (56 to 59)
    13. Tamil Nadu (60 to 64)
    14. Kerala (67 to 69)
    15. West Bengal (70 to 74)
    16. Orissa (75 to 77)
    17. Assam (78)
    18. North Eastern (79)
    19. Bihar and Jharkand (80 to 85)
    20. Army Postal Service (APS) (90 to 99)
"""

codes = [[11], [12, 13], range(14, 17), [17], [18, 19], range(20, 29), range(30, 35),
         range(36, 40), range(40, 45), range(45, 50), range(50, 54), range(56, 60),
         range(60, 65), range(67, 70), range(70, 75), range(75, 78), [78], [79], range(80, 86),
         range(90, 100)]

if __name__ == "__main__":
    print banner
    location = raw_input(r"File Location (example: c:\data\noname.pdf): ")
    if not os.path.isfile(location):
        print "Wrong Location"
        os._exit(1)
    index = input("Circle ID: ")
    if index >= len(codes) or index < 0:
        os._exit(1)
    main(codes[index-1])
