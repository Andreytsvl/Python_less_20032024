# Погружение в Python | Коллекции
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

import argparse
import logging

logging.basicConfig(filename="zanatie_15_stand_labrori/error.log",
                    level=logging.INFO, filemode="a", encoding="utf-8")

def check_data(data):
    try:


        if data.isdigit():
            result = int(data)
        elif data.replace(".","").replace("-","").isdigit()\
        and data.count(".") < 2 and "-" not in data[1:]:
            result = float(data)
        elif not data.islower():
            result = data.lower()
        else:
            result = data.upper()
        logging.info(f'Проверка данных: "{data}" успешна. Результат: {result}')
        #print(f'{result= }')
        return result
    except Exception as e:
        logging.error(f'Ошибка при проверке данных: {e}')
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Проверка данных пользователя",
                                     prog="read_dir()")
    parser.add_argument("data", type=str,
                        help="Введите данные для проверки")
    args = parser.parse_args()

    logging.info(f'Запуск программы с переданными данными: "{args.data}"')
    processed_result = check_data(args.data)

    if processed_result is not None:
        print(f'Result: {processed_result}')