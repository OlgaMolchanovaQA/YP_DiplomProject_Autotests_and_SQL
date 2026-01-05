import configuration
import requests
import data

#Создание заказа
def create_order(order_body):
    # Формируем полный URL
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER_ENDPOINT
    # Отправляем POST-запрос
    response = requests.post(url=url,
        json=data.order_body)  # Отправляем тело заказа в JSON-формате
    return response  # Возвращаем ответ сервера

#Получение заказа по треку
def get_order_by_track(track_number):
    # Формируем URL через конкатенацию
    url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_ENDPOINT + track_number
    # Отправляем GET-запрос
    response = requests.get(url=url)
    return response  # Возвращаем ответ сервера

def get_track_number(response):
    return str(response.json()['track'])