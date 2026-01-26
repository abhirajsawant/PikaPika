#include<stdio.h>
int main (){
    float radius ,height;
    printf("raduis of circle : ");
    scanf("%f", &radius);
    printf("area of circle: %f",3.1415 *radius *radius );
    printf("\n height of Cylinder : ");
    scanf("%f", &height);
    printf("Volume of Cylinder: %f",3.1415 * radius * radius * height);
    printf("\nVolume of Sphere: %f",(4/3)*3.1415*radius*radius*radius);
    return 0;
}