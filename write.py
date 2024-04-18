# !/usr/bin/activate python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

# try:
#     text = input('New data:')
#     print("Now place your tag to write")
#     reader.Write(text)
#     print("Written")
# finally:
#     GPIO.cleanup()

try: 
    id, text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()

