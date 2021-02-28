#include<stdio.h>
void main()
{
    int i=10;

    int *p=&i;
    printf("%x\n",p);
    p=p+4;
    printf("%d\n",i);
    printf("%x\n",p);
}
