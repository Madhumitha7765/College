#include<iostream>
using namespace std;
class Example
{
    int a;
    public:
    Example()
    {
        a=10;
    }
};
int main()
{
    int *x;
    Example e;
    x=(int*)&e;
    cout<<*x;                   //private access specifier violated
}
