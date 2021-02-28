#include<iostream>
using namespace std;
class Point
{
    public:
    int x,y;
    void set();             //member functions are pooled
    bool isOrigin();
    void display();
    Point diff(Point);
};
void Point::set()
{
    x=0;
    y=0;
}
bool Point::isOrigin()
{
    if(x==0 && y==0)
        return true;
    else
        return false;
}
void Point::display()
{
    cout<<x<<"\t"<<y;
}
Point Point::diff(Point p2)
{
    Point p3;
    p3.x=x+p2.x;
    p3.y=y+p2.y;
    return p3;
}
int main()
{
    Point p1,p2,p3;
    p1.x=5;
    p1.y=5;
    p2.x=6;
    p2.y=7;
    cout<<p1.isOrigin()<<endl;
    p3=p1.diff(p2);
    cout<<p3.x<<"\n"<<p3.y;
}
