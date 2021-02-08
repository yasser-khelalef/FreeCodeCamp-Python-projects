class Rectangle:
    def __init__(self, width, height):
        self.height=height
        self.width=width
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width=width

    def set_height(self, height):
        self.height=height

    def get_area(self):
        return (self.height*self.width)
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        line=""
        pic=""
        if self.height<50 and self.width<50:
            for i in range(self.width):
                line = line +"*"
            for i in range(self.height):
                pic = pic +line +"\n"
            return pic
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        vertical_fit = self.height//shape.height
        horizontal_fit = self.width//shape.width
        return vertical_fit*horizontal_fit

class Square(Rectangle):
    def __init__(self, slength):
        self.set_height(slength)
        self.set_width(slength)    

    def __str__(self):
        return f"Square(side={self.width})"   

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

a= Rectangle(4,8)
b=Rectangle(3,6)



print(a.get_amount_inside(b))