#include "main.h"
#include "debug.h"

int initial(void);


int main (void){
    double f_distance = 0;                      //前面距離
    int turn_flag = 0;                          //左右判定フラグ
    static int voice_mode = OFF;                //音声入力モード確認

    initial();                                  //GPIO入出力設定
    
#if ONLY_VOICE_MODE == ON
    printf("音声入力モードのみ\n");
#endif
   
    /*メイン処理*/
    while(TRUE){

    #if DEBUG_VOICE_MODE == ON
        voice_mode = ON;
    #endif

        /*自動運転モードのみの場合*/
        if(voice_mode == OFF){
            if(digitalRead(MODE_PIN) == HIGH){
                voice_mode = ON;
                voiceMode_ON();                 //音声入力モード開始
            }

        /*音声入力受付状態の場合*/
        }else if(voice_mode == ON){

        #if DEBUG_VOICE_MODE == ON
            debug_voiceMode();                  //疑似音声入力受け付け(デバッグ)
        #endif

            if(digitalRead(MODE_PIN) == HIGH){
                voiceMode();                    //音声入力受け付け
            }
        }

    #if ONLY_VOICE_MODE != ON
        f_distance = frontDistance();           //前面距離を取得

        /*前面距離が「緊急停止距離」内の場合*/
        if(f_distance < EMERGENCY_STOP_D){
            stop();delay(STOP);delay(STOP);     //緊急停止
            back();delay(BACK);                 //後退
            stop();delay(STOP);                 //停止

        }
        
        /*前面距離が「緊急停止距離」以上「旋回距離」未満の場合*/
        else if((f_distance >= EMERGENCY_STOP_D) && (f_distance < STOP_D)){
            stop();delay(STOP);                 //停止

            turn_flag = sideDistance();         //左右の旋回方向を取得

            /*turn_flagが右の場合*/
            if(turn_flag == RIGHT){
                t_Right();                      //右旋回
        
            /*turn_flagが左の場合*/
            }else{
                t_Left();                       //左旋回
            }
        
            /*前面距離が「旋回距離」未満の場合*/
            while(f_distance < STOP_D){
                f_distance = frontDistance();   //前面の距離を取得
                delay(TURN);                    //旋回時間の調整

                /*ループ中に音声入力があった場合*/
                if((voice_mode == OFF) && (digitalRead(MODE_PIN) == HIGH)){
                    voice_mode = ON;
                    voiceMode_ON();             //音声入力モード開始
                    break;
                }else if((voice_mode == ON) && (digitalRead(MODE_PIN) == HIGH)){
                    voiceMode();                //音声入力受け付け
                    break;
                }
            }
        
            stop();delay(STOP);                 //停止
        }
        
        /*前面距離が「旋回距離」より大きい場合*/
        else if(f_distance > STOP_D){
            forward();                          //直進
        }
    #endif

    }

    return 0;
}


int initial(void){
    if(wiringPiSetupGpio() == -1){
        return -1;
    }

    /*GPIO設定*/   
    pinMode(MODE_PIN, INPUT);                   //音声入力モード設定受信ピン
    pinMode(FORWARD_PIN, INPUT);                //前進命令受信ピン
    pinMode(RIGHT_PIN, INPUT);                  //右旋回命令受信ピン
    pinMode(LEFT_PIN, INPUT);                   //左旋回命令受信ピン

    pinMode(TRIG, OUTPUT);                      //超音波センサ 出力設定
    pinMode(ECHO, INPUT);                       //超音波センサ 入力設定

    pinMode(MOTOR1, OUTPUT);                    //モータードライバ1 出力設定
    pinMode(MOTOR2, OUTPUT);                    //モータードライバ2 出力設定
    pinMode(MOTOR3, OUTPUT);                    //モータードライバ3 出力設定
    pinMode(MOTOR4, OUTPUT);                    //モータードライバ4 出力設定
    pinMode(MOTOR1_2, OUTPUT);                  //モーター1，2用 出力設定
    pinMode(MOTOR3_4, OUTPUT);                  //モーター3，4用 出力設定
    
    /*GPIO初期化*/
    digitalWrite(MODE_PIN, LOW);
    digitalWrite(FORWARD_PIN, LOW);
    digitalWrite(RIGHT_PIN, LOW);
    digitalWrite(LEFT_PIN, LOW);

    digitalWrite(TRIG, LOW);
    digitalWrite(ECHO, LOW);

    digitalWrite(MOTOR1, LOW);
    digitalWrite(MOTOR2, LOW);
    digitalWrite(MOTOR3, LOW);
    digitalWrite(MOTOR4, LOW);
    digitalWrite(MOTOR1_2, LOW);
    digitalWrite(MOTOR3_4, LOW);

    return 0;
}
