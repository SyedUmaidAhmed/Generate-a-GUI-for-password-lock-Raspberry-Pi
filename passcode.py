
import RPi.GPIO as GPIO
from guizero import App, Text, warn, TextBox, PushButton,info
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

pwm=GPIO.PWM(8,50)
pwm.start(0)
app = App(title="TREASURE BOX", height=280, width=600)
message = Text(app, text="\n\n Please Enter your password to Login ! \n", size=18,font="Arial")
my_input = TextBox(app)


def do_nothing():
    c = my_input.get()
    if c=="treasure":
        info("BEST", "You are welcomed !")
        pwm.ChangeDutyCycle(4)
        GPIO.output(16,GPIO.HIGH)
        sleep(3)
        GPIO.output(16,GPIO.LOW)
        

    else:
        warn("BAD!", "Please Try again !")
        GPIO.output(10,GPIO.HIGH)
        sleep(3)
        GPIO.output(10,GPIO.LOW)






message2 = Text(app, text=" ", size=18,font="Arial")


Button = PushButton(app,text = "Check Passocde", command=do_nothing, padx=30, pady=20)

 
app.display()
