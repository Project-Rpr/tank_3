import main as M
import debug
import RPi.GPIO as GPIO
import time

ON  = GPIO.HIGH
OFF = GPIO.LOW

rec_time = 2

def word_check(word):

    #自動運転モードのみの場合
    if M.mode == M.tank:
        if 'スタート' in word\
        or 'すたーと' in word:
            voice_mode_ON()     #音声入力受付状態開始
            M.mode = M.voice
        else:
            pass                #DO NOTHING
    
    #音声入力受付状態の場合
    elif M.mode == M.voice:
        #停止
        if 'ストップ' in word\
        or 'すとっぷ' in word\
        or 'スタート' in word\
        or 'すたーと' in word:
            stop()
        #前進
        elif '前' in word:
            forward()

        #右旋回
        elif '右' in word:
            t_Right()

        #左旋回
        elif '左' in word:
            t_Left()

        #その他
        else:
            pass

    time.sleep(rec_time)

def voice_mode_ON():
    pass

def forward():
    pass

def t_Right():
    pass

def t_Left():
    pass

def stop():
    pass
