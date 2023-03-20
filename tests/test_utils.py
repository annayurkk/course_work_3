import pytest

from utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def test_get_data():
    url = "https://api.npoint.io/c0177ed05cb3355459ac"
    assert get_data(url) is not None
    url = "https://api.npoint.io/c017ed05cb3355459ac"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Статус ответа 500"


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 5
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 4


def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2021-08-26T10:50:58.294041'
    assert len(data) == 2


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2021 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']
    data = get_formatted_data(test_data[3:4])
    assert data == ["23.03.2018 Открытие вклада\n['СКРЫТО']  -> Счет **2431\n48223.05 руб.\n"]