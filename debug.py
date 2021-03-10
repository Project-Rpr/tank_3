import main as M
import globals as G
import front
import side
import motor
import word_check

import RPi.GPIO as GPIO
import math
import time

#動作時間(Active_time)
A_time = 2


#########################
#   front.py            #
#########################
#前面距離の出力 (ON/OFF)
print_front_distance = G.OFF

#########################
#   side.py             #
#########################
#アナログ値の出力   (ON/OFF)
print_adc            = G.OFF
#入力電圧値の出力   (ON/OFF)
print_volts          = G.OFF
#側面距離の出力     (ON/OFF)
print_side_distance = G.ON

#########################
#   motor.py            #
#########################
#動作制御命令の出力 (ON/OFF)
print_motor         = G.ON


#前面距離測定
def front_distance():
    print('前面距離 =', math.floor(front.distance()), 'cm')

#側面距離測定
def side_distance():
    print(side.judge())
    time.sleep(A_time)

#動作制御
def auto_motor():
    motor.forward()
    time.sleep(A_time)

    motor.t_left()
    time.sleep(A_time)

    motor.t_right()
    time.sleep(A_time)

    motor.back()
    time.sleep(A_time)

    motor.stop()
    time.sleep(A_time)

#自動音声入力
def autoi_voice():
    word = 'こんにちは'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = 'スタート'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = '前進'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = '右'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = '左'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = 'ストップ'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = 'スタート'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

#手動音声入力
def manual_voice():
    print('語句を入力')
    word = input()
    word_check.word_check(word)

def read_GPIO():
    print('MODE_PIN:' + str(GPIO.input(M.MODE_PIN)))
    print('FORWARD_PIN:' + str(GPIO.input(M.FORWARD_PIN)))
    print('RIGHT_PIN:' + str(GPIO.input(M.RIGHT_PIN)))
    print('LEFT_PIN:' + str(GPIO.input(M.LEFT_PIN))) 
