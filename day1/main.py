"""
Day 1
"""
import math

# Level 1
def hello_world() -> None:
    print(1+1)
    print(7-1)
    print(4*4)
    print(40%15)
    print(60/10)
    print(2**2)
    print(40//3)

    print("Jeff")
    print("Retard")
    print("Atlantis")
    print("I am enjoying 30 day of python") # that's a lie, i'm just bored

    print(type(10))
    print(type(9.8))
    print(type(3.14))
    print(type(4 - 4j))
    print(type(['Asabeneh', 'Python', 'Finland']))
    print(type("Jeff"))
    print(type("Retard"))
    print(type("Atlantis"))

# Level 2
def example_datatypes() -> None:
    examples: list = [
        42,
        21.732,
        2j,
        "Im am a String",
        "False",
        ["1", "1"],
        {2, 2},
        (3, 3),
        {"1": 2, "2": 1},
        bytearray(8),
        bytes(4)

    ]

    for i in examples:
        print(i, " is of type ", type(i))

def find_euclidian_distance(points: tuple[tuple]) -> int:
    """
    Finds the euclidian distance between to points.

    points - a tuple containing two tuples referencing a point e.g. ((2,1), (8,3))
    return - the distance as an int
    """
    distance: int = math.sqrt((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)

    return distance # i hate math

def main() -> None:
    hello_world()
    example_datatypes()
    print(find_euclidian_distance(((2, 3),(10, 8))))

if __name__ == "__main__":
    main()