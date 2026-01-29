# Day 2: 30 Days of Python Programming
# Variable Sude

first_name = "Sude"
last_name = "Moon"
full_name = first_name + " " + last_name
country = 'Japan'
city = 'Okinawa'
age = 23
is_married = False
is_true = True
is_light_on = True
mom_name, dad_name = 'Yumi', 'Hiroshi'

# level 1 excercise finished

# level 2 excercise
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(mom_name))
print(type(dad_name))
print("*****************************************")

print(len(first_name))
print(len(last_name))
print(max(len(first_name), len(last_name)))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_div = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_div)
print("*****************************************")

radius_user = input("Enter radius: ")
area_of_circle = 3.14 * float(radius_user) ** 2
circum_of_circle = 2 * 3.14 * float(radius_user)

print("Area of circle:", area_of_circle)
print("*****************************************")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print(f"Your first name is {first_name}, your last name is {last_name}. You are from {country} and you are {age} years old.")