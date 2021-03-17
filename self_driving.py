import main as M
import globals as G
import front
import side
import motor
import debug
import word_check as WC

import RPi.GPIO as GPIO
import time


def func():
    #音声認識機能起動待ち
    time.sleep(G.VOICE_WAIT)

    #変数宣言&初期化
    f_distance  = 0     #前面距離
    t_flag      = 0     #旋回方向判定フラグ

    while not M.quit:
        #音声入力確認
        if WC.C == G.OFF:
            voice_input()
        
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

def voice_input():
    #print(WC.S, WC.F, WC.L, WC.R, WC.C)

    if WC.S == G.ON:
        print("停止(音声入力)")
        #動作前停止
        motor.stop()
        time.sleep(G.S_time)
        #音声入力による制御
        time.sleep(G.S_time)

    elif WC.F == G.ON:
        print("前進(音声入力)")
        #動作前停止
        motor.stop()
        time.sleep(G.S_time)
        #音声入力による制御
        motor.forward()

    elif WC.L == G.ON:
        print("左旋回(音声入力)")
        #動作前停止
        motor.stop()
        time.sleep(G.S_time)
        #音声入力による制御
        motor.t_left()
        time.sleep(G.T_time)

    elif WC.R == G.ON:
        print("右旋回(音声入力)")
        #動作前停止
        motor.stop()
        time.sleep(G.S_time)
        #音声入力による制御
        motor.t_right()
        time.sleep(G.T_time)

