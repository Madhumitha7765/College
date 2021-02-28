#include<iostream>
using namespace std;
class Point
{
    int x;
    int y;
    public:
    Point();
    friend void operator -(Point&);
    void display();
};
Point::Point()
{
    x=y=50;
}
void operator -(Point &q)
{
    q.x=-q.x;
    q.y=-q.y;
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
