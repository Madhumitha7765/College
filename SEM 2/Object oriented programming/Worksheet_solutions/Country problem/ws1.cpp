#include<iostream>
using namespace std;

class country
{
    char *name;
    int pop;
    float area;
    public :
    country(){
            name= new char[100];
             }
    float ret_area();
    int ret_pop();
    float ret_popden();
    void input();
    void display();
};

float country::ret_area()
{
    return area;
}

int country::ret_pop()
{
    return pop;
}

float country::ret_popden()
{
    return float(area/pop);
}

void input()
{
    cout<<"\nEnter details : ";
    cout<<"\n1.Area : ";
    cin>>area;
    cout<<"\n2.Population : ";
    cin>>pop;
    cout<<"\n3.Name of country : ";
    cin>>country;
}

void display()
{
    cout<<"\n1.Area : "<<area;
    cout<<"\n2.Population : "<<pop;
    cout<<"\n3.Name of country : "<<country;
}

int main()
{
    country c[10];
    int x;
    cout<<"\nEnter the number of countries to input : ";
    cin>>x;
    for(int i=0;i<x;i++)
    {
        c[i].input();
    }
    cout<<"\nThe enetered details are : ";
     for(int i=0;i<x;i++)
    {
        c[i].display();
    }

}
