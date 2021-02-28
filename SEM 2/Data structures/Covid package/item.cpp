#include "item.h"
#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
#include "item.h"
#define A cout<<"*********************************************************************";

void item::getItem()
{
    cout<<"\n enter id:";
    cin>>id;
    cout<<"\n enter stock:";
    cin>>stock;
    cout<<"\n enter price:";
    cin>>price;
}
void item::putItem()
{
    cout<<"\n Id:"<<id;
    cout<<"\n Stock:"<<stock;
    cout<<"\n Price:"<<price;
}
item::item()
{
    id=10;
    stock=20;
    price=100;
}
