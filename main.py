import voice_rec
import debug
import RPi.GPIO as GPIO
import sys

#GPIO初期化
MODE_PIN    = 12
FORWARD_PIN = 16
RIGHT_PIN   = 20
LEFT_PIN    = 21

#音声入力モード初期設定
tank    = 0
voice   = 1
mode = tank

if __name__=="__main__":
    #GPIO設定    
    GPIOs = [MODE_PIN, FORWARD_PIN, RIGHT_PIN, LEFT_PIN]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOs, GPIO.OUT)
    GPIO.output(GPIOs, GPIO.LOW)

    try:
        #デバッグ用
        #while True:
            #debug.auto()   #自動デバッグ
            #debug.manual()  #手動デバッグ

        #voice_recクラスのインスタンスを生成
        voice_rec_start = voice_rec.voice_rec()

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("プログラムを終了します")
        sys.exit(0)
