import numpy as np


def main():
    print('Welcome in program which finds closest path between 2 or more points ')
    points = int(input('How many points want you check?: '))
    coordinate = []
    for i in range(1, (points+1)):
        x1 = input(f'{i} Coordinate (A): ')
        x2 = input(f'{i} Coordinate (B): ')
        coordinate.append((x1, x2))

    print(coordinate)


main()
