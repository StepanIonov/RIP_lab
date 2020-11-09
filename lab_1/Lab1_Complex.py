from cmath import sqrt
import argparse
import sys


def create_parser():  # получение параметров командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("a", nargs="?")
    parser.add_argument("b", nargs="?")
    parser.add_argument("c", nargs="?")
    return parser.parse_args()


def get_from_param(val, instructions):  # проверка параметров
    try:
        return complex(val)
    except ValueError:
        print(instructions['param_value_error'])
        print(instructions['instr_for_parameters'])
        sys.exit()
    except TypeError:
        print(instructions['param_type_error'])
        print(instructions['instr_for_parameters'])
        sys.exit()


def get_from_input(input_request, error_msg):  # проверка ввода
    while True:
        try:
            coefficient = input(input_request)
            return complex(coefficient)
        except ValueError:
            print(error_msg)
        except EOFError:
            print(error_msg)


def main_solution(root, str1, str2):  # вывод решения при 'a', не равном нулю,
    if root.real == 0:                # и не нулевом дискриминанте
        print(str1, " = ", root.imag, "j", sep="")
        print(str2, " = ", -root.imag, "j", sep="")
    elif root.imag == 0:
        print(str1, " = ", root.real, sep="")
        print(str2, " = ", -root.real, sep="")
    else:
        print(str1, " = ", root, sep="")
        print(str2, " = ", -root, sep="")


instr = dict(intro="""Ионов Степан Александрович, ИУ5-52Б
Данная программа предназначена для решения биквадратного
уравнения вида ax^4+bx^2+c=0 относительно переменной "x",
где коэффициенты a,b,c принадлежат множеству комплексных чисел;
запись "x^n" равносильна действию операции возведения числа x
в натуральную степень n\n""",
             request_for_first_coeff="Введите коэффициент a: ",
             request_for_second_coeff="Введите коэффициент b: ",
             request_for_third_coeff="Введите коэффициент c: ",
             param_value_error="Ошибка типа данных параметров командной строки!",
             param_type_error="Не хватает параметров командной строки!",
             instr_for_parameters="Введите коэффициенты a,b,c через пробел",
             input_value_error="""Ошибка ввода! Необходимо ввести
число вида a+bj, где a,b - действительные числа;
j - мнимая единица. Слагаемое "bj" может отсутствовать""")                
print(instr['intro'])
if len(sys.argv) > 1:  # коэффициенты как параметры командной строки
    namespace = create_parser()
    a = get_from_param(namespace.a, instr)
    b = get_from_param(namespace.b, instr)
    c = get_from_param(namespace.c, instr)
else:  # коэффициенты как вводимые данные по запросу
    a = get_from_input(instr['request_for_first_coeff'],
                       instr['input_value_error'])  # старший коэффициент уравнения
    b = get_from_input(instr['request_for_second_coeff'],
                       instr['input_value_error'])  # средний коэффициент уравнения
    c = get_from_input(instr['request_for_third_coeff'],
                       instr['input_value_error'])  # свободный член уравнения
print("\nРЕШЕНИЕ:")
if a == 0:  # анализ решений и выдача ответа
    if b != 0:
        if c != 0:
            z = sqrt(-c/b)
            if z.real == 0:
                print("x1 = ", z.imag, "j", sep="")
                print("x2 = ", -z.imag, "j", sep="")
            else:
                print("x1 = ", z.real, sep="")
                print("x2 = ", -z.real, sep="")
        else:
            z = 0.0
            print("x = ", z, sep="")
    elif b == 0 and c == 0:
        print("x - любой из множества комплексных чисел")
    else:
        print("Решений нет")
elif b != 0 and c == 0:
    z = sqrt(-b/a)
    print("x1 = x2 = ", 0, sep="")
    if z.real == 0:
        print("x3 = ", z.imag, "j", sep="")
        print("x4 = ", -z.imag, "j", sep="")
    else:
        print("x3 = ", z.real, sep="")
        print("x4 = ", -z.real, sep="")
else:
    d = b**2 - 4*a*c  # дискриминант уравнения относительно второй степени
    if d == 0:
        t = sqrt(-b/(2*a))
        if t == 0:
            print("x = ", 0, sep="")
        else:
            if t.real == 0:
                print("x1 = x2 = ", t.imag, "j", sep="")
                print("x3 = x4 = ", -t.imag, "j", sep="")
            else:
                print("x1 = x2 = ", t.real, sep="")
                print("x3 = x4 = ", -t.real, sep="")
    else:
        t1 = sqrt((-b+sqrt(d))/(2*a))
        t2 = sqrt((-b-sqrt(d))/(2*a))
        main_solution(t1, "x1", "x2")
        main_solution(t2, "x3", "x4")
