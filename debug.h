#include "main.h"

//////////////////////////////////////////////////////////////////
//  疑似音声入力モード                                          //
//  DEBUG_VOICE_MODE                                            //
//--------------------------------------------------------------//
    #define DEBUG_VOICE_MODE        OFF
//--------------------------------------------------------------//
//  <説明>                                                      //
//  raspi3に接続することなく音声入力モードのデバッグが取れる。  //
//--------------------------------------------------------------//
//  <指定値>                                                    //
//  ON          :疑似音声入力モードON                           //
//  OFF         :疑似音声入力モードOFF(デフォルト)              //
//--------------------------------------------------------------//
//  <使用ファイル>                                              //
//  main.c, voiceMode.c, debug.c                                //
//--------------------------------------------------------------//
    #define INPUT_VOICE             OFF
//--------------------------------------------------------------//
//  <説明>                                                      //
//  疑似音声入力モードでの制御命令を指定する。                  //
//--------------------------------------------------------------//
//  <指定値>                                                    //
//  FORWARD :前進                                               //
//  LEFT    :左旋回                                             //
//  RIGHT   :右旋回                                             //
//  STOP    :停止                                               //
//  RAND    :ランダム                                           //
//  MANUAL  :動作命令手入力                                     //
//  OFF     :疑似音声入力モードでの制御命令なし                 //
//--------------------------------------------------------------//
//  <使用ファイル>                                              //
//  debug.c                                                     //
//////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////
    #define GPIO_READ               ON
//--------------------------------------------------------------//
//  <説明>                                                      //
//  疑似音声入力モード時のGPIO値を出力する。                    //
//--------------------------------------------------------------//
//  <指定値>                                                    //
//  ON          :GPIO値出力                                     //
//  OFF         :GPIO値出力なし(デフォルト)                     //
//--------------------------------------------------------------//
//  <使用ファイル>                                              //
//  debug.c                                                     //
//////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////
//  音声入力モードのみ                                          //
//  ONLY_VOICE_MODE                                             //
//--------------------------------------------------------------//
    #define ONLY_VOICE_MODE         ON
//--------------------------------------------------------------//
//  <説明>                                                      //
//  音声入力モードのみを実行する。(擬似音声入力と併用可能)      //
//--------------------------------------------------------------//
//  <指定値>                                                    //
//  ON  :音声入力モードのみを実行                               //
//  OFF :通常モード(デフォルト)                                 //
//--------------------------------------------------------------//
//  <使用ファイル>                                              //
//  main.c                                                      //
//////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////
//  前面距離測定デバッグ(超音波センサ)                          //
//  DEBUG_FRONT_DISTANCE                                        //
//--------------------------------------------------------------//
    #define DEBUG_FRONT_DISTANCE    ON
//--------------------------------------------------------------//
//  <説明>                                                      //
//  frontDistance()内で取得される各種変数の値を表示する。       //
//--------------------------------------------------------------//
//  <指定値>                                                    //
//  ON      :前面距離の値を出力(デフォルト)                     //
//  OFF     :デバッグなし                                       //
//  DETAIL  :各種変数値を出力                                   //
//--------------------------------------------------------------//
//  <使用ファイル>                                              //
//  distance.c                                                  //
//////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////
//  側面距離測定デバッグ(赤外線センサ)                          //
//  DEBUG_SIDE_DISTANCE                                         //
//--------------------------------------------------------------//
    #define DEBUG_SIDE_DISTANCE     OFF
//--------------------------------------------------------------//
//  <説明>                                                      //
//  sideDistance()内で取得されるアナログ値を表示する。          //
//  MANUAL_V を指定した場合、手動で入力電圧(V)を指定する。      //
//  MANUAL_D を指定した場合、手動で側面距離(cm)を指定する。     //
//--------------------------------------------------------------//
//  <指定値>                                                    //
//  ON          :アナログ値を出力                               //
//  OFF         :デバッグなし(デフォルト)                       //
//  MANUAL_V    :入力電圧を指定                                 //
//  MANUAL_D    :側面距離を指定                                 //
//--------------------------------------------------------------//
//  <使用ファイル>                                              //
//  sideDistance.c                                              //
//////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////
//  動作制御命令デバッグ(モーター)                              //
//  DEBUG_MOTOR                                                 //
//--------------------------------------------------------------//
    #define DEBUG_MOTOR             ON
//--------------------------------------------------------------//
//  <説明>                                                      //
//  実行中の動作制御命令の名称を出力する。                      //
//--------------------------------------------------------------//
//  <指定値>                                                    //
//  ON  :名称出力(デフォルト)                                   //
//  OFF :名称出力なし                                           //
//--------------------------------------------------------------//
//  <使用ファイル>                                              //
//  motor.c                                                     //
//////////////////////////////////////////////////////////////////

