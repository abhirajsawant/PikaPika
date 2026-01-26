#include<stdio.h>
int main (){
    printf("hi I'm Jerry\n"); //to show output
    int a =33; //data type : integer
    float j = 6.77; //data type : float
    char b= 'h'; // data type : character
    printf("\n%d \n%f \n%c",a,j,b);  
    // %d , %f , %c are format speccifir & \n is an escape sequence
    int k ;
    scanf("\n%d", &k); // to get input from user
    // & is "address of"
    printf("%d",k);
    return 0;
}