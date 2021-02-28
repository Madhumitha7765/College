 #include<iostream>
using namespace std;
class Point
{
    int x;
    int y;
    public:
    friend istream& operator >>(istream&,Point&);
    friend ostream& operator <<(ostream&,Point&);
};
istream& operator >>(istream& cin,Point &p)
{
    cin.sync();
    cin>>p.x;
    cin>>p.y;
    return cin;
}
ostream& operator <<(ostream& cout,Point &p)
{
    cout<<"("<<p.x<<","<<p.y<<")";
    return cout;
}
int main()
{
    Point a;
    cin>>a;
    cout<<a;
}
