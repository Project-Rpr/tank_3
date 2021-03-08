#include "main.h"
#include "debug.h"

int debug_init(void);
void gpio_off(void);
void gpio_read(void);

void debug_forward(void);
void debug_right(void);
void debug_left(void);
void debug_stop(void);


void debug_voiceMode(void){
    static int debug = OFF;
    unsigned int num = 10;
    
    if(debug == OFF){
        debug_init();
        debug = ON;
    }

#if INPUT_VOICE == RAND
    srand((unsigned int)time(NULL));
    num = rand() % 5;
    printf("rand() = %d\n", num);
#elif INPUT_VOICE == FORWARD
    num = 0;
#elif INPUT_VOICE == RIGHT
    num = 1;
#elif INPUT_VOICE == LEFT
    num = 2;
#elif INPUT_VOICE == STOP
    num = 3;
#elif INPUT_VOICE == MANUAL
    printf("【擬似音声入力モード】\n");
    printf("0:前進\n");
    printf("1:右旋回\n");
    printf("2:左旋回\n");
    printf("3:停止\n");
    printf("動作命令を手入力:\n");
    scanf("%d", &num);
#endif

    switch(num){
        case 0:
            debug_forward();
            break;
        case 1:
            debug_right();
            break;
        case 2:
            debug_left();
            break;
        case 3:
            debug_stop();
            break;
        default:
            /*DO NOTHING*/
            printf("pass\n");
            break;
    }
    voiceMode();

#if (INPUT_VOICE == MANUAL) && (GPIO_READ == ON)
    delay(VOICE_MODE_TIME);
    debug_stop();
#endif

}


int debug_init(void){
    pinMode(DEBUG_MODE_PIN, OUTPUT);
    pinMode(DEBUG_FORWARD_PIN, OUTPUT);
    pinMode(DEBUG_RIGHT_PIN, OUTPUT);
    pinMode(DEBUG_LEFT_PIN, OUTPUT);

    printf("debug init\n");

    return 0;
}

void gpio_off(void){
    digitalWrite(DEBUG_MODE_PIN, LOW);
    digitalWrite(DEBUG_FORWARD_PIN, LOW);
    digitalWrite(DEBUG_RIGHT_PIN, LOW);
    digitalWrite(DEBUG_LEFT_PIN, LOW);
    digitalWrite(MODE_PIN, LOW);
    digitalWrite(FORWARD_PIN, LOW);
    digitalWrite(RIGHT_PIN, LOW);
    digitalWrite(LEFT_PIN, LOW);
}

void gpio_read(void){
    printf("\n");
    printf("MODE_PIN\tGPIO%d : %d\n", MODE_PIN, digitalRead(MODE_PIN));
    printf("FORWARD_PIN\tGPIO%d : %d\n", FORWARD_PIN, digitalRead(FORWARD_PIN));
    printf("RIGHT_PIN\tGPIO%d : %d\n", RIGHT_PIN, digitalRead(RIGHT_PIN));
    printf("LEFT_PIN\tGPIO%d : %d\n", LEFT_PIN, digitalRead(LEFT_PIN));
    printf("\n");
}

void debug_forward(void){
    digitalWrite(DEBUG_FORWARD_PIN, HIGH);
    digitalWrite(DEBUG_RIGHT_PIN, LOW);
    digitalWrite(DEBUG_LEFT_PIN, LOW);
    printf("debug_forward\n");
}

void debug_right(void){
    digitalWrite(DEBUG_FORWARD_PIN, LOW);
    digitalWrite(DEBUG_RIGHT_PIN, HIGH);
    digitalWrite(DEBUG_LEFT_PIN, LOW);
    printf("debug_right\n");
}

void debug_left(void){
    digitalWrite(DEBUG_FORWARD_PIN, LOW);
    digitalWrite(DEBUG_RIGHT_PIN, LOW);
    digitalWrite(DEBUG_LEFT_PIN, HIGH);
    printf("debug_left\n");
}

void debug_stop(void){
    digitalWrite(DEBUG_FORWARD_PIN, LOW);
    digitalWrite(DEBUG_RIGHT_PIN, LOW);
    digitalWrite(DEBUG_LEFT_PIN, LOW);
    printf("debug_stop\n");
}
