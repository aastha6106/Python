print(type(10))
print(type(10.5))
print(type(10 + 9j))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({"a": 1, "b": 2}))

first_name = "Aastha"
print(len(first_name))

last_name = "Aggarwal"
print(len(last_name))

if len(first_name) > len(last_name):
    print("First name is longer.")
else:
    print("Last name is longer.")

num_one = 5
num_two = 4

variable_total = num_one + num_two
print("Total:", variable_total)

variable_diff = num_one - num_two
print("Difference:", variable_diff)

variable_product = num_one * num_two
print("Product:", variable_product)

variable_division = num_one / num_two
print("Division:", variable_division)

variable_remainder = num_one % num_two
print("Remainder:", variable_remainder)

variable_exp = num_one ** num_two
print("Exponent:", variable_exp)

variable_floor_division = num_one // num_two
print("Floor Division:", variable_floor_division)

area_of_circle = 3.14 * 30 ** 2
print("Area of Circle:", area_of_circle)

circum_of_circle  = 2 * 3.14 * 30
print("Circumference of circle:", circum_of_circle)

radius = int(input("Enter radius of circle:"))
area_of_circle = 3.14 * radius ** 2
circum_of_circle  = 2 * 3.14 * radius
print("Area of Circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

First_name = input("Enter your first name: ")
Last_name = input("Enter your Last name: ")
Country = input("Enter your country: ")
City = input("Enter your city: ")
age = int(input("Enter your age: "))
print("First Name:", First_name)
print("Last Name:", Last_name)  
print("Country:", Country)
print("City:", City)
print("Age:", age)