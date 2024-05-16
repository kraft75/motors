"""
Aufgabe: Potentialfreie Ansteuerung eines Lüfterrads


Taster sollen als Schaltglieder nicht mit dem Motorspannung in Berührung kommen,Steuerspannung
und Lastspannung sind grundsätzlich voneinander zu trennen. Controller ermöglichen in diesem
Zusammenhang das Speichern von elektrischen Signaländerungen.  

Steuerspannung: 	3.3 V 

Lastspannung: 5-9 V 



Verwende für die folgenden Aufgaben die Tools uPyCraft und Fritzing. 

a) Entwickle eine Schaltung, bei der du einen Gleichstrommotor mit einem Taster einschalten
und mit einem zweiten Taster wieder ausschalten kannst.  

b) Ergänze die Schaltung um ein Potentiometer. Mit dessen Hilfe kann der Motor von 0 bis Max
in seiner Drehzahl reguliert werden.  
"""

from machine import Pin, PWM, ADC, SoftI2C
from time import sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd


""" Potentiometer """
adc = ADC(Pin(4))
""" Pin-Belegungen für den Motor """
en = Pin(13, Pin.OUT)
# Bestimmen die Richtung
in1 = Pin(12, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in1.off()
in2.off()
button1 = Pin(2, Pin.IN, Pin.PULL_UP)
button2 = Pin(33, Pin.IN, Pin.PULL_UP)
""" PWM für den Motor. Kontrolliert Spannungszufuhr(Geschwindigkeit) """
pwm = PWM(en)
pwm.freq(500)

""" LCD einrichten """
# LCD Speicheradresse und Größenangabe des Bildschirms
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
# I2C mit Pins und gegebener Taktung
i2c = SoftI2C(scl = Pin(22), sda = Pin(21), freq = 10000)
# LCD-Monitor
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


while True:
    lcd.clear()
    
    wert = adc.read()
    #wert = adc.read_u16()
    #lcd.putstr("Value: " + str(wert))
    
    start = button1.value()
    #print("Start ini ", start)
    stop = button2.value()
    #print("Stop ini", stop)
    if start:
        print("Start ", start)
        in1.off()
        in2.on()
    else:
        pass
        duty_cycle = int(wert * 1023 / 4094)
        pwm.duty(duty_cycle)
        lcd.putstr("Value: " + str(duty_cycle ))
        sleep(0.2)
    
    if stop:
        print("Stop", stop)
        in1.on()
        in2.on()
    else:
        pass
        sleep(0.4)
    
    sleep(0.3)
    
    
    