import requests
import RPi.GPIO as GPIO
from time import sleep

#LED 1
blue1 = 14
#LED 2
blue2 = 15
#LED 3
blue3 = 18
#LED 4
blue4 = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(blue1, GPIO.OUT)
GPIO.setup(blue2, GPIO.OUT)
GPIO.setup(blue3, GPIO.OUT)
GPIO.setup(blue4, GPIO.OUT)
#setting all colours off
GPIO.output(blue1, 0)
GPIO.output(blue2, 0)
GPIO.output(blue3, 0)
GPIO.output(blue4, 0)

#destroy method turns off led and cleans gpio for next use
def destroy():
        GPIO.output(blue1, 0)
        GPIO.output(blue2, 0)
        GPIO.output(blue3, 0)
        GPIO.output(blue4, 0)
        print("goodbye :)")
        GPIO.cleanup()

try:
    while True:
        #json data
        url = "http://api.open-notify.org/astros.json"
        r = requests.get(url)
        data = r.json()
        people = data['number']
        print(people)

        if people == 0:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 0)
        
        elif people == 1:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 1)

        elif people == 2:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 0)   
                
        elif people == 3:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 1)

        elif people == 4:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 0)   
            
        elif people == 5:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 1)

        elif people == 6:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 0)   
                
        elif people == 7:
            GPIO.output(blue1, 0)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 1)

        elif people == 8:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 0)   
                
        elif people == 9:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 1)

        elif people == 10:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 0)   
            
        elif people == 11:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 0)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 1)

        elif people == 12:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 0)   
                
        elif people == 13:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 0)
            GPIO.output(blue4, 1)

        elif people == 14:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 0)   
                
        elif people == 15:
            GPIO.output(blue1, 1)
            GPIO.output(blue2, 1)
            GPIO.output(blue3, 1)
            GPIO.output(blue4, 1)

        sleep(60)

except KeyboardInterrupt:
    destroy()
