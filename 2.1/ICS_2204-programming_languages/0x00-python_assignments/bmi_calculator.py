## SCT211-0009/2022
## Njoroge Kanyagia

def bmicalculator(h, w):
    bmi = w / (h ** 2)
    
    print(f"Your BMI is: {bmi}")
    
    if bmi < 18.5:
        print("You are underweight!")
    elif 18.5 <= bmi <= 24.9:
        print("You have normal weight!")
    elif 25 <= bmi <= 29.9:
        print("You are overweight!")
    else:
        print("You are obese!")

def main():
    weight = float(input("Enter your weight (in kilograms): "))
    height = float(input("Enter your height (in meters): "))
    
    print()
    bmicalculator(height, weight)

if __name__ == "__main__":
    main()
