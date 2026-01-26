#include<iostream>
using namespace std;
int main(){
    int x;
    cout<<"enter no.: ";
    cin>>x;
    cout<<"Square of the no.: "<<x*x;
    cout<<endl<<"Choose another no.: ";
    int y;
    cin>>y;
    // modulus is used to get Reamainder
    // a%(-b) = a%b
    // (-a)%b = -(a%b)
    cout<<"Remainder of the no.: "<<x%y;
}