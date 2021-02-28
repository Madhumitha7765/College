#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
#include "shoppingcart.h"
#define A cout<<"\n*********************************************************************";
void shoppingCart::getShopcart(int id1,char s,float price1,int qty1)
{
    id=id1;
    price=price1;
    qty=qty1;
    subtotal=price1*qty1;
    t=s;

}
int shoppingCart::count=0;

/*void shoppingCart::putShopcart()
{
    A
    cout<<"\nId:"<<id;
    if(t=='m')
    cout<<"\n Name:mask";
    if(t=='s')
    cout<<"\n Name:sanitiser";
    if(t=='h')
    cout<<"\n Name:Handwash";
    cout<<"\n Price:"<<price;
    cout<<"\n Qty:"<<qty;
    cout<<"\n Sub total:"<<subtotal;
}*/
ostream& operator<<(ostream &out,const shoppingCart &s)
{
    A
    out<<"\nId:"<<s.id;
    if(s.t=='m')
    out<<"\n Name:mask";
    if(s.t=='s')
    out<<"\n Name:sanitiser";
    if(s.t=='h')
    out<<"\n Name:Handwash";
    out<<"\n Price:"<<s.price;
    out<<"\n Qty:"<<s.qty;
    out<<"\n Sub total:"<<s.subtotal;
}


void writeShopcart(shoppingCart &s)
{
    ofstream ofile("carts.dat",ios::binary|ios::app);
    ofile.write((char*)&s,sizeof(s));
    //s.putShopcart();
    cout<<s;
    ofile.close();

}

void readShopcart(shoppingCart &s)
{
    float total=0;
     ifstream ifile("carts.dat",ios::binary);
    while(true)
    {
        if(!ifile.read((char*)&s,sizeof(s))) break;
            cout<<s;
            total+=s.subtotal;
    }
    A
    cout<<"\n Grand total:"<<total<<endl;
    A
    ifile.close();
}



void deleteShopcart(shoppingCart &s)
{
    int pos, flag = 0,idno;
    cout<<"\n enter id. no to delete:";
    cin>>idno;

    ifstream ifs;
    ifs.open("carts.dat", ios::in | ios::binary);

    ofstream ofs;
    ofs.open("temp.dat", ios::out | ios::binary);

    while (!ifs.eof()) {

        ifs.read((char*)&s, sizeof(s));

        // if(ifs)checks the buffer record in the file
        if (ifs) {

            // comparing the roll no with
            // roll no of record to be deleted
            if (idno == s.id) {
                flag = 1;
                cout << "The deleted record is \n";

                // display the record
                cout<<s;
            }
            else {
                // copy the record of "he" file to "temp" file
                ofs.write((char*)&s, sizeof(s));
            }
        }
    }

    ofs.close();
    ifs.close();

    // delete the old file
    remove("carts.dat");

    // rename new file to the older file
    rename("temp.dat", "carts.dat");

    if (flag == 1)
        cout << "\nrecord successfully deleted \n";
    else
        cout << "\nrecord not found \n";
        return;
}

