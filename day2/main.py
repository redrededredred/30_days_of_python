"""
Day 2
"""
import math

# Level 1
first_name: str = "John"
last_name: str = "Hardcore"
full_name: str = first_name + last_name
country: str = "Alaska" # :DDDDD
city: str = "Berlin"
age: float = 27.3
year: int = 2024
is_married: bool = True
is_true: bool = False
is_light_on: bool = True

# Level 2   
print(type(first_name))
# ...
print(len(first_name))
print(f"Lenght of Firstname: {len(first_name)}")
print(f"Lenght of Firstname: {len(last_name)}")

num_one: int = 5
num_two: int = 4
total: int = num_one + num_two
diff: int = num_one - num_two
product: int = num_two * num_one
division: float = num_two / num_one
remainder: int = num_two % num_one
exp: int = num_one**num_two
floor_division: int = num_one // num_two

def circle_circumference(radius: int) -> float:
    """
    Calculates the circumference of a circle.

    radius - radius of a circle as ints
    returns - circumference as a float    
    """
    return 2 * math.pi * radius

def circle_area(radius: int) -> float:
    """
    Calculates the area of a circle.

    radius - radius of a circle as int
    returns - area as a float
    """
    return math.pi * radius**2

def leech_data() -> None:
    """
    Gets some data from the user.

    return - None
    """

    first_name: str = input("Whats ur first name?")
    last_name: str = input("Whats ur last name?")
    country: str = input("Where do you live (country)?")
    age: int = int(input("How old are you?"))

def main() -> None:
    data: int = int(input("Enter a radius as an int: "))
    print(circle_circumference(data))
    print(circle_area(data))

if __name__ == "__main__":
    main()