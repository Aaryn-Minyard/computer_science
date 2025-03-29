import math
def hypo():
    while True:
        a = int(input("First leg: "))
        b = int(input("Second leg: "))
        if a <= 0 or b <= 0:
            print("Error: The lengths of the legs must be positive.")
        else:
            c = math.sqrt(a**2 + b**2)
            print(f"Right triangle has side lengths {a:.2f} and {b:.2f}")
            print(f"the Hypotenuse is {c:.2f}")

hypo()