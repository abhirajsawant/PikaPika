#include<iostream>
using namespace std;
int main(){
    int x = 5;
    cout<<x<<endl;
    x = 6; //updating or overwriting
    cout<<x<<endl;
    x = x + 8;
    // x += 8;
    cout<<x<<endl;
    x = x - 5;
    // x -= 5:
    cout<<x<<endl;
    x++;    //Post-increment : first use then update 
    cout<<x<<endl;
    ++x;    //Pre-increment : first update then use
    cout<<x<<endl;
    x--;    //Post-decrement : first use then update
    cout<<x<<endl;
    --x;    //Pre-decrement : first update then use
    cout<<x<<endl;
    
}
