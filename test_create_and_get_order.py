# Ольга Молчанова, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_create_and_get_order():
    # Шаг 1: Создание заказа
    create_response = sender_stand_request.create_order(data.order_body)

    # Проверяем статус создания заказа
    assert create_response.status_code == 201, "Ошибка при создании заказа: неверный статус ответа"

     # Проверяем создание заказа
    if create_response.status_code == 201:
        print("Заказ успешно создан")
    else:
        print(f"Ошибка создания заказа. Статус: {create_response.status_code}")
        return

    # Шаг 2: Получаем трек-номер
    track_number = sender_stand_request.get_track_number(create_response)
    assert track_number is not None, "Трек-номер не был получен из ответа"

    if track_number:
        print(f"Трек-номер: {track_number}")
    else:
        print("Не удалось получить трек-номер")
        return

    # Шаг 3: Получение заказа по треку
    get_response = sender_stand_request.get_order_by_track(track_number)

    # Шаг 4: Проверяем статус ответа
    assert get_response.status_code == 200, "При получении заказа по треку получен неверный статус ответа"

    if get_response.status_code == 200:
        print("Заказ успешно получен")
        print("Информация о заказе:")
        print(get_response.json())
    else:
        print(f"Ошибка получения заказа. Статус: {get_response.status_code}")
