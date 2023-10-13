#include <stdio.h>
/**
 * SCT211-0009/2022
 * Njoroge Kanyagia
 * 
 * bmicalculator - calculates the body mass index
 * 
 * @h: height parameter 
 * @w: weight parameter
 * 
 * Return: void
*/
void bmicalculator(double h, double w)
{
    double bmi = (w / (h * h));
    
    printf("Your BMI is: %lf\n", bmi);
    
    if (bmi < 18.5)
    {
        puts("You are underweight!");
    }
    else if (bmi <= 24.9 && bmi >= 18.5)
    {
        puts("You have normal weight!");
    }
    else if (bmi <= 29.9 && bmi >= 25)
    {
        puts("You are overweight!");
    }
    else
    {
        puts("You are obese!");
    }
    
}
/**
 * main - Entry point
 * 
 * allows i/o and calculates bmi
 * 
 * Return: 0(success)
*/
int main(void)
{
    double weight, height;

    printf("Enter your weight(in kilograms): ");
    scanf("%lf", &weight);
    printf("\nEnter your height(in metres): ");
    scanf("%lf", &height);
    putchar('\n');

    bmicalculator(height, weight);
    return (0);
}