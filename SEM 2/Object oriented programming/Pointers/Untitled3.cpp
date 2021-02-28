#include<iostream>
using namespace std;
main()
{
    int *i,a[]={0,1,2,3,4,5,6};
    i=a;
    int *p=i+3;
    int n=*p-(*i+2);
    cout<<*p<<"\n"<<*i<<"\n"<<n;
}
