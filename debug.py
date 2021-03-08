import main as M
import RPi.GPIO as GPIO
import word_check

#自動
def auto():
    word = 'こんにちは'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = 'スタート'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = '前進'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = '右'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = '左'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = 'ストップ'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

    word = 'スタート'
    print(word)
    word_check.word_check(word)
    time.sleep(debug_time)

#手動
def manual():
    print('語句を入力')
    word = input()
    word_check.word_check(word)

def read_GPIO():
    print('MODE_PIN:' + str(GPIO.input(M.MODE_PIN)))
    print('FORWARD_PIN:' + str(GPIO.input(M.FORWARD_PIN)))
    print('RIGHT_PIN:' + str(GPIO.input(M.RIGHT_PIN)))
    print('LEFT_PIN:' + str(GPIO.input(M.LEFT_PIN))) 
