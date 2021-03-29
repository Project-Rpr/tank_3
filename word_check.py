import main as M
import globals as G
import debug
import time


rec_time = 2

S = G.OFF   #停止フラグ
F = G.OFF   #前進フラグ
L = G.OFF   #左旋回フラグ
R = G.OFF   #右旋回フラグ
C = G.OFF   #チャタリングフラグ

def func(word):
    global S, F, L, R, C

    #停止
    if 'ストップ' in word\
    or 'すとっぷ' in word:
        S = G.ON
        C = G.ON
        #デバッグ用
        if debug.print_flags == G.ON:
            print("SフラグON")
    #前進
    elif '前' in word:
        F = G.ON
        C = G.ON
        #デバッグ用
        if debug.print_flags == G.ON:
            print("FフラグON")
    #左旋回
    elif '左' in word:
        L = G.ON
        C = G.ON
        #デバッグ用
        if debug.print_flags == G.ON:
            print("LフラグON")
    #右旋回
    elif '右' in word:
        R = G.ON
        C = G.ON
        #デバッグ用
        if debug.print_flags == G.ON:
            print("RフラグON")
    #その他
    else:
        pass

    time.sleep(rec_time)
    S = G.OFF
    F = G.OFF
    L = G.OFF
    R = G.OFF
    C = G.OFF

