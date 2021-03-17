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


#前面距離の出力     (ON/OFF)
print_front_distance = \
G.OFF
#アナログ値の出力   (ON/OFF)
print_adc            = \
G.ON
#入力電圧値の出力   (ON/OFF)
print_volts          = \
G.ON
#側面距離の出力     (ON/OFF)
print_side_distance  = \
G.ON
#動作制御命令の出力 (ON/OFF)
print_motor          = \
G.ON


#前面距離測定       (ON/OFF)
front_distance_test = \
G.OFF
#側面距離測定       (ON/OFF)
side_distance_test  = \
G.OFF
#動作制御           (ON/OFF)
auto_motor_test     = \
G.OFF
#自動音声入力       (ON/OFF)
auto_voice_test     = \
G.OFF
#G.ON
#手動音声入力       (ON/OFF)
manual_voice_test   = \
G.OFF


#########################
#   front.py            #
#########################
#前面距離測定
def front_distance():
    print('前面距離 =', math.floor(front.distance()), 'cm')

#########################
#   side.py             #
#########################
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
    time.sleep(A_time)

    word = 'スタート'
    print(word)
    word_check.word_check(word)
    time.sleep(A_time)

    word = '前進'
    print(word)
    word_check.word_check(word)
    time.sleep(A_time)

    word = '右'
    print(word)
    word_check.word_check(word)

    word = '左'
    print(word)
    word_check.word_check(word)
    time.sleep(A_time)

    word = 'ストップ'
    print(word)
    word_check.word_check(word)
    time.sleep(A_time)

    word = 'スタート'
    print(word)
    word_check.word_check(word)
    time.sleep(A_time)

#手動音声入力
def manual_voice():
    print('語句を入力')
    word = input()
    word_check.word_check(word)


def test():
    while not M.quit:
        #前面距離測定
        if front_distance_test == G.ON:
            front_distance()
            continue

        #側面距離測定
        if side_distance_test == G.ON:
            side_distance()
            continue

        #動作制御
        if auto_motor_test == G.ON:
            auto_motor()
            continue

        break

def func():
    #音声認識機能起動待ち
    time.sleep(G.VOICE_WAIT)
    while not M.quit:
        #print("デバッグ")
        
        time.sleep(1)
        #自動音声入力
        if auto_voice_test == G.ON:
            auto_voice()
            continue
        #自動音声入力
        if manual_voice_test == G.ON:
            manual_voice()
            continue

        break
