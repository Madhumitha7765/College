#include<iostream>
using namespace std;
class Point
{
    public:
    int x;
    int y;
    Point()
    {
        x=0;
        y=0;
    }
    void display()
    {
        cout<<x<<"\t"<<y<<endl;
    }
};
class Rational
{
    public:
    int m;
    int n;
    Rational()
    {
        m=5;
        n=5;
    }
    void display()
    {
        cout<<m<<"\t"<<n<<endl;
    }
};
int main()
{
    Point p;
    Rational *r;
    r=(Rational *)&p;
    p.display();
    r->display();
}
