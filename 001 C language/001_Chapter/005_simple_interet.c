#include<stdio.h>
int main(){
    float r , t,p ;
    scanf("%f %f %f", &p,&r,&t);
    printf("simple interest : %f",(r*p*t)/100.0);
    
    return 0;
}