from utils import get_data, get_filtered_data, get_last_data, get_formatted_data
from datetime import datetime

def main():
    """
    Функция, которая выводит на экран список из 5 последних выполненных клиентом операций в формате:
<дата перевода> <описание перевода>
<откуда> -> <куда>
<сумма перевода> <валюта>
    """
    OPERATIONS_URL = "https://api.npoint.io/c0177ed05cb3355459ac"
    COUNT_LAST_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_data(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    for row in data:
        print(row)

if __name__ == "__main__":
    main()