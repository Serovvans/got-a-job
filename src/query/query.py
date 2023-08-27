from src.api.base_api import Api


class Query:
    """Объект запроса с настриваемыми параметрами"""
    def __init__(self):
        """Задаёт значение полей по умолчанию"""
        self.key_words: list[str] = []
        self.api_list: list[Api] = []
        self.need_sort: bool = False
        self.file_managers: list = []

    def __get_api_response(self):
        """Отправляет запрос к api"""
        pass

    def __save_response(self, response):
        """Сохраняет запрос в файл-менеджер"""
        pass

    def __call__(self):
        """Вызов объекта отправляет запрос к api и сохраняет ответ"""
        pass
