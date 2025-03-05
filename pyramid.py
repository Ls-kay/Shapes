def full_pyramid(height):
    for row in range(1, height + 1):
        # print empty spaces
        for col in range(height - row):
            print(" ", end="")

        # print asterisks for curent row
        for col1 in range(1, 2 * row):
            print("*", end="")

        print()


full_pyramid(3)
