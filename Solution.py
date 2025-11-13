import sys
import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    q = int(data[0])
    idx = 1
    outputs = []

    for _ in range(q):
        shape = data[idx]
        idx += 1

        if shape == "rectangle":
            length = float(data[idx])
            width = float(data[idx + 1])
            idx += 2
            rectangle = Rectangle(length, width)
            outputs.append(rectangle.area())
        elif shape == "circle":
            radius = float(data[idx])
            idx += 1
            circle = Circle(radius)
            outputs.append(circle.area())
        else:
            raise ValueError("Unknown shape: " + shape)

    formatted = "\n".join("{0:.2f}".format(value) for value in outputs)
    sys.stdout.write(formatted)


if __name__ == "__main__":
    main()

