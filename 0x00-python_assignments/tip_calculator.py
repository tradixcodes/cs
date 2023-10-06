def tip_calculator(bill, tip_percentage):
    tip_amount = bill * tip_percentage
    total_bill = tip_amount + bill
    return total_bill

def main():
    bill = float(input("Enter the bill: "))
    tip_percentage = float(input("Enter the tip percentage; choose either 10, 12, or 15: "))

    if tip_percentage in {10.0, 12.0, 15.0}:
        tip_percentage /= 100.0
        total_bill = tip_calculator(bill, tip_percentage)
    else:
        print("Invalid input!")
        return

    num = int(input("Enter the number of people splitting the bill: "))
    bill_per_person = total_bill / num
    print(f"Your bill per person is: {bill_per_person:.2f}")

if __name__ == "__main__":
    main()
