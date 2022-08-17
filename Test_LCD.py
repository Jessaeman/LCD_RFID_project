#RFID
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#LCD
import lcddriver
from time import sleep, strftime
from subprocess import *
import time


#Relay setup
relay_1 = 5
relay_2 = 6

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_1, GPIO.OUT)
GPIO.setup(relay_2, GPIO.OUT)
   
GPIO.setwarnings(False)



reader = SimpleMFRC522()

lcd = lcddriver.lcd()
lcd.lcd_clear()
#lcd.lcd_device.write_cmd(LCD_NOBACKLIGHT)

MB34A1_antal_vaske = (3)
MB34A2_antal_vaske = (2)
MB34B1_antal_vaske = (4)
MB34B2_antal_vaske = (5)
MB34C_antal_vaske = (2)
MB34D_antal_vaske = (7)
MB34E_antal_vaske = (6)

MB34E = (9)

antal_vaske = ()


GPIO.setwarnings(False)  
  
def run_cmd(cmd):
    p = Popen(cmd, shell = True, stdout = PIPE)
    output = p.communicate() [0]
    return output


try:
  while True:
        
        
        lcd.lcd_clear()
        lcd.lcd_display_string("Venligst indlaes", 1)
        lcd.lcd_display_string("     kort", 2)
        
        id, text = reader.read()
        
        print (id)
        print(text)
        
        lcd.lcd_clear()
        lcd.lcd_display_string("     Hej", 1)
        sleep (1)
        lcd.lcd_display_string((text), 2)    
        sleep (1)
        antal_vaske = -1
        print (antal_vaske)
        lcd.lcd_clear()
        lcd.lcd_display_string("Resterende vaske", 1)
        lcd.lcd_display_string(str(antal_vaske), 2)
        sleep(5)
        lcd.lcd_clear()
        sleep(0.5)        
        GPIO.output(relay_1, False)
        GPIO.output(relay_2, False)
        lcd.lcd_display_string("  Vask/Toerrer", 1)
        lcd.lcd_display_string("     koerer", 2)
        sleep(10)
        lcd.lcd_clear()
        GPIO.output(relay_1, True)
        GPIO.output(relay_2, True)
        lcd.lcd_display_string("  Vask/Toerrer", 1)
        lcd.lcd_display_string("    Feardig!", 2)
        sleep(10)
        lcd.lcd_clear()
                                      
    
finally:
    GPIO.cleanup()
    
#while True:  #for uret til at koere kontinuerligt      
#        lcd.lcd_display_string("Venligst", 1)
#        sleep(2)
#        lcd.lcd_clear()
#        lcd.lcd_display_string("Indlaes", 1)
#        lcd.lcd_display_string("kort", 2)
#        sleep(5)
#        lcd.lcd_clear()
#        sleep(0.5)
#        lcd.lcd_clear()
 
#        lcd.lcd_display_string(strftime('    ''%H:%M:%S '), 1)
#        lcd.lcd_display_string(strftime('%a %d %b %Y'), 2)        
    
  
    
    
