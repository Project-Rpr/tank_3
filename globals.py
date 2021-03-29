#ON/OFF
ON  = 1
OFF = 0

#旋回方向判定
LEFT    = 0
RIGHT   = 1

#旋回距離
TURN_D  = 30
#停止距離
STOP_D  = 15

#前進時間
F_time  = 0.1
#後退時間
B_time  = 0.5
#旋回時間
T_time  = 0.5
#停止時間
S_time  = 1
#音声入力時間
V_time  = 2

#音声認識モジュール起動待ち時間
VOICE_WAIT = 5

#超音波センサ
TRIG = 17
ECHO = 27

#左後輪
LEFT_BACK_0         = 14
LEFT_BACK_1         = 15
LEFT_BACK_POWER     = 18
LEFT_BACK           = [LEFT_BACK_0, LEFT_BACK_1, LEFT_BACK_POWER]

#右後輪
RIGHT_BACK_0        = 23
RIGHT_BACK_1        = 24
RIGHT_BACK_POWER    = 25
RIGHT_BACK          = [RIGHT_BACK_0, RIGHT_BACK_1, RIGHT_BACK_POWER]

OUT_GPIOs   = [ TRIG,\
                LEFT_BACK_0, LEFT_BACK_1, LEFT_BACK_POWER,\
                RIGHT_BACK_0, RIGHT_BACK_1, RIGHT_BACK_POWER]
IN_GPIOs    = [ ECHO ]

