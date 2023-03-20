import requests
from datetime import datetime

def get_data(url):
    """
    Функция получает данные из файла operations.json
    :return: Список операций в виде списка словарей
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно!"
    except Exception as e:
        return None, e
    return None, f"WARNING: Статус ответа {response.status_code}"


def get_filtered_data(data, filtered_empty_from=False):
    """
    Функция, которая выводит оследние 5 выполненных (EXECUTED) операций
    """
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data,count_last_values):
    """
    Функция, которая ставит сверху самые последние операции (по дате)
    :return:
    """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data):
    """
    Функция, которая переводит дату в формат ДД.ММ.ГГГГ, а также
    Номер карты замаскирован и не отображается целиком, а в формате  XXXX XX** **** XXXX
    Номер счета замаскирован и не отображается целиком, а в формате  **XXXX
    """
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        if "from" in row:
            sender = row["from"].split()
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_info = " ".join(sender)
        else:
            sender_bill, sender_info = "", ["СКРЫТО"]

        recipient = f"**{row['to'][-4:]}"

        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} -> Счет {recipient}
{amount}
""")
        return formatted_data