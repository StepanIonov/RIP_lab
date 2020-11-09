import json
import sys
from task5_print_result import print_result
from task3_unique import Unique
from task1_field import field
from task2_gen_random import gen_random
from task6_cm_timer import cm_timer_1


if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print('Файл не задан! Укажите путь к файлу в качестве параметра')
    sys.exit(1)
with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name')))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    gen_salary = list(gen_random(len(arg), 100000, 200000))
    work_and_salary = list(zip(arg, gen_salary))
    return list(map(lambda x: x[0] + ', зарплата ' + str(x[1]) + ' руб', work_and_salary))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
