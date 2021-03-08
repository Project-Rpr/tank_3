#include "main.h"
#include "debug.h"

double  frontDistance (void){
        double duration, distance = 0;
        clock_t s_time,e_time;

        digitalWrite(TRIG, ON);
        delay(1);
        digitalWrite(TRIG, OFF);
        while(digitalRead(ECHO) == 0){
        #if DEBUG_FRONT_DISTANCE == DETAIL
            printf("digitalRead(ECHO) == 0\n");
        #endif
        }

        s_time = clock();

        while(digitalRead(ECHO) == 1){
        #if DEBUG_FRONT_DISTANCE == DETAIL
            printf("digitalRead(ECHO) == 1\n");
        #endif
        }

        e_time = clock();
    #if DEBUG_FRONT_DISTANCE == DETAIL
        printf("s_time: %lf \ne_time: %lf \n",(double)s_time,(double)clock());
    #endif

        duration =(double)(e_time - s_time)/CLOCKS_PER_SEC;
    #if DEBUG_FRONT_DISTANCE == DETAIL
        printf("duration: %lf\n",duration);
    #endif

        distance = (duration / 2) * 34350;

    #if DEBUG_FRONT_DISTANCE != OFF
        printf("front distance = %lf cm\n", distance);
    #endif

        return distance; 

}
