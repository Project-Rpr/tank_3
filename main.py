import globals as G
import front
import side
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

        #while True:
            #print('前面距離 = ', math.floor(front.distance()), 'cm')

        while True:
            print(side.judge())
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        spi.close()
        print("プログラムを終了します")
        sys.exit(0)

