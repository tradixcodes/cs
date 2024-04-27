#include <stdio.h>
#include <stdlib.h>

int main()
{
        double amount, time, principal;
        int i;

        printf("Enter the deposit amount: ");
        scanf("%lf", amount);

        printf("Enter duration in years: ");
        scanf("%lf", time);

        for (i = 0; i < time; i++)
        {
                principal = amount;
                amount = (principal * time * 0.3)/100 ;
        }

        printf("Amount : %.02lf" ,amount);
        return(0);
}