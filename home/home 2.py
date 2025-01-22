class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть реализован в дочернем классе.")

    def info(self):
        raise NotImplementedError("Метод info должен быть реализован в дочернем классе.")



class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(
            f"Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}²."
        )



class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(
            f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, "
            f"area: {self.calculate_area()}{Figure.unit}²."
        )


if __name__ == "__main__":

    squares = [Square(5), Square(7)]
    rectangles = [Rectangle(5, 8), Rectangle(6, 9), Rectangle(4, 10)]

    shapes = squares + rectangles

    for shape in shapes:
        shape.info()