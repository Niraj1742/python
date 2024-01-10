class rectangle:
    
    def __init__(self, height, width):
        self.width = width
        self.height = height
    
    # def set_dimensions(self, height, width):
    #     self.height = height
    #     self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)

rectangle1 = rectangle(4, 3)
# rectangle1.set_dimensions(4, 3)
print("the height and width of rectangle", rectangle1.height, rectangle1.width)
print(rectangle1.area())
print(rectangle1.perimeter())
