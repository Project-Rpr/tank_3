import globals as G
import front
import side
import motor
import voice_rec
import debug

import RPi.GPIO as GPIO
import spidev
import sys
import math
import subprocess
import time

#SPIセットアップ
spi = spidev.SpiDev()

#音声入力モード初期設定
tank    = 0
voice   = 1
mode = tank

A_time = 2

def front_test():
    print('前面距離 = ', math.floor(front.distance()), 'cm')

def side_test():
    print(side.judge())
    time.sleep(A_time)

def motor_test():
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

def init():
    #GPIO初期化
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(G.OUT_GPIOs, GPIO.OUT)
    GPIO.setup(G.IN_GPIOs, GPIO.IN)

    #GPIOクリーンアップ
    GPIO.output(G.OUT_GPIOs, GPIO.LOW)

if __name__=='__main__':
    #初期化
    init()

    try:
        #デバッグ用
        #while True:
            #debug.auto()   #自動デバッグ
            #debug.manual()  #手動デバッグ

        #voice_recクラスのインスタンスを生成
        #voice_rec_start = voice_rec.voice_rec()

        while True:
            front_test()
            side_test()
            motor_test()

    except KeyboardInterrupt:
        GPIO.cleanup()
        spi.close()
        print("プログラムを終了します")
        sys.exit(0)

