#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
#include<cstring>
#include "shoppingmall.h"
#define A cout<<"\n*********************************************************************";

ShopMall::ShopMall(string name1)
{
    nameMall=name1;

}
void ShopMall::getName()
{
    cout<<"\n"<<nameMall<<endl;
}
void ShopMall::setName()
{
    A
    string giveName;
    cout<<"\n enter your preferred name for the shopping cart:\n";
    getline(cin,giveName);
    nameMall=giveName;
    cout<<"\n Name:"<<nameMall<<endl;
    cout<<"\n Name of the mall is successfully set\n";
}
int ShopMall::chooseUser()
{
    int n;
    A
    cout<<"\nEnter 1 for ADMIN 2 for CUSTOMER 3 TO EXIT\n";
    cin>>n;
    return n;
    system("cls");

}
