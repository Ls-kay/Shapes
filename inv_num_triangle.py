def inverse_num_triangle(height):
    for row in range(height, 0, -1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()


inverse_num_triangle(5)
