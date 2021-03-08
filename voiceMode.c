#include "main.h"
#include "debug.h"


void voiceMode_ON(void){
    printf("音声入力モード開始\n");
    stop();delay(VOICE_MODE_TIME);

}

void voiceMode(void){
#if GPIO_READ == ON
    gpio_read();
#endif

    /*前進*/
    if( (digitalRead(FORWARD_PIN)==HIGH)    &&
        (digitalRead(RIGHT_PIN)==LOW)       &&
        (digitalRead(LEFT_PIN)==LOW)){

    #if (DEBUG_VOICE_MODE == ON) || (GPIO_READ == ON)
        printf("voiceMode forward()\n");
    #endif
        stop();delay(VOICE_MODE_TIME);
        forward();delay(FORWARD);

    /*右旋回*/
    }else if((digitalRead(FORWARD_PIN)==LOW)&&
            (digitalRead(RIGHT_PIN)==HIGH)  &&
            (digitalRead(LEFT_PIN)==LOW)){

    #if (DEBUG_VOICE_MODE == ON) || (GPIO_READ == ON)
        printf("voiceMode t_Right()\n");
    #endif
        stop();delay(VOICE_MODE_TIME);
        t_Right();delay(TURN);

    /*左旋回*/
    }else if((digitalRead(FORWARD_PIN)==LOW)&&
            (digitalRead(RIGHT_PIN)==LOW)   &&
            (digitalRead(LEFT_PIN)==HIGH)){

    #if (DEBUG_VOICE_MODE == ON) || (GPIO_READ == ON)
        printf("voiceMode t_Left()\n");
    #endif
        stop();delay(VOICE_MODE_TIME);
        t_Left();delay(TURN);

    /*停止*/
    }else if((digitalRead(FORWARD_PIN)==LOW)&&
            (digitalRead(RIGHT_PIN)==LOW)   &&
            (digitalRead(LEFT_PIN)==LOW)){

    #if (DEBUG_VOICE_MODE == ON) || (GPIO_READ == ON)
        printf("voiceMode stop()\n");
    #endif
        stop();delay(VOICE_MODE_TIME);
        stop();delay(STOP);

    }
}
