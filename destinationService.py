import math,coord_extractor,publisher,json,time,RPi.GPIO as GPIO

lat = input("Latitude: ")
longit=input("Longitude: ")
#print lat,longit
lastDistance=20000

LCD_RS = 25
LCD_E  = 24
LCD_D4 = 23
LCD_D5 = 17
LCD_D6 = 18
LCD_D7 = 22
 
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False
 
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0


E_PULSE = 0.0005
E_DELAY = 0.0005

def main():
 
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LCD_E, GPIO.OUT)
  GPIO.setup(LCD_RS, GPIO.OUT)
  GPIO.setup(LCD_D4, GPIO.OUT)
  GPIO.setup(LCD_D5, GPIO.OUT)
  GPIO.setup(LCD_D6, GPIO.OUT)
  GPIO.setup(LCD_D7, GPIO.OUT)
 
  lcd_init()

def lcd_init():

  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
 
  GPIO.output(LCD_RS, mode)
 
 
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)
 
  lcd_toggle_enable()

  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)
 
  lcd_toggle_enable()

def lcd_toggle_enable():

  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)
 
def lcd_string(message,line,style):

 
  if style==1:
    message = message.ljust(LCD_WIDTH," ")
  elif style==2:
    message = message.center(LCD_WIDTH," ")
  elif style==3:
    message = message.rjust(LCD_WIDTH," ")
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

try:
  main()
 

  while(True):
  	 time.sleep(5)

    x=coord_extractor.getCoords(lat,longit)

    distance=abs(float(lat)-float(x['latitude']))+abs(float(longit)-float(x['longitude']))

    R = 6371e3
    fi1 = math.radians(x['latitude'])
    fi2 = math.radians(lat)
    deltafi = math.radians(lat-x['latitude'])
    deltalambda = math.radians(longit-x['longitude'])
    a = math.sin(deltafi/2) * math.sin(deltafi/2) + math.cos(fi1) * math.cos(fi2) * math.sin(deltalambda/2) * math.sin(deltalambda/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c / 1000


    oldDistance=publisher.getFromFirebase()

    print oldDistance
    print distance
    if float(distance)<0.3:
        lcd_string("Destination reached",LCD_LINE_1,2)
        break
    elif abs(float(distance)-float(oldDistance))<=0.3 :
                lcd_string("You are not moving",LCD_LINE_1,2)
                lcd_string("Distance: "+str(distance),LCD_LINE_2,2)
    elif float(distance)>float(oldDistance):
                lcd_string("Distance larger", LCD_LINE_1,2)
                lcd_string(str(distance),LCD_LINE_2,2)
    else:
                lcd_string("Distance remaining:",LCD_LINE_1,2)
                lcd_string(str(distance),LCD_LINE_2,2)


except KeyboardInterrupt:
  pass
finally:
  lcd_byte(0x01, LCD_CMD)
  lcd_string("Destination",LCD_LINE_1,2)
  lcd_string("Reached",LCD_LINE_2,2)
  GPIO.cleanup()