#ifndef SHOPPINGMALL_H_INCLUDED
#define SHOPPINGMALL_H_INCLUDED

class ShopMall
{
    public:
        ShopMall(string="ABC shopping cart");
        void setName();
        void getName();
        int chooseUser();


    private:
       string nameMall;
};

#endif // SHOPPINGMALL_H_INCLUDED
