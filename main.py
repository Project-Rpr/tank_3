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


def init():
    #GPIO初期化
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(G.OUT_GPIOs, GPIO.OUT)
    GPIO.setup(G.IN_GPIOs, GPIO.IN)

    #GPIOクリーンアップ
    GPIO.output(G.OUT_GPIOs, GPIO.LOW)

if __name__=='__main__':
    try:
        #デバッグ用
        #while True:
            #debug.front_distance()  #前面距離測定
            #debug.side_distance()   #側面距離測定
            #debug.auto_motor()      #動作制御
            #debug.auto_voice()      #自動音声入力
            #debug.manual_voice()    #手動音声入力

        #voice_recクラスのインスタンスを生成
        #voice_rec_start = voice_rec.voice_rec()

        #変数宣言&初期化
        f_distance  = 0     #前面距離
        t_flag      = 0     #左右判定フラグ

        #初期化
        init()

        while True:
            #前面距離を取得
            f_distance = front.distance()

            #前面距離が「停止距離」未満の場合
            if f_distance < G.STOP_D:
                #動作前停止
                motor.stop()
                time.sleep(G.S_time)
                
                #停止
                time.sleep(G.S_time)
                
                #後退
                motor.back()
                time.sleep(G.B_time)
                
                #動作後停止
                motor.stop()
                time.sleep(G.S_time)

                
            #前面距離が「停止距離」以上「旋回距離」未満の場合
            elif (f_distance >= G.STOP_D) and (f_distance < G.TURN_D):
                #動作前停止
                motor.stop()
                time.sleep(G.S_time)
                
                #旋回方向の決定
                t_flag = side.judge()

                #旋回方向が「右」の場合
                if t_flag == G.RIGHT:
                    motor.t_right()

                #旋回方向が「左」の場合
                else:
                    motor.t_left()

                while f_distance < G.TURN_D:
                    f_distance = front.distance()
                    time.sleep(G.T_time)

                #動作後停止
                motor.stop()
                time.sleep(G.S_time)
                

            #前面距離が「旋回距離」以上の場合
            elif f_distance >= G.TURN_D:
                motor.forward()


    except KeyboardInterrupt:
        GPIO.cleanup()
        spi.close()
        print("プログラムを終了します")
        sys.exit(0)

