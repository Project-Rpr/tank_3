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

    debug.read_GPIO()   #デバッグ
    time.sleep(rec_time)
    #print('cleanup')    #デバッグ
    cleanup()
    #debug.read_GPIO()   #デバッグ

def voice_mode_ON():
    GPIO.output(M.MODE_PIN, ON)
    GPIO.output(M.FORWARD_PIN, OFF)
    GPIO.output(M.RIGHT_PIN, OFF)
    GPIO.output(M.LEFT_PIN, OFF)

def forward():
    GPIO.output(M.MODE_PIN, ON)
    GPIO.output(M.FORWARD_PIN, ON)
    GPIO.output(M.RIGHT_PIN, OFF)
    GPIO.output(M.LEFT_PIN, OFF)
    #print('python_forward')         #デバッグ

def t_Right():
    GPIO.output(M.MODE_PIN, ON)
    GPIO.output(M.FORWARD_PIN, OFF)
    GPIO.output(M.RIGHT_PIN, ON)
    GPIO.output(M.LEFT_PIN, OFF)
    #print('python_right')           #デバッグ

def t_Left():
    GPIO.output(M.MODE_PIN, ON)
    GPIO.output(M.FORWARD_PIN, OFF)
    GPIO.output(M.RIGHT_PIN, OFF)
    GPIO.output(M.LEFT_PIN, ON)
    #print('python_left')            #デバッグ

def stop():
    GPIO.output(M.MODE_PIN, ON)
    GPIO.output(M.FORWARD_PIN, OFF)
    GPIO.output(M.RIGHT_PIN, OFF)
    GPIO.output(M.LEFT_PIN, OFF)
    #print('python_stop')            #デバッグ

def cleanup():
    GPIO.output(M.MODE_PIN, OFF)
    GPIO.output(M.FORWARD_PIN, OFF)
    GPIO.output(M.RIGHT_PIN, OFF)
    GPIO.output(M.LEFT_PIN, OFF)
