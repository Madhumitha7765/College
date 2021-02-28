#ifndef ITEM_H_INCLUDED
#define ITEM_H_INCLUDED

class item
{
public:
    int id;
    int stock;
    float price;
    void getItem();
    void putItem();
    item();
};

#endif // ITEM_H_INCLUDED
