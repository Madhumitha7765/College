#include<iostream>
using namespace std;
class Base
{
    protected:
    int i;
    Base()
    {
        i=5;
    }
    void display()
    {
        cout<<i;
    }
};
class Derived:protected Base
{
    public:
    int j;
    Base::i;            //Derived class can grant access to Base
    Derived()
    {
        j=1;
    }
    void display()
    {
        Base::display();        //we cant call Base::display in main since its protected
        cout<<endl<<j;
    }
};
int main()
{
    Derived d;
    cout<<d.i<<endl<<d.j<<endl;
    d.display();
}
