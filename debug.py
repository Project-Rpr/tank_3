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


#前面距離の出力 (ON/OFF)
print_front_distance = G.OFF
#アナログ値の出力   (ON/OFF)
print_adc            = G.ON
#入力電圧値の出力   (ON/OFF)
print_volts          = G.ON
#側面距離の出力     (ON/OFF)
print_side_distance = G.ON
#動作制御命令の出力 (ON/OFF)
print_motor         = G.ON



#########################
#   front.py            #
#########################
#前面距離測定
def front_distance():
    print('前面距離 =', math.floor(front.distance()), 'cm')

#########################
#   side.py             #
#########################
#旋回方向決定
def side_judge():
    print(side.judge())
    time.sleep(A_time)

#側面距離測定
def side_distance():
    print(side.judge())
    time.sleep(A_time)

#########################
#   motor.py            #
#########################
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

#########################
#   voice_rec.py        #
#########################
#自動音声入力
def auto_voice():
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


def debug():
    #音声認識機能起動待ち
    time.sleep(G.VOICE_WAIT)
    while not G.quit:
        print("デバッグ")
        #front_distance()
        #side_judge()
        #side_distance()
        #auto_motor()
        #auto_voice()
        #manual_voice()

        time.sleep(1)
