"""
Kod pra naprogramovanie blikania led svetla ktore je umiestnen na breadboard.

"""

#import pre pridanie kniznic
from machine import Pin
import time

#vytvorenie vystupu pre LED 
led = Pin(15, Pin.OUT)


#telo samostatneho kodu
try:
        #nekonecny cyklus pre neustale prehravanie kodu
    while True:
        #zapnutie LED svetla
        led.value(True)
        time.sleep(1)
        print("On")
        #vypnutie LED svetla
        led.value(False)
        time.sleep(1)
        print("Off")
        
except:
    pass

