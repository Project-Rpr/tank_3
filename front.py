import globals as G
import debug
import time
import RPi.GPIO as GPIO

def distance():
    GPIO.output(G.TRIG, GPIO.HIGH)
    time.sleep(0.01)
    GPIO.output(G.TRIG, GPIO.LOW)

    while GPIO.input(G.ECHO) == 0:
        pass
    s_time = time.time()

    while GPIO.input(G.ECHO) == 1:
        pass
    e_time = time.time()

    duration = (e_time - s_time)
    front_distance = (duration / 2) * 34350
    #デバッグ用
    if debug.print_front_distance == G.ON:
        print("前面距離 =", front_distance, "cm")
    return front_distance
