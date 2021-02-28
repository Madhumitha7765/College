#include<iostream>
using namespace std;
class Point
{
    int x;
    int y;
    public:
    Point();
    Point(int a,int b):x(a),y(b)
    {}
    void display();
    void operator ++()
    {
        x++;
        y++;
    }
    void operator ++(int)
    {
        ++x;
        ++y;
    }
};
void Point::display()
{
    cout<<x<<endl<<y<<endl;
}
int main()
{
    Point p(10,20);
    p.display();
    p++;
    p.display();
    ++p;
    p.display();
}
