#include<iostream>
#include<string.h>
using namespace std;
class Mystring
{
    char *x;
    public:
    Mystring();
    void get();
    void display();
    void operator ++(int);
    bool operator ==(Mystring&);
    Mystring& operator +(Mystring&);
    Mystring& operator =(Mystring&);
};
Mystring::Mystring()
{
    x=new char[10];
}
void Mystring::get()
{
    char *c;
    cout<<"Enter the string...";
    cin>>c;
    strcpy(x,c);
}
void Mystring::display()
{
    cout<<x<<endl;
}
void Mystring::operator ++(int)
{
    for(int i=0;x[i]!='\0';i++)
    {
        x[i]=x[i]+1;
    }
}
bool Mystring::operator ==(Mystring &y)
{
    return strcmp(x,y.x);
}
Mystring& Mystring::operator +(Mystring &y)
{
    strcat(x,y.x);
    return *this;
}
Mystring& Mystring::operator =(Mystring &y)
{
    strcpy(x,y.x);
    return *this;
}
int main()
{
    int n;
    Mystring x,y;
    x.get();
    cout<<"x=";x.display();
    y.get();
    cout<<"y=";y.display();
    l1:cout<<"1)Postfix\n2)Compare\n3)Equal\n4)Concate\n";
    cin>>n;
    if(n==1)
    {
        cout<<"x=";x.display();
        x++;
        cout<<"Postfix of X:";x.display();
        goto l1;
    }
    else if(n==2)
    {
        cout<<"x=";x.display();
        cout<<"y=";y.display();
        cout<<"Compare:";
        n=(x==y);
        cout<<n<<endl;
        goto l1;
    }
    else if(n==3)
    {
        cout<<"x=";x.display();
        cout<<"y=";y.display();
        x=y;
        cout<<"After operation\n";
        cout<<"x=";x.display();
        cout<<"y=";y.display();
        goto l1;
    }
    else if(n==4)
    {
        cout<<"x=";x.display();
        cout<<"y=";y.display();
        cout<<"After operation:-"<<endl;
        x+y;
        cout<<"x=";x.display();
        goto l1;
    }
}
