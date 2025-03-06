def Triangle(height):
    for row in range(height):
        for col in range(row + 1):
            print("*", end="")
        print()


Triangle(6)
