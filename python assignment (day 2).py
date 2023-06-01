def calculate_simple_interest(principal, time, gender, age):
    if gender == 'female' and age >= 60:
        rate = 8
    elif gender == 'female' and age < 60:
        rate = 6
    elif gender == 'male' and age >= 60:
        rate = 7
    else:
        rate = 5

    interest = (principal * rate * time) / 100
    return interest

principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period (in years): "))
gender = input("Enter the gender (male/female): ")
age = int(input("Enter the age: "))

simple_interest = calculate_simple_interest(principal, time, gender, age)
print("Simple Interest:", simple_interest)
