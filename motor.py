import globals as G
import debug

import RPi.GPIO as GPIO

P = 2   #電源(POWER)

#駆動輪_正転(FORWARD)
def roll_F(wheel):
    GPIO.output(wheel[0], GPIO.HIGH)
    GPIO.output(wheel[1], GPIO.LOW)
    GPIO.output(wheel[P], GPIO.HIGH)

#駆動輪_後転(BACK)
def roll_B(wheel):
    GPIO.output(wheel[0], GPIO.LOW)
    GPIO.output(wheel[1], GPIO.HIGH)
    GPIO.output(wheel[P], GPIO.HIGH)

#駆動輪_停止(STOP)
def roll_S(wheel):
    GPIO.output(wheel[0], GPIO.LOW)
    GPIO.output(wheel[1], GPIO.LOW)
    GPIO.output(wheel[P], GPIO.LOW)


#動作制御_
def forward():
    roll_F(G.LEFT_BACK)
    roll_F(G.RIGHT_BACK)
    #デバッグ用
    if debug.print_motor == G.ON:
        print("前進")

#動作制御_左旋回
def t_left():
    roll_B(G.LEFT_BACK)
    roll_F(G.RIGHT_BACK)
    #デバッグ用
    if debug.print_motor == G.ON:
        print("左旋回")

#動作制御_右旋回
def t_right():
    roll_F(G.LEFT_BACK)
    roll_B(G.RIGHT_BACK)
    #デバッグ用
    if debug.print_motor == G.ON:
        print("右旋回")

#動作制御_後退
def back():
    roll_B(G.LEFT_BACK)
    roll_B(G.RIGHT_BACK)
    #デバッグ用
    if debug.print_motor == G.ON:
        print("後退")

#動作制御_停止
def stop():
    roll_S(G.LEFT_BACK)
    roll_S(G.RIGHT_BACK)
    #デバッグ用
    if debug.print_motor == G.ON:
        print("停止")

