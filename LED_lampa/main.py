#importovanie kniznic
from machine import Pin
import time

#nastavenie komponentov ako objektov pre to aby python vedel s nimi pracovat
led = Pin(15, Pin.OUT)                   
button = Pin(13, Pin.IN, Pin.PULL_UP) 

#vytvorenie kyvadlovej funkcie pre zmenu stavu LED na inu hodnotu voci hodnote ktoru malo ako poslednu
def reverseGPIO():
    if led.value():
        led.value(0)
    else:
        led.value(1)
        
#funkcia pre spustanie tlacidla a overenie ci je tlacidlo stlacne znova pre vypnutie svetla
def run():
    #ak nie je hodnota pre tlacidlo 1 tak je svetlo pre tuto poziciu na zaciatku zhasnute
    if not button.value():
        time.sleep_ms(20)
        #ked dojde k zmene stavu svetla na tlacidlu tak sa spusti reverseGPIO() azmeni sa hodnota led na to aby svietila albo zhasla podla toho co je posledna hodnota
        if button.value():
            reverseGPIO()
            while button.value():
                time.sleep_ms(20)

#spusenie kodu
if __name__ == "__main__":
    try:
        while True:
            run()
    except:
        pass

