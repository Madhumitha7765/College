#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
#include "item.h"
#include "sanitisers.h"
#include "shoppingcart.h"
#define A cout<<"\n*********************************************************************";

sanitisers::sanitisers()
{
    name="alcohol based sanitiser";
    seller="dettol";

}
sanitisers::~sanitisers()
{
        remove("sanitisers.dat");
}
void sanitisers::getSanitisers()
{
    A
    cin.ignore();
    cout<<"\n enter name:";
    getline(cin,name);
    cout<<"\n enter seller name:";
    getline(cin,seller);
    getItem();
}

void sanitisers::putSanitisers()
{
    A
     cout<<"\n Name:"<<name;
    cout<<"\n Seller:"<<seller;
    putItem();
}

void writeSanitisers(sanitisers &s)
{
     ofstream ofile("sanitisers.dat",ios::binary|ios::app);
    s.getSanitisers();
    ofile.write((char*)&s,sizeof(s));
    ofile.close();
}

void readSanitisers(sanitisers &s)
{
     ifstream ifile("sanitisers.dat",ios::binary);
    while(ifile.read((char*)&s,sizeof(s)))
      s.putSanitisers();
    ifile.close();
}

void purchaseSanitisers(sanitisers &m)
{
    A
    int idno,buyqty;
    cout<<"\n enter id no:";
    cin>>idno;
    cout<<"\n enter qty to buy:";
    cin>>buyqty;
    ifstream ifile("sanitisers.dat",ios::binary);
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
            modifySanitisers(m,buyqty);
            shoppingCart s;
            s.getShopcart(m.id,'s',m.price,buyqty);
            writeShopcart(s);
            cout<<"\n Item added successfully to cart\n";
        }
    }
    else
        cout<<"\n entered id is invalid\n";

}

void modifySanitisers(sanitisers &m,int bqty)
{
    m.stock-=bqty;
    fstream iofile("sanitisers.dat",ios::in|ios::out|ios::binary);
    sanitisers l;
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




