# Решить задания, которые не успели решить на семинаре.
# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним, только если треугольник существует .
# Пример
# На входе:
# a = 4
# b = 4
# c = 4


import argparse
import sys
import logging

logging.basicConfig(filename='zanatie_15_stand_labrori/error.log',
                    level=logging.INFO, filemode='a', encoding='utf-8')


def check_triangle(a, b, c):
    if a + b <= c or c + b <= a or c + a <= b:
        logging.error('Треугольник не существует')
    elif a == b == c:
        logging.info('Треугольник существует')
        logging.info('Треугольник равносторонний')
    elif a == b or b == c or a == c:
        logging.info('Треугольник существует')
        logging.info('Треугольник равнобедренный')
    else:
        logging.info('Треугольник существует')
        logging.info('Треугольник разносторонний')


def walker():
    parser = argparse.ArgumentParser(
        description='Проверяем, существует ли треугольник с заданными сторонами',
        prog='read_dir()')
    parser.add_argument('side_a', type=int, help='Длинна стороны a')
    parser.add_argument('side_b', type=int, help='Длинна стороны b')
    parser.add_argument('side_c', type=int, help='Длинна стороны c')
    args = parser.parse_args()

    logging.info('Проверка треугольника со сторонами {}, {}, {}'.
                 format(args.side_a, args.side_b, args.side_c))
    check_triangle(args.side_a, args.side_b, args.side_c)


if __name__ == '__main__':
    # a, b, c = map(int, input('Укажите 3 стороны в виде целых положительных чисел через пробел: ').split())
    # check_triangle(a, b, c)
    # Для запуска без командной строки требуется раскомментировать 2 верхних строки,
    # функцию walker() - закомментировать
    walker()