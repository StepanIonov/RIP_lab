from lab_python_oop.Circle import Circle
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Square import Square
import pygame  # another module loaded using pip


def main():
    """It's main function that is called after this module is launched."""
    variant = 20  # variant number in your group
    color = ['синий', 'зеленый', 'красный']  # colors of the figures
    call_my_packet(variant, color)
    call_other_packet(variant, color)


def call_my_packet(variant, color):
    """Using of my own modules. Variant is number of variant.
    Color is list of 3rd colors: rectangle, circle, square."""
    print('В соответствии со входными данными: ')
    my_rect = Rectangle(variant, variant, color[0])
    print(my_rect)
    my_circle = Circle(variant, color[1])
    print(my_circle)
    my_square = Square(variant, color[2])
    print(my_square)


def call_other_packet(variant, color):
    """Using of another module. Variant is number of variant.
    Color is list of 3rd colors: rectangle, circle, square."""
    flag_error = False  # shows if there is incorrect parameters
    fps = 10  # number of frames per second
    start_pos_x, start_pos_y = 0, 0  # starting position of print in the window
    screen_size_x, screen_size_y = 320, 240  # the size of the window
    if (start_pos_x + 4 * variant) > screen_size_x or (start_pos_y + 4 * variant) > screen_size_y or variant < 1:
        max_var = min((screen_size_x - start_pos_x) / 4, (screen_size_y - start_pos_y) / 4)
        while variant < 1 or variant > max_var:
            flag_error = True
            print("""При таком значении 'variant' картинка не будет правильно отображаться.
    Выберите значение от 1 до {}: """.format(max_var), end="")
            try:
                variant = int(input())
            except ValueError:
                pass
    step = {'rect_x': start_pos_x, 'rect_y': start_pos_y,  # coordinates for showing in the window
            'circle_x': start_pos_x + 2*variant,
            'circle_y': start_pos_y + 2*variant,
            'square_x': start_pos_x + 3*variant, 'square_y': start_pos_y + 3*variant}
    color_rgb = {'rect': color[0], 'circle': color[1], 'square': color[2]}  # for changing text-color to rgb-color
    find_rgb(color_rgb)
    if flag_error:
        print("-----------Новые данные-----------")
        call_my_packet(variant, color)
    pygame.init()
    sc = pygame.display.set_mode((screen_size_x, screen_size_y))
    sc.fill((255, 255, 255))
    pygame.draw.rect(sc, color_rgb['rect'], (step['rect_x'], step['rect_y'], variant, variant))
    pygame.draw.circle(sc, color_rgb['circle'], (step['circle_x'], step['circle_y']), variant)
    pygame.draw.rect(sc, color_rgb['square'], (step['square_x'], step['square_y'], variant, variant))

    clock = pygame.time.Clock()
    pygame.display.update()
    while True:
        clock.tick(fps)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return


def find_rgb(color_rgb):
    """Giving of the conformity text-color and rgb-color.
    Color_rgb is dict that keeps the names of colors.
    This function changes color_rgb from text to rgb-format"""
    name = {'rect': 'прямоугольник', 'circle': 'окружность', 'square': 'квадрат'}
    for i in color_rgb:
        not_find = True
        while not_find:
            if color_rgb[i] == 'красный':
                color_rgb[i] = (255, 0, 0)
                not_find = False
            elif color_rgb[i] == 'зеленый' or color_rgb[i] == 'зелёный':
                color_rgb[i] = (0, 255, 0)
                not_find = False
            elif color_rgb[i] == 'синий':
                color_rgb[i] = (0, 0, 255)
                not_find = False
            else:
                color_rgb[i] = input("""В программе задан неожиданный цвет для фигуры '{}'. 
        Выберите для нее один из цветов: 'красный', 'зеленый', 'синий': """.format(name[i]))


if __name__ == '__main__':
    main()
