#include<iostream>
using namespace std;
class Point
{
    int x;
    int y;
    public:
    Point(int a,int b):x(a),y(b){}
    void display();
    Point operator +(Point);
};
void Point::display()
{
    cout<<x<<endl<<y<<endl;
}
Point Point::operator +(Point p2)
{
    Point temp(0,0);
    temp.x=x+p2.x;
    temp.y=y+p2.y;
    return temp;
}
int main()
{
    Point p1(10,20);
    Point p2(20,10);
    p1.display();
    p2.display();
    p1=p1+p2;
    p1.display();
}
