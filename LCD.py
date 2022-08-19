import lcddriver
from time import *

lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string("Jamie", 1)
lcd.lcd_display_string("Jess", 2)
