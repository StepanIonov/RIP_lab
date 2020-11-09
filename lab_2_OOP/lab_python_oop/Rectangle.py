import lab_python_oop.Geometric_figure as Geom_fig
import lab_python_oop.Figure_color as Color_fig


class Rectangle(Geom_fig.Figure):
    __name = 'Прямоугольник'

    def __init__(self, width, length, color):
        self._width = width
        self._length = length
        self._color = Color_fig.Color()
        self._color = color

    @staticmethod
    def get_name():
        return Rectangle.__name

    @property
    def width(self):
        """It's the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @width.deleter
    def width(self):
        del self._width

    @property
    def length(self):
        """It's the length of the rectangle"""
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @length.deleter
    def length(self):
        del self._length

    def space(self):
        """It's the space of the rectangle"""
        return self._width * self._length

    def __repr__(self):
        return '''{} имеет {} цвет, ширину {} 
и длину {}. Его площадь {}'''.format(Rectangle.get_name(), self._color, self._width, self._length, self.space())
