import sender_stand_requests # Импорт модуля с API-функциями для работы с заказами
import data # Импорт модуля с тестовыми данными (нужен для передачи order_data)

# Денис Барановский, 36-я  когорта - Финальный проект. Инженер по тестированию плюс

# Основной тестовый сценарий: создание заказа и проверка его получения
def test_create_and_get_order():
    
    # Шаг 1: Выполнить запрос на создание заказа
    response_create = sender_stand_requests.post_create_order(data.order_data)
    # Проверяем, что заказ успешно создан (код ответа 201 - Created)
    assert response_create.status_code == 201
    
    # Шаг 2: Сохранить номер трека заказа
    track = response_create.json()["track"]
    
    # Шаг 3: Выполнить запрос на получение заказа по треку заказа
    response_get = sender_stand_requests.get_order_by_track(track)
  
    # Шаг 4: Проверить, что код ответа равен 200 (OK)
    assert response_get.status_code == 200

