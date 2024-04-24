def print_y_pattern(name):
    n = len(name)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print(name[j], end='')
            else:
                print(' ', end='')
        print()

name = "YOUR_NAME"
print_y_pattern(zeeshan)