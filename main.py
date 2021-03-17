import globals as G
import self_driving
import voice_rec
import debug

import RPi.GPIO as GPIO
import spidev
import sys
import concurrent.futures


#音声入力モード初期設定
#tank    = 0
#voice   = 1
#mode = tank
quit = False


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
        #SPIセットアップ
        spi = spidev.SpiDev()
        #初期化
        init()
        #デバッグ
        debug.test()

        #マルチプロセス実行
        #executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
        #自動運転機能
        #executor.submit(self_driving.func)
        #音声認識機能
        #executor.submit(voice_rec.func)
        #デバッグ
        #executor.submit(debug.func)

        #マルチプロセス実行
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            #自動運転機能
            executor.submit(self_driving.func)
            #音声認識機能
            executor.submit(voice_rec.func)
            #デバッグ
            executor.submit(debug.func)

    except KeyboardInterrupt:
        quit = True
        GPIO.cleanup()
        spi.close()
        #executor.shutdown()
        #print("プログラムを終了します")
        #sys.exit(0)
        sys.exit("プログラムを終了します")
