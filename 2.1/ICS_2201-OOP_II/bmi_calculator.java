// SCT211-0009/2022
// Njoroge Kanyagia

import java.util.Scanner;

public class bmi_calculator {
    public static void calculateBMI(double h, double w){
        double bmi = (w / (h * h));
        
        System.out.printf("Your BMI is : %f\n", bmi);
        
        if (bmi < 18.5){
            System.out.println("You are underweight!");
        }else if (bmi <= 24.9){
            System.out.println("You have normal weight");
        }else if (bmi <= 29.9){
            System.out.println("You are overweight!");
        }else{
            System.out.println("You are obese!");
        }
    }
    public static void main(String[] args){
        double weight, height;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your weight in kilograms: ");
        weight = scanner.nextDouble();
        
        System.out.print("Enter your height in metres: ");
        height = scanner.nextDouble();      
        
        scanner.close();

        calculateBMI(height, weight);
    }
}