# Introduction
print("Let's calculate the area of a trapezoid!")

# Get user input and convert to numbers (floats)
base1 = float(input("What is the base1 (cm)? "))
base2 = float(input("What is the base2 (cm)? "))
height = float(input("What is the height (cm)? "))

# Perform the calculation
# Formula: A = ((a + b) / 2) * h
area = (base1 + base2) / 2 * height

# Display the result using an f-string for cleaner formatting
print(f"\nThe area of the trapezoid with base1 {base1}cm, base2 {base2}cm, "
      f"and height {height}cm gives us an area of {area}cm².")