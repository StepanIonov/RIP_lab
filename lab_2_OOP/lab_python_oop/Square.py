import lab_python_oop.Rectangle as Rect


class Square(Rect.Rectangle):
    __name = 'Квадрат'

    def __init__(self, length, color):
        self._length = length
        self._width = length
        self._color = color

    @staticmethod
    def get_name():
        return Square.__name

    def __repr__(self):
        return '''{} имеет {} цвет, длину {}.
Его площадь {}'''.format(Square.get_name(), self._color, self._length, self.space())
