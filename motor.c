#include "main.h"
#include "debug.h"

void left_motor(int);
void right_motor(int);

void forward(void){
    int mode;

    mode =  F;
    left_motor(mode);
    right_motor(mode);

#if DEBUG_MOTOR == ON
    printf("forward\n");
#endif
}

void stop(void){
    int mode;

    mode =  S;
    left_motor(mode);
    right_motor(mode);

#if DEBUG_MOTOR == ON
    printf("stop\n");
#endif
}

void t_Right(void){
    int mode;

    mode =  F;
    left_motor(mode);

    mode =  B;
    right_motor(mode);

#if DEBUG_MOTOR == ON
    printf("t_Right\n");
#endif
}

void t_Left(void){
    int mode;

    mode =  B;
    left_motor(mode);

    mode =  F;
    right_motor(mode);

#if DEBUG_MOTOR == ON
    printf("t_Left\n");
#endif
}

void back(void){
    int mode;

    mode =  B;
    left_motor(mode);
    right_motor(mode);

#if DEBUG_MOTOR == ON
    printf("back\n");
#endif
}    

void left_motor(int mode){
    if(mode==F){
        digitalWrite(MOTOR1 , HIGH);
        digitalWrite(MOTOR2 , LOW);
        digitalWrite(MOTOR1_2 , HIGH);

    }else if(mode==B){
        digitalWrite(MOTOR1 , LOW);
        digitalWrite(MOTOR2 , HIGH);
        digitalWrite(MOTOR1_2 , HIGH);

    }else{
        digitalWrite(MOTOR1 , LOW);
        digitalWrite(MOTOR2 , LOW);
        digitalWrite(MOTOR1_2 , LOW);
    }
}

void right_motor(int mode){
    if(mode==F){
        digitalWrite(MOTOR3 , HIGH);
        digitalWrite(MOTOR4 , LOW);
        digitalWrite(MOTOR3_4 , HIGH);

    }else if(mode==B){
        digitalWrite(MOTOR3 , LOW);
        digitalWrite(MOTOR4 , HIGH);
        digitalWrite(MOTOR3_4 , HIGH);

    }else{
        digitalWrite(MOTOR3 , LOW);
        digitalWrite(MOTOR4 , LOW);
        digitalWrite(MOTOR3_4 , LOW);
    }

}
