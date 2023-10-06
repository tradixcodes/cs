#include <stdio.h>
/*
 * tip_calculator - function that calculates the tip and adds to the total bill
 * 
 * @bill: parameter for charge of services offered
 * @tip_percentage: parameter for desired tip percentage
 * 
 * Return: total_bill
*/
double tip_calculator(double bill, double tip_percentage)
{
    double tip_amount = bill * tip_percentage;
    double total_bill = tip_amount + bill;
    return total_bill;
}
/**
 * main - Entry point
 * 
 * void: no parameter
 * 
 * Return: -1 (fail), 0 (success)
*/
int main(void){
    double bill, total_bill, bill_per_person, tip_percentage;
    int num;

    printf("Enter the bill: ");
    scanf("%lf", &bill);
    printf("\nEnter the tip percentage; choose either 10, 12 or 15: ");
    scanf("%lf", &tip_percentage);

    if (tip_percentage == 10.0 || tip_percentage == 12.0 || tip_percentage == 15.0)
    {
        tip_percentage = tip_percentage / 100;
        total_bill = tip_calculator(bill, tip_percentage);
    }
    else
    {
        printf("Invalid input!\n");
        return (-1);
    }

    printf("\nEnter the number of people splitting the bill: ");
    scanf("%d", &num);
    
    bill_per_person = total_bill / num;
    printf("Your bill is: %.02lf\n", bill_per_person);

    return (0);
}