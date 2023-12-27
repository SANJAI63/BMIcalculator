def calculate_bmi(weight_kg, height_m):

    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
def test(weight,height):
    if weight<0 :
        print("height cannot be negative plz enter valid input to get  result")
        return False
    elif  height <0:
        print("height cannot be negative plz enter valid input to get  result")
        return False
    elif weight==0:
        print("weight cannot be zero enter valid input result")
        return False
    elif height==0:
        print("height  cannot be zero enter valid input result")
        return False
    else:
        print("your inputs are valid you will get result")
        return True
def main():
    print("BMI Calculator")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    flag=test(weight,height)
    if flag:
        bmi_result = calculate_bmi(weight, height)
        bmi_category = interpret_bmi(bmi_result)

        print("\nYour BMI is {:.2f}".format(bmi_result))
        print("BMI Category: {}".format(bmi_category))

if __name__ == "__main__":
    main()
