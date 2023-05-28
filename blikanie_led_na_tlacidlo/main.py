#importovanie kniznic
from machine import Pin

led = Pin(15, Pin.OUT)
#vytvorenie objektu pre tlacidlo
button = Pin(13, Pin.IN, Pin.PULL_UP)

#telo kodu ktory sposoby svietenie led svetla ked sa stlaci tlacidlo
try:
    while True:
        if not button.value():
            led.value(1)
        else:
            led.value(0)
except:
    pass
