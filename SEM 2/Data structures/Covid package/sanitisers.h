#ifndef SANITISERS_H_INCLUDED
#define SANITISERS_H_INCLUDED

class sanitisers:public item
{
    private:
    string name;
    string seller;
    public:
        sanitisers();
        void getSanitisers();
        void putSanitisers();
        friend void writeSanitisers(sanitisers&);
        friend void readSanitisers(sanitisers&);
        friend void purchaseSanitisers(sanitisers &);
    friend void modifySanitisers(sanitisers &,int=0);
    ~sanitisers();

};


#endif // SANITISERS_H_INCLUDED
