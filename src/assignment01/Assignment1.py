my_string: str = "my string"
my_integer: int = 1
my_float: float = 1.1

int1: int = 2
int2: int = 3
int3: int = int1 + int2
# I expect the value of int 3 to be 5

print(int3)

float1: float = 2.2
float2: float = 3.3
float3: float = float1 + float2
# I expect the value of int3 to be 5.5

print(float3)

string1: str = "aaa"
string2: str = "bbb"
string3: str = string1 + string2
# I expect the value of string3 to be "aaabbb"

print(string3)

intflt1 = int1 + float1
# I expect the value of intflt1 to be 4.2

print(intflt1)

#intstr1 = int1 + string1
# I expect that this will throw and errors since you cannot add an int and a string together

#print(intstr1)
# The output was an error because you cannot add an int and a string together

print(type(my_string))
print(type(my_integer))
print(type(my_float))

stringint1 = "4"
print(type(stringint1))
int4: int = int(stringint1)
print(type(int4))

roundedfloat1: float = round(5*7.654321, 3)
print(roundedfloat1)

my_name: str = input("Enter your name")
print(my_name)

favorite_number = input("Enter your favorite number")
print(favorite_number)
# I expect the type of favorite_number to be a string
print(type(favorite_number))
# favorite_number is a string because input is accepted as a string unless the variable type for input is declared otherwise

num1 = input("Please enter a number")
num2 = input("Please enter another number")
num3 = num1 + num2
# I expect the value of int7 to be int5 and int6 next to each other in string format
print(num3)
num4 = int(num1) + int(num2)
# I expect in8 to be the sum value of int5 and int6
print(num4)