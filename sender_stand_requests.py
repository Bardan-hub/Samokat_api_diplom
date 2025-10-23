import configuration # Импорт модуля конфигурации с базовыми настройками (URL, пути API)
import requests # Импорт библиотеки для выполнения HTTP-запросов
import data # Импорт модуля с тестовыми данными (нужен для получения headers)

# Функция для создания заказа
def post_create_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.API_ORDERS_PATH,
        json=body,
        headers=data.headers
    )


# Функция для получения заказа по трек номеру
def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.API_TRACK_PATH,
        params={"t": track}
    )