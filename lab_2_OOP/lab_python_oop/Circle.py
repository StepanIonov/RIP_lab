import lab_python_oop.Geometric_figure as Geom_fig
import lab_python_oop.Figure_color as Color_fig
from math import pi


class Circle(Geom_fig.Figure):
    __name = 'Окружность'

    def __init__(self, radius, color):
        self._radius = radius
        self._color = Color_fig.Color()
        self._color = color

    @staticmethod
    def get_name():
        return Circle.__name

    @property
    def radius(self):
        """It's the radius of the circle"""
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

    def space(self):
        """It's the space of the circle"""
        return float('{:.2f}'.format(pi * self._radius ** 2))

    def __repr__(self):
        return '''{} имеет {} цвет, радиус {}.
Её площадь {}'''.format(Circle.get_name(), self._color, self._radius, self.space())
