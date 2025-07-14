import math
import os

filename = "input_multiple.txt"

if not os.path.isfile(filename):
    with open(filename, "w") as f:
        f.write("1 -3 2\n")     
        f.write("1 -2 1\n")     
        f.write("1 1 1\n")      
    print(f"'{filename}' was not found, so it has been created with 3 default equations.")

print("\n>> Solving multiple quadratic equations from", filename)

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    for idx, line in enumerate(lines, 1):
        try:
            a, b, c = map(float, line.strip().split())
            print(f"\nEquation {idx}: {a}x² + {b}x + {c} = 0")
            discriminant = b**2 - 4*a*c

            if discriminant > 0:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                print(" → Two real roots:", root1, "and", root2)
            elif discriminant == 0:
                root = -b / (2*a)
                print(" → One real root:", root)
            else:
                print(" → No real roots (complex roots).")
        except ValueError:
            print(f" → Error: Invalid coefficients in line {idx}: '{line.strip()}'")

except Exception as e:
    print("Unexpected error:", e)
