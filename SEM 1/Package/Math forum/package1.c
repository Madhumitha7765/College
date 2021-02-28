



#include<stdio.h>
#include<math.h>
#include<stdlib.h>

/*#define KEY "Enter the calculator Operation you want to do:"*/


// Function prototype declaration
int cwin();
void input();
void addition();
void subtraction();
void multiplication();
void division();
void modulus();
void power();
int factorial();
void calculator_operations();
int age5();
void student();
int calcinput();
void operations1();
int binAddition();
int binSubtraction();
int binaryoperations();
int qeroots();
int matrixtranspose();
void main();
void  forexit();
int tictactoe();

char square[10]={'0','1','2','3','4','5','6','7','8','9'};


//function definitions

//addition function
void addition()
{
                int n, total=0, k=0, number,j1;
                printf("\nEnter the number of elements you want to add:");
                scanf("%d",&n);
                printf("Please enter %d numbers one by one: \n",n);
                while(k<n)
                        {
                            scanf("%d",&number);
                            total=total+number;
                            k=k+1;
                        }
                printf("Sum of %d numbers = %d \n",n,total);
                forexit();
}

//subtraction function
void subtraction()
{
    int a, b, c = 0,j1;
    printf("\nPlease enter first number  : ");
    scanf("%d", &a);
    printf("Please enter second number : ");
    scanf("%d", &b);
    c = a - b;
    printf("\n%d - %d = %d\n", a, b, c);
    forexit();
}

//multiplication function
void multiplication()
{
    int a, b, mul=0,j1;
    printf("\nPlease enter first number   : ");
    scanf("%d", &a);
    printf("Please enter second number: ");
    scanf("%d", &b);
    mul=a*b;
    printf("\nMultiplication of entered numbers = %d\n",mul);
    forexit();
}
//division function
void division()
{
    int a, b, d=0,j1;
    printf("\nPlease enter first number  : ");
    scanf("%d", &a);
    printf("Please enter second number : ");
    scanf("%d", &b);
    d=a/b;
    printf("\nDivision of entered numbers=%d\n",d);
    forexit();
}

//modulus function
void modulus()
{
    int a, b, d=0,j1;
    printf("\nPlease enter first number   : ");
    scanf("%d", &a);
    printf("Please enter second number  : ");
    scanf("%d", &b);
    d=a%b;
    printf("\nModulus of entered numbers = %d\n",d);
    forexit();
}

//power function
void power()
{

    double a,num, p;
    printf("\nEnter two numbers to find the power \n");
    printf("number: ");
    scanf("%lf",&a);

    printf("power : ");
    scanf("%lf",&num);

    p=pow(a,num);

    printf("\n%lf to the power %lf = %lf \n",a,num,p);
    forexit();

}

//factorial function
int factorial()
{
    int i,fact=1,num,j1;

    printf("\nEnter a number to find factorial : ");
    scanf("%d",&num);

    if (num<0)
    {
        printf("\nPlease enter a positive number to");
        printf(" find factorial and try again. \n");
        printf("\nFactorial can't be found for negative");
        printf(" values. It can be only positive or 0  \n");
        return 1;
    }

    for(i=1;i<=num;i++)
    fact=fact*i;
    printf("\n");
    printf("Factorial of entered number %d is:%d\n",num,fact);
    return 0;

}

//calc operations(age in range of 5--12)
void calculator_operations()
{

    printf("\n                   Welcome to world of math operations      \n\n");
    printf("     sharpen your skills by practising and enjoying the buliding basics of math\n");

    printf("******* Press 'Q' or 'q' to quit ");
    printf("the program ********\n");
    printf("***** Press 'H' or 'h' to display ");
    printf("below options *****\n\n");
    printf("Enter + symbol for Addition \n");
    printf("Enter - symbol for Subtraction \n");
    printf("Enter * symbol for Multiplication \n");
    printf("Enter / symbol for Division \n");
    printf("Enter ? symbol for Modulus\n");
    printf("Enter ^ symbol for Power \n");
    printf("Enter ! symbol for Factorial \n\n");
}
int calcinput()
{

        char Calc_oprn;
        calculator_operations();
        do
        {
                printf("\n");
                printf("Enter the operation you want to perform:\n");
                scanf("%*c%c",&Calc_oprn);
                switch(Calc_oprn)
                {
                        case '+':addition();
                                break;
                        case '-':subtraction();
                                break;
                        case '*':multiplication();
                                break;
                        case '/':division();
                                break;
                        case '?':modulus();
                                break;
                        case '!':factorial();
                                break;
                        case '^':power();
                                break;
                        case 'H':
                        case 'h':calculator_operations();
                                break;
                        case 'Q':
                        case 'q':exit(0);
                                break;

                }
        }while(Calc_oprn!='q'&&Calc_oprn!='Q');
}
int age5()
{

                    printf("\tHI!EXPLORE MATH BY COUNTING STARS :)\n");
                    l2:printf("enter the number of STARS shown:\n");
                    printf("\t\t*\t*\t*\n");
                    printf("count::");
                    int n1;
                    scanf("%d",&n1);
                    printf("\t*\t*\n");
                    printf("count::");
                    int n2;
                    scanf("%d",&n2);
                    printf("now,count the total stars:\n");
                    int n3;
                    scanf("%d",&n3);
                    int n4;
                    n4=n1+n2;
                    if(n4==n3)
                     printf("\n\tCONGRATS!!YOU SUCCESSFULLY MASTERED ADDITION OPERATION\n");
                     else
                     printf("\nMORE EXPLORATION NEEDED!!TAKE ANOTHER CHANCE--\n");
                     l3:printf("press 1 to try the game again,0 to exit\n");
                     int n5;
                     scanf("%d",&n5);
                     if(n5==1)
                                goto l2;
                     else if(n5==0)
                                main();
                     else
                        {
                                printf("wrong input,enter again:\n");
                                goto l3;
                        }
}


