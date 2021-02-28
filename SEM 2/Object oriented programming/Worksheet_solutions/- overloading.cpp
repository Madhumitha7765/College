#include<iostream>
using namespace std;
class Point
{
    int x;
    int y;
    public:
    Point();
    void operator -();
    void display();
};
Point::Point()
{
    x=y=50;
}
void Point::operator -()
{
    x=-x;
    y=-y;
}
void Point::display()
{
    cout<<"x="<<x<<endl<<"y="<<y<<endl;
}
int main()
{
    Point p1;
    -p1;
    p1.display();
}
