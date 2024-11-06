import websocket

def handle_open(connection):
    print("Подключение к WebSocket серверу установлено")


def handle_message(connection, data):
    print("Получены данные:", data)
    # Обработка полученных данных и обновление графика


def handle_close(connection):
    print("Соединение с WebSocket сервером закрыто")


def handle_error(connection, err):
    print("Ошибка WebSocket соединения:", err)


if __name__ == "__main__":
    ws_connection = websocket.WebSocketApp(
        "ws://localhost:4000",
        on_open=handle_open,
        on_message=handle_message,
        on_close=handle_close,
        on_error=handle_error
    )

    try:
        ws_connection.run_forever()
    except KeyboardInterrupt:
        print("Соединение прервано вручную")