void operations1()
{
        printf("\n\t***enjoy math learning by exploring the important basics of your high school***\n");
        l4:printf("\n\tchoose the arena you want to master:\n");
        printf("\n1.TRANSPOSE OF MATRICES\n");
        printf("\n2.FINDING ROOTS OF QUADRATIC EQUATION\n");
        printf("\n3.BINARY OPERATIONS\n");
        int ch;
        scanf("%d",&ch);
        if(ch==1)
                matrixtranspose();
        else if(ch==2)
                qeroots();
        else if(ch==3)
                binaryoperations();
        else
                {
                        printf("invalid option\n");
                        goto l4;
                }

}

//function for Binary Addition
int binAddition(int a,int b)
{
      int c,j1; //carry
      while (b != 0) {
              //find carry and shift it left
              c = (a & b) << 1;
              //find the sum
              a=a^b;
              b=c;
      }
      return a;

}

//function for Binary Subtraction
int binSubtracton(int a, int b)
{
      int carry,j1;
      //get 2's compliment of b and add in a
      b = binAddition(~b, 1);

      while (b != 0) {
              //find carry and shift it left
              carry = (a & b) << 1;
              //find the sum
              a = a ^ b;
              b = carry;
      }
      return a;


}


int binaryoperations()
{
    int number1,number2, binAdd, binSub,j1;

    printf("Input first integer value: ");
    scanf("%d",&number1);

    printf("Input second integer value: ");
    scanf("%d",&number2);

    binAdd=binAddition(number1,number2);
    binSub=binSubtracton(number1,number2);

    printf("Binary Addition: %d\n",binAdd);
    printf("Binary Subtraction: %d\n",binSub);

    return 0;


}
int qeroots()
{
   int a, b, c, d,j1;
   double root1, root2;

   printf("Enter a, b and c where a*x*x + b*x + c = 0\n");
   scanf("%d%d%d", &a, &b, &c);

   d = b*b - 4*a*c;

   if (d < 0) { //complex roots
     printf("First root = %.2lf + j%.2lf\n", -b/(double)(2*a), sqrt(-d)/(2*a));
     printf("Second root = %.2lf - j%.2lf\n", -b/(double)(2*a), sqrt(-d)/(2*a));
   }
   else { //real roots
      root1 = (-b + sqrt(d))/(2*a);
      root2 = (-b - sqrt(d))/(2*a);

      printf("First root = %.2lf\n", root1);
      printf("Second root = %.2lf\n", root2);
   }

   return 0;

}

int matrixtranspose()
{
   int m, n, c, d, matrix[10][10], transpose[10][10];

   printf("Enter the number of rows and columns of matrix\n");
   scanf("%d%d", &m, &n);

   printf("Enter elements of the matrix\n");

   for (c = 0; c < m; c++)
      for(d = 0; d < n; d++)
         scanf("%d", &matrix[c][d]);

   for (c = 0; c < m; c++)
      for( d = 0 ; d < n ; d++ )
         transpose[d][c] = matrix[c][d];

   printf("Transpose of the matrix:\n");

   for (c = 0; c < n; c++)
   {
      for (d = 0; d < m; d++)
         printf("%d\t", transpose[c][d]);
      printf("\n");
   }

   return 0;


}

void explorer()
{
        int chh;
        printf("      ***HI EXPLORER***     ");
        printf("   learning is always awesome  but with fun  \n");
        l5:printf("choose your way:\n");
        printf("1.play and rejoice\n");
        printf("2.get set learn\n");
        scanf("%d",&chh);
        switch(chh)
        {
                case 1:
                    tictactoe();
                        break;
                case 2:
                    student();
                        break;
                default:printf("\nwrong option,re--enter\n");
                        goto l5;
        }
}

