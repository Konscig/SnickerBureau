from config import app


@app.get("/")
def hello_world():
    """Пример работы рутов

    Returns:
        str: вывод строки на "/"
    """
    return str("hello_world")
