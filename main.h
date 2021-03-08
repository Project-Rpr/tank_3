/************************
*   ヘッダーファイル    *
************************/
#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiSPI.h>
#include <unistd.h>
#include <stdint.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

/****************
*   マクロ定数  *
****************/
/*main.c*/
#define MODE_PIN    12
#define FORWARD_PIN 16
#define RIGHT_PIN   20
#define LEFT_PIN    21

#define TRIG        17
#define ECHO        27

#define MOTOR1      14
#define MOTOR2      15
#define MOTOR3      23
#define MOTOR4      24
#define MOTOR1_2    18
#define MOTOR3_4    25

#define LEFT        1
#define RIGHT       2

#define EMERGENCY_STOP_D    15
#define STOP_D              30

#define FORWARD             100
#define BACK                500
#define TURN                500
#define STOP                1000
#define VOICE_MODE_TIME     2000

/*sideDistance.c*/
#define TRUE                    (1==1)
#define FALSE                   (!TRUE)
#define CHAN_CONFIG_SINGLE      8
#define BUFFER_SIZE             3
#define VOLT                    5       //3.3V or 5.0V
#define VREF                    5       //3.3V or 5.0V
#define CALC10BIT               (float)1023

/*motor.c*/
#define F   2                   /*forward*/
#define B   1                   /*back*/
#define S   0                   /*stop*/

/*distance.c*/
#define ON  1
#define OFF 0

/*debug.c*/
#define DEBUG_MODE_PIN      6
#define DEBUG_FORWARD_PIN   13
#define DEBUG_RIGHT_PIN     19
#define DEBUG_LEFT_PIN      26

#define RAND            10
#define MANUAL_V        20
#define MANUAL_D        30
#define DETAIL          40
#define MANUAL          50

/****************************
*   関数プロトタイプ宣言    *
****************************/
/*distance.c*/
double frontDistance(void);

/*sideDistance.c*/
int sideDistance(void);

/*motor.c*/
void forward(void);     //前進
void stop(void);        //停止
void t_Right(void);     //右旋回
void t_Left(void);      //左旋回
void back(void);        //後退

/*voice_mode.c*/
void voiceMode_ON(void);
void voiceMode(void);

/*debug.c*/
void debug_voiceMode(void);
void gpio_read(void);
