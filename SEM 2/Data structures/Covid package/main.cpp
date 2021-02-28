#include <iostream>
#include<fstream>
using namespace std;
#include "masks.h"
#include "item.h"
#include "shoppingcart.h"
#include "sanitisers.h"
#include "handwash.h"
#include "shoppingmall.h"
#include <stdlib.h>
#define A cout<<"\n*********************************************************************\n";
int adminMenu()
{

    A
    int choice1;
    cout<<"\n1.Add stock\n2.View stock\n3.Modify stock\n4.Main menu\nEnter your choice:";
    cin>>choice1;
    return choice1;
}

int main()
{
  masks m;
  sanitisers s;
  handwash h;
  shoppingCart sc;
  int choice,choice1,n,i;
  ShopMall sm;
  A
  sm.getName();
  A
  a:
    int user=sm.chooseUser();
    try{
    if(user==1)
    {
        b:
        A
        cout<<"\n Admin \n";
        cout<<"\n1.Masks\n2.Sanitisers\n3.Handwashes\n4.exit\n";
        cin>>choice;
        if(choice==1)
        {
            do
            {
            cout<<"\n MASKS\n";
            choice1=adminMenu();
            switch(choice1)
            {
            case 1:
                A
                cout<<"\n enter no. of masks to be added:";
                cin>>n;
                for(i=0;i<n;i++)
                    writeMasks(m);
                break;
            case 2:
                cout<<"\n Available Stock\n";
                readMasks(m);
                break;
            case 3:
                cout<<"\n Modify stock\n";
                cout<<"\n enter the new data for the same old id No:\n";
                m.getMasks();
                modifyMasks(m);
                break;
            case 4:
                goto b;
                break;
            default:
                cout<<"\n Invalid choice\n";

            }
            }while(choice1!=4);



        }
        if(choice==2)
        {
            do
            {
                cout<<"\n SANITISERS \n";
            choice1=adminMenu();
            switch(choice1)
            {
            case 1:
                cout<<"\n enter no. of sanitisers to be added:";
                cin>>n;
                for(i=0;i<n;i++)
                    writeSanitisers(s);
                break;
            case 2:
                cout<<"\n Available Stock\n";
                readSanitisers(s);
                break;
            case 3:
                cout<<"\n Modify stock\n";
                cout<<"\n enter the new data for the same old id No:\n";
                s.getSanitisers();
                modifySanitisers(s);
                break;
            case 4:
                goto b;
                break;
            default:
                cout<<"\n Invalid choice\n";

            }
            }while(choice1!=4);


        }
        if(choice==3)
        {
            do
            {
                cout<<"\n HANDWASHES \n";
            choice1=adminMenu();
            switch(choice1)
            {
            case 1:
                cout<<"\n enter no. of handwashes to be added:";
                cin>>n;
                for(i=0;i<n;i++)
                    writeHandwash(h);
                break;
            case 2:
                cout<<"\n Available Stock\n";
                readHandwash(h);
                break;
            case 3:
                cout<<"\n Modify stock\n";
                cout<<"\n enter the new data for the same old id No:\n";
                h.getHandwash();
                modifyHandwash(h);
                break;
            case 4:
                goto b;
                break;
            default:
                cout<<"\n Invalid choice\n";

            }
            }while(choice1!=4);


        }
        if(choice==4)
            goto a;
    }
    else if(user==2)
    {
        x:
        A
        cout<<"\n Welcome to Shopping cart\n";
        cout<<"\n 1.Buy\n2.View cart\n3.Delete cart\n4.Main menu\nEnter your choice:\n";
        cin>>choice;
        do
        {
            if(choice==1)
            {

                do{
                    A
                    cout<<"\n1.Masks\n2.Sanitisers\n3.Handwash\n4.Customer Menu\nEnter your choice:\n";
                        cin>>choice1;
                    switch(choice1)
                    {
                    case 1:
                        cout<<"\n Available stock\n";
                        readMasks(m);
                        purchaseMasks(m);
                        break;
                    case 2:
                        cout<<"\n Available stock\n";
                        readSanitisers(s);
                        purchaseSanitisers(s);
                        break;
                    case 3:
                        cout<<"\n Available stock\n";
                        readHandwash(h);
                        purchaseHandwash(h);
                        break;
                    case 4:
                        goto x;
                        break;
                    default:
                        cout<<"\n Invalid choice\n";

                    }
            }while(choice1!=4);
                break;
            }
            if(choice==2)
            {
                A
                cout<<"\n MY CART\n";
                A
                readShopcart(sc);

                goto x;
            }
            if(choice==3)
{
 A
                cout<<"\n MY CART\n";
                A

                deleteShopcart(sc);
                goto x;
}
            if(choice==4)
                goto a;



        }while(choice!=4);

    }
    else if(user==3)
        exit(0);
    else
    {
       throw(user);
    }
    }
    catch(int user)
    {
         cout<<"\n YOU HAVE ENTERED AN INVALID CHOICE........\n";
        cout<<"\n :D PLS TRY AGAIN :D\n";
        goto a;

    }


}
