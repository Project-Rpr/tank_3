import globals as G
import debug
import spidev

VREF = 5
CALC10BIT = float(1023)

#SPIセットアップ
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

#距離リスト
D_list = [   6 ,  10 ,  15 ,  20 ,  30 ,  50 ,  60 ,  80 ]
#電圧リスト
V_list = [ 3.15, 2.3 , 1.65, 1.3 , 0.9 , 0.6 , 0.5 , 0.4 ]

def direction():
    left  = getDistance(G.LEFT)
    right = getDistance(G.RIGHT)

    if left > right:
        return G.LEFT
    else:
        return G.RIGHT

def getDistance(side):
    adc      = readAdc(side)
    volts    = convertVolts(adc)
    distance = convertDistance(volts)

    #デバッグ用
    if debug.print_side_distance == G.ON:
        if side == G.LEFT:
            print('側面距離(左) =', distance, 'cm')
        else:
            print('側面距離(右) =', distance, 'cm')

    return distance

def readAdc(channel):
    data = spi.xfer2([1, (8 + channel)<< 4, 200])
    adc  = ((data[1] & 0b11)<< 8) + data[2]

    #デバッグ用
    if debug.print_adc == G.ON:
        print("アナログ値 =", adc)

    return adc

def convertVolts(adc):
    volts = (adc * VREF) / CALC10BIT

    #デバッグ用
    if debug.print_volts == G.ON:
        print("入力電圧 = ", volts, "V")

    return volts

def convertDistance(volts):
    distance = 0

    if(V_list[-1] > volts)or(volts > V_list[0]):
        #デバッグ用
        if debug.print_side_distance == G.ON:
            print('out of range.')
    elif(V_list[0] >= volts)and(volts > V_list[1]):
        distance = calcDistance(D_list[0],D_list[1],V_list[0],V_list[1],volts)
    elif(V_list[1] >= volts)and(volts > V_list[2]):
        distance = calcDistance(D_list[1],D_list[2],V_list[1],V_list[2],volts)
    elif(V_list[2] >= volts)and(volts > V_list[3]):
        distance = calcDistance(D_list[2],D_list[3],V_list[2],V_list[3],volts)
    elif(V_list[3] >= volts)and(volts > V_list[4]):
        distance = calcDistance(D_list[3],D_list[4],V_list[3],V_list[4],volts)
    elif(V_list[4] >= volts)and(volts > V_list[5]):
        distance = calcDistance(D_list[4],D_list[5],V_list[4],V_list[5],volts)
    elif(V_list[5] >= volts)and(volts > V_list[6]):
        distance = calcDistance(D_list[5],D_list[6],V_list[5],V_list[6],volts)
    elif(V_list[6] >= volts)and(volts > V_list[7]):
        distance = calcDistance(D_list[6],D_list[7],V_list[6],V_list[7],volts)
    else:
        pass

    return distance

def calcDistance(D_S, D_L, V_L, V_S, volts):
    Ddiff = (D_L - D_S)
    Vdiff = (V_L - V_S)
    Vcalc = (V_L - volts) * 100

    cmPer0_01V = (Ddiff / Vdiff) / 100

    Dcalc = (Vcalc * cmPer0_01V)
    distance = (D_S + Dcalc)

    return distance

def judge():
    sideDirection = direction()

    return sideDirection

