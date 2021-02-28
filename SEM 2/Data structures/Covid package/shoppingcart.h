#ifndef SHOPPINGCART_H_INCLUDED
#define SHOPPINGCART_H_INCLUDED

class shoppingCart
{
private:
     int id;
    float price;
    int qty;
    float subtotal;
    char t;


public:
    static int count;
    void getShopcart(int,char,float,int);
    friend ostream& operator<<(ostream &out,const shoppingCart&s);
    friend void writeShopcart(shoppingCart&);
    friend void readShopcart(shoppingCart&);
    friend void deleteShopcart(shoppingCart&);




};
#endif // SHOPPINGCART_H_INCLUDED

