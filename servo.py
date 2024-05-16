from machine import Pin, PWM, ADC, SoftI2C
from time import sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

"""
Ein Servomotor wird als Stellmotor in einer Lüftungssteuerung vorgesehen.

Der Stellwert (Sollposition) wird jedoch durch eine übergeordnete Steuerung als
Analogwert übertragen. Dies kannst du mittels Potentiometer simulieren.  

Der Sollwert soll in vollem Spektrum (0-4080) in 1°-Schritten auf 180° aufgelöst werden.  

Zusatz: Stelle den Sollwert und den Istwert auf einem LCD dar. 

Verwende für diese Aufgabe die Tools uPyCraft und Fritzing. 
"""


""" Bestimmung des gesuchten Winkels """

def intervall_mapping(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

""" vesrsion aus dem internet """
def servoFunction(degrees):     #rotate servo arm to degrees position
# limit degrees beteen 0 and 180
    if degrees > 180:
        degrees=180
    if degrees < 0:
        degrees=0
    # set max and min duty
    maxDuty=9000
    minDuty=1000
    # new duty is between min and max duty in proportion to its value
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    # servo PWM value is set
    servo.duty_u16(int(newDuty))   

""" Größen definieren """
adc = ADC(Pin(36))
# Servomotor wird über PWM gesteuert
servo = PWM(Pin(14))
servo.freq(50)
# Variable für die Pause in der while-Schleife
PAUSE = 0.001

""" LCD einrichten """
# LCD Speicheradresse und Größenangabe des Bildschirms
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
# I2C mit Pins und gegebener Taktung
i2c = SoftI2C(scl = Pin(22), sda = Pin(21), freq = 10000)
# LCD-Monitor
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

""" Ausgabe auf dem Display """
while True:
    lcd.clear()
    
    #wert = adc.read ()
    wert = adc.read_u16()
    grad = (wert * 180) / 65500
    #if grad > 180: degrees = 180
    #if grad < 0: degrees = 0
    #servo.duty(intervall_mapping(grad, 0, 180, 20, 128))
    print(wert)
    lcd.putstr("Value: " + str(wert))
    lcd.putstr("\nDeg: " + str(grad))
    servoFunction(int(grad))
    sleep(PAUSE)
