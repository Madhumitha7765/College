#include<iostream>
#include<string.h>
using namespace std;
class Point
{
    int x;
    int y;
    char *desc;
    public:
    Point(char *c,int a,int b):x(a),y(b)
    {
        desc=new char[10];
        strcpy(desc,c);
    }
    void display();
    Point& operator =(const Point&);
};
void Point::display()
{
    cout<<desc<<endl<<x<<endl<<y<<endl;
}
Point& Point::operator =(const Point &p)
{
    if(this!=&p)
    {
        delete []desc;
        desc=new char[strlen(p.desc)+1];
        strcpy(desc,p.desc);
        x=p.x;
        y=p.y;
    }
    return *this;
}
int main()
{
    Point p1("hi",0,0);
    Point p2("bye",10,20);
    p1.display();
    p2.display();
    p1=p2;
    cout<<"\n\nAfter Copying:-\n";
    p1.display();
    p2.display();
}
