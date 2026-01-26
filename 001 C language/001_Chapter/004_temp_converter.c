#include<stdio.h>
int main(){
    float celcius , Fahrenheit ;
    printf("celcius : ");
    scanf("%f", &celcius);
    Fahrenheit  = (celcius*(9.0/5))+32.0;
    printf("Fahrenheit  : %f", Fahrenheit );
    return 0;
}