int tictactoe()
        {
                int p=1,i,choice,j1;
                char mark;
                do
                {
                        input();
                        p=(p%2)?1:2;
                        printf("Player %d,enter a number:\n",p);
                        scanf("%d",&choice);

                        mark=(p==1)?'x':'o';
                        if (choice == 1 && square[1] == '1')
                           square[1] = mark;
                        else if (choice == 2 && square[2] == '2')
                           square[2] = mark;
                        else if (choice == 3 && square[3] == '3')
                           square[3] = mark;
                        else if (choice == 4 && square[4] == '4')
                           square[4] = mark;
                        else if (choice == 5 && square[5] == '5')
                           square[5] = mark;
                        else if (choice == 6 && square[6] == '6')
                           square[6] = mark;
                        else if (choice == 7 && square[7] == '7')
                           square[7] = mark;
                        else if (choice == 8 && square[8] == '8')
                           square[8] = mark;
                        else if (choice == 9 && square[9] == '9')
                           square[9] = mark;
                        else
                        {
                            printf("Invalid move ");
                        }
                        i=cwin();
                        p++;
                }while(i==-1);
                input();
                if(i==1)
                        printf("\n\t***CONGRATS!!!***\n\t***PLAYER %d WINS***",--p);
                else
                        printf("***GAME DRAW***");
}
int cwin()
{
    if (square[1] == square[2] && square[2] == square[3])
        return 1;

    else if (square[4] == square[5] && square[5] == square[6])
        return 1;

    else if (square[7] == square[8] && square[8] == square[9])
        return 1;

    else if (square[1] == square[4] && square[4] == square[7])
        return 1;

    else if (square[2] == square[5] && square[5] == square[8])
        return 1;

    else if (square[3] == square[6] && square[6] == square[9])
        return 1;

    else if (square[1] == square[5] && square[5] == square[9])
        return 1;

    else if (square[3] == square[5] && square[5] == square[7])
        return 1;

    else if (square[1] != '1' && square[2] != '2' && square[3] != '3' &&
        square[4] != '4' && square[5] != '5' && square[6] != '6' && square[7]
        != '7' && square[8] != '8' && square[9] != '9')

        return 0;
    else
        return  - 1;
}


//FUNCTION TO DRAW BOARD OF TIC TAC TOE WITH PLAYERS MARK
 void input()

{
                printf("\n\t\twelcome to");
                printf("\n\t\t=>TIC TAC TOE<=\n");
                printf("Player 1 (X)  -  Player 2 (O)\n\n\n");


                printf("     |     |     \n");
                printf("  %c  |  %c  |  %c \n", square[1], square[2], square[3]);
                printf("_____|_____|_____\n");
                printf("     |     |     \n");
                printf("  %c  |  %c  |  %c \n", square[4], square[5], square[6]);
                printf("_____|_____|_____\n");
                printf("     |     |     \n");
                printf("  %c  |  %c  |  %c \n", square[7], square[8], square[9]);
                printf("     |     |     \n\n");
}

void main()
{
        int age,designation;
        m1:do
        {
                l1:printf("\n\tWELCOME TO THE MATH FORUM!!!\n");
                printf("\nplease enter your designation according to the list below:\n");
                printf("1.STUDENT--^.^ \n");
                printf("2.EXPLORER--:) \n");
                printf("3.Exit--:( \n");
                scanf("%d",&designation);

        //here designation of the user is basic tool for classifying the proceedings of the program

                switch(designation)
                {
                        case 1:student();
                                break;
                        case 2:explorer();
                                break;
                        case 3:exit(0);
                                break;
                                default:
                                {
                                        printf("\n---oops!--you have entered a wrong option.\nplease re-enter your input to proceed:\n");
                                        goto l1;
                                        break;
                                }
                }
        }while(designation!=3);
}

void student()
{
        int age;
        printf("\tWELCOME LEARNER!!!\n");
        printf("\nEnter your age to start exploring:\n");
        scanf("%d",&age);
        if(age<5)
                {
                        age5();
                }
        if(age>=5 && age<12)
                {
                        calcinput();
                }
        if(age>=12 && age<18)
                {
                        operations1();
                }
}

void forexit()
{
        char mm;
        l6:printf("\n*please enter c to continue and q to exit* :\n");
        scanf("%*c%c",&mm);
        switch(mm)
                {
                case 'c':
                case 'C':main();break;
                case 'q':
                case 'Q':exit(0);break;
                deafult:
                        {
                        printf("\noops--you entered a wrong option.enter again:\n");
                        goto l6;
                        }
             }
}



