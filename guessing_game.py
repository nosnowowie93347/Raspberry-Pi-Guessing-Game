# ODI0NzIxNzc5MzIxNzMzMTYw.YFzgAg.7QK1022XWfl9ZJe-S-TDJ4X27Lk
import random
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)


n = random.randint(1, 99)

guess = int(input("Enter an integer from 1 to 99: "))

while n != "guess":

  print

  if guess < n:

    print("guess is low")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(18,GPIO.LOW)
    guess = int(input("Enter an integer from 1 to 99: "))

  elif guess > n:

    print ("guess is high")
    GPIO.output(27,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(27,GPIO.LOW)
    guess = int(input("Enter an integer from 1 to 99: "))

  else:

    print ("you guessed it!")
    GPIO.output(17,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(17,GPIO.LOW)

    break
