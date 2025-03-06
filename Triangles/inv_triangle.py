def Inverse_Triangle(height):
    for row in range(height, 0, -1):
        for col in range(0, row):
            print("*", end="")
        print()


Inverse_Triangle(5)
