def calculate_bmi(weight, height):
    """Calculate Body Mass Index."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than zero.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Health Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    if _name_ == "_main_":
         main()