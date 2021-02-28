#include<iostream>
using namespace std;

class Country
{
    char * country;
    int pop;
    float area;
    public :
    Country();
    void getdata();
    void print();
    int ret_pop();
    float ret_area();
    float ret_popden();
    void put_name();
    void put_pop();
    void put_area();
};

Country::Country()
{
    country = new char[30];
}

void Country::getdata()
{
    cout<<"\nEnter area : ";
    cin>>area;
    cout<<"\nEnter population : ";
    cin>>pop;
    cout<<"\nPopulation density is : "<<ret_popden();
}

void Country::print()
{
    cout<<"\narea : "<<area;
    cout<<"\npopulation : "<<pop;
    cout<<"\npopulation density : "<<ret_popden();
}

int Country::ret_pop()
{
    return pop;
}

float Country::ret_area()
{
    return area;
}

float Country::ret_popden()
{
    return (float)pop/area;
}

int main()
{
    Country c[10];
    int n,i;
    cout<<"\nEnter the number of countries u want to input : ";
    cin>>n;
    for(i=0;i<n;i++)
    {
        cout<<"Country : "<<i+1;
        cout<<"\nEnter country name : ";
        cin>>c[i].put_name();
        cout<<"\nEnter area : ";
        cin>>c[i].put_area();
        cout<<"\nEnter population : ";
        cin>>c[i].put_pop();
    }
}
