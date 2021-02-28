#include<iostream>
#include<string.h>
using namespace std;
class Phone
{
    char *country;
    char *landline;
    char *main;
    public:
    Phone();
    void get(char*);
    void print();
};
Phone::Phone()
{
    country=new char[3];
    landline=new char[5];
    main=new char[6];
}
void Phone::get(char *phone)
{
    int i;
    for(i=0;i<2;i++)
    {
        country[i]=phone[i];
    }
    country[i]='\0';
    for(i=3;i<7;i++)
    {
        landline[i-3]=phone[i];
    }
    landline[i]='\0';
    for(i=8;i<13;i++)
    {
        main[i-8]=phone[i];
    }
}
void Phone::print()
{
    cout<<"country-code:"<<country<<endl;
    cout<<"landline-code:"<<landline<<endl;
    cout<<"main:"<<main<<endl;
}
int main()
{
    char phone[20];
    Phone p;
    cout<<"Enter the phone number....";
    cin>>phone;
    p.get(phone);
    p.print();
}
