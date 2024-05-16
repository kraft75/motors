"""
Steuere den Schrittmotor so, dass er nach einem Startimpuls in den
Automatikbetrieb wechselt.
Durch einen Stoppimpuls soll der Antrieb zum Stillstand gebracht werden. 

Automatikbetrieb: 
Der Motor pendelt beim Start einmal zwischen 0° und 90°.
Im Anschluss pendelt der Motor ohne Halt zwischen +90° und -90°,
bis eine Abbruchbedingung eintritt.   

Sicherheitsbedingung:  
Das Programm und die Verdrahtung sind drahtbruchsicher auszuführen. 

Ein Abbruch ist jederzeit mittels Not-Halt-Taster möglich.
Stepper.py
"""
from machine import Pin, SoftI2C
import Stepper
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

""" Pins für den Motor, per Interface """
in1 = Pin(14,Pin.OUT)
in2 = Pin(27,Pin.OUT)
in3 = Pin(26,Pin.OUT)
in4 = Pin(25,Pin.OUT)
#Not-Halt-Taster
on = Pin(32, Pin.IN, Pin.PULL_UP)
check = Pin(13, Pin.OUT)
check.value() = 0
""" Schrittmotor """
s1 = Stepper.create(in1, in2, in3, in4)

""" LCD einrichten """
# LCD Speicheradresse und Größenangabe des Bildschirms
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
# I2C mit Pins und gegebener Taktung
i2c = SoftI2C(scl = Pin(22), sda = Pin(21), freq = 10000)
# LCD-Monitor
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

counter = 0
while counter <= 3:
    lcd.clear()
    
    an = on.value()
    
    
    if counter == 0:
        free = check.value() + halt
        if free == 1:
            break
        else:
            s1 = Stepper.create(in1, in2, in3, in4, delay = 4)
            s1.angle(0)
            s1.angle(90)
        
    else:
    
        free = check.value() + halt
        
        if free == 1:
            break
        else:
            s1 = Stepper.create(in1, in2, in3, in4)
            s1.angle(90, -1)
            s1.angle(90)
        
        
    counter += 1
    lcd.putstr("Counter " + str(counter))
    sleep(0.3)
    

