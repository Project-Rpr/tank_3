import globals as G
import front
import voice_rec
import debug

import RPi.GPIO as GPIO
import math
import sys


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

if __name__=="__main__":
    init()

    try:
        #デバッグ用
        #while True:
            #debug.auto()   #自動デバッグ
            #debug.manual()  #手動デバッグ

        #voice_recクラスのインスタンスを生成
        #voice_rec_start = voice_rec.voice_rec()

        while True:
            print("前面距離 = ", math.floor(front.distance()), "cm")

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("プログラムを終了します")
        sys.exit(0)

