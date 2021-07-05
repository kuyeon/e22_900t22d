import Jetson.GPIO as GPIO

print("Module 1 Setting pin is M0: 11, M1: 12 and Module 2 Setting pin is M0: 35, M1: 36")
M0_PIN = int(input("Input Pin number 'M0': "))
M1_PIN = int(input("Input Pin number 'M1': "))
#AUX_PIN = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(M0_PIN, GPIO.OUT)
GPIO.setup(M1_PIN, GPIO.OUT)
#GPIO.setup(AUX_PIN, GPIO.IN)

print("Select Mode ---> '0: Normal', '1: WOR', '2: Configuration', '3: Deep Sleep")
mode = input("Input Mode Number: ")

if mode == 0:
    # Normal : Mode0
    GPIO.output(M0_PIN, GPIO.LOW)
    GPIO.output(M1_PIN, GPIO.LOW)
elif mode == 1:
    # WOR : Mode1
    GPIO.output(M0_PIN, GPIO.HIGH)
    GPIO.output(M1_PIN, GPIO.LOW)
elif mode == 2:
    # Configuration : Mode2
    GPIO.output(M0_PIN, GPIO.LOW)
    GPIO.output(M1_PIN, GPIO.HIGH)
elif mode == 3:
    # Deep Sleep : Mode3
    GPIO.output(M0_PIN, GPIO.HIGH)
    GPIO.output(M1_PIN, GPIO.HIGH)

