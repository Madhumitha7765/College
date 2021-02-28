#ifndef HANDWASH_H_INCLUDED
#define HANDWASH_H_INCLUDED

class handwash:public item
{
    private:
    string name;
    string seller;
    public:
        handwash();
        void getHandwash();
        void putHandwash();
        friend void writeHandwash(handwash&);
        friend void readHandwash(handwash&);
        friend void purchaseHandwash(handwash &);
    friend void modifyHandwash(handwash&,int=0);
    ~handwash();
};

#endif // HANDWASH_H_INCLUDED
