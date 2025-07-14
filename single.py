import math
import os

filename = "input_single.txt"
if not os.path.isfile(filename):
    with open(filename, "w") as f:
        f.write("1 -3 2\n")
    print(f"'{filename}' was not found, so it has been created with default values.")

try:
    
    with open(filename, "r") as file:
        line = file.readline()
        a, b, c = map(float, line.strip().split())

    print(f"\nEquation: {a}x² + {b}x + {c} = 0")

    
    discriminant = b**2 - 4*a*c

    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Two real roots:", root1, "and", root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("One real root:", root)
    else:
        print("No real roots. Discriminant is negative.")

except ValueError:
    print("Error: Could not parse the coefficients. Ensure the file has three numeric values.")
except Exception as e:
    print("Unexpected error:", e)
