#include<iostream>
using namespace std;
class Number
{
    int x;
    public:
    Number()
    {
        x=5;
    }
    void display()const
    {
        cout<<increment()<<endl;            //we cant call a non-constant function inside a constant function
        cout<<x;
    }
    int increment()
    {
        x++;
        return x;
    }
};
int main()
{
    Number x;
    x.display();
}
