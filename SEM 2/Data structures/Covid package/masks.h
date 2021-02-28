#ifndef MASKS_H_INCLUDED
#define MASKS_H_INCLUDED
#include "item.h"

class masks:public item
{
private:
    string name;
    string seller;

public:
    void getMasks();
    void putMasks();
    friend void writeMasks(masks &);
    friend void readMasks(masks &);
    friend void purchaseMasks(masks &);
    friend void modifyMasks(masks &,int=0);
    masks();
    ~masks();
};

#endif // MASKS_H_INCLUDED
