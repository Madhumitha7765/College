#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
#include "item.h"
#include "masks.h"
#include "shoppingcart.h"
#define A cout<<"\n*********************************************************************";
masks::masks()
{
    name="n95";
    seller="wildcraft";


}
masks::~masks()
{

    remove("masks.dat");
}

void masks::getMasks()
{
    cin.ignore();
    A
    cout<<"\n enter name:";
    getline(cin,name);
    cout<<"\n enter seller name:";
    getline(cin,seller);
    getItem();
}

void masks::putMasks()
{
    A
    cout<<"\n Name:"<<name;
    cout<<"\n Seller:"<<seller;
    putItem();
}

void writeMasks(masks &m)
{
    ofstream ofile("masks.dat",ios::binary|ios::app);
    m.getMasks();
    ofile.write((char*)&m,sizeof(m));
    ofile.close();
}

void readMasks(masks &m)
{
    ifstream ifile("masks.dat",ios::binary);
    while(ifile.read((char*)&m,sizeof(m)))
      m.putMasks();
    ifile.close();
}
void purchaseMasks(masks &m)
{
    A
    int idno,buyqty;
    cout<<"\n enter id no:";
    cin>>idno;
    cout<<"\n enter qty to buy:";
    cin>>buyqty;
    ifstream ifile("masks.dat",ios::binary);
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
            modifyMasks(m,buyqty);
            shoppingCart s;
            s.getShopcart(m.id,'m',m.price,buyqty);
            writeShopcart(s);
            cout<<"\n Item added successfully to cart\n";
        }
    }
    else
        cout<<"\n entered id is invalid\n";

}

void modifyMasks(masks &m,int bqty)
{
    m.stock-=bqty;
    fstream iofile("masks.dat",ios::in|ios::out|ios::binary);
    masks l;
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



