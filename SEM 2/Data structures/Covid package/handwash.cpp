#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
#include "item.h"
#include "handwash.h"
#include "shoppingcart.h"
#define A cout<<"\n*********************************************************************";

handwash::handwash()
{
    name="clear handwash";
    seller="lifebuoy";

}
handwash::~handwash()
{

    remove("handwash.dat");
}
void handwash::getHandwash()
{
    A
    cin.ignore();
     cout<<"\n enter name:";
    getline(cin,name);
    cout<<"\n enter seller name:";
    getline(cin,seller);
    getItem();
}

void handwash::putHandwash()
{
    A
      cout<<"\n Name:"<<name;
    cout<<"\n Seller:"<<seller;
     putItem();
}

void writeHandwash(handwash &h)
{
     ofstream ofile("handwash.dat",ios::binary|ios::app);
    h.getHandwash();
    ofile.write((char*)&h,sizeof(h));
    ofile.close();
}

void readHandwash(handwash &h)
{
    ifstream ifile("handwash.dat",ios::binary);
    while(ifile.read((char*)&h,sizeof(h)))
      h.putHandwash();
    ifile.close();
}

void purchaseHandwash(handwash &m)
{
    A
    int idno,buyqty;
    cout<<"\n enter id no:";
    cin>>idno;
    cout<<"\n enter qty to buy:";
    cin>>buyqty;
    ifstream ifile("handwash.dat",ios::binary);
    int flag=0,count=0;
    while(ifile.read((char*)&m,sizeof(m)))
    {   count++;
        if(m.id==idno)
        {
            flag=count;
            break;
        }
    }
    if(flag!=0)
    {
        ifile.seekg((count-1)*sizeof(m));
        ifile.read((char*)&m,sizeof(m));
        if(m.stock<buyqty)
        {
            cout<<"\n the entered qty is unavailable\n";
        }
        else
        {
            modifyHandwash(m,buyqty);
            shoppingCart s;
            s.getShopcart(m.id,'h',m.price,buyqty);
            writeShopcart(s);
            cout<<"\n Item added successfully to cart\n";
        }
    }
    else
        cout<<"\n entered id is invalid\n";

}

void modifyHandwash(handwash &m,int bqty)
{
    m.stock-=bqty;
    fstream iofile("handwash.dat",ios::in|ios::out|ios::binary);
    handwash l;
    while(iofile.read((char*)&l,sizeof(l)))
    {
        if(l.id==m.id)
        {
            int p=iofile.tellg();
            iofile.seekp(p-sizeof(l));
            iofile.write((char*)&m,sizeof(m));
        }
    }

}

