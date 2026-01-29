age = int (input("Enter your age: "))
height = float (input("Enter your height in meters: "))
try:
    complex_input = input("Enter a complex number (e.g., 1+2j): ")
    complex_number = complex(complex_input)
except ValueError:
    print("Invalid complex number format. Please enter a value like 1+2j.")
    complex_number = None
# third one is complex number in an exception handling block, we will learn it later

base = float(input("Enter the base of the triangle: "))
height_triangle = float(input("Enter the height of the triangle: "))
area_of_triangle = 0.5 * base * height_triangle
print("The area of the triangle is:", area_of_triangle)

side_1 = float(input('Enter first side of the triangle: '))
side_2 = float(input('Enter second side of the triangle: '))
side_3 = float(input('Enter third side of the triangle: '))

triangle_perimeter = side_1 + side_2 + side_3
print('The perimeter of the triangle is:', triangle_perimeter)

# 6 
length = int(input('Enter a length: '))
width = int(input('Enter a width: '))

area_rect = length * width
print('Area of the rectangle is: ', area_rect)

perimeter = 2 * length * width 
print('Perimeter of the rectangle is: ', perimeter)

# 7 
pi = 3.14
circle_radius = input('Enter a radius value: ')
area = pi * circle_radius**2
circumference = 2*pi*circle_radius

# 8
x, y = vars
equation = y == 2*x - 2
 
