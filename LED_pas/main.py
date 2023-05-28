#importovanie kniznic pre spustenie programu
from machine import Pin
import time

#nastavenie vsetkych pinov pripojenych k doske
pins = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]

#kod pre prechadzajuce svetlo
def showLed():
    #smer do jednej strany
    for pin in pins:
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)
        
    #prechod do opacnej strany
    for pin in reversed(pins):
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)

#spustenie kodu (nekonecny cyklus)
while True:
    showLed()

