from src.api.base_api import Api
from src.vacansy import Vacancy
from src.file_saver.json_saver import JsonSaver


class Query:
    """Объект запроса с настриваемыми параметрами"""
    def __init__(self, file_manager=JsonSaver()):
        """Задаёт значение полей по умолчанию"""
        self.keywords: list[str] = []
        self.api_list: list[Api] = []
        self.need_sort: bool = False
        self.file_saver = file_manager

    def __get_api_response(self) -> list[Vacancy]:
        """Отправляет запрос к api"""
        response = []
        for api in self.api_list:
            response += api.get_vacancies(self)

        return response

    def __save_response(self, response: list[Vacancy]) -> None:
        """Сохраняет запрос в файл-менеджер"""
        for item in response:
            self.file_saver.add_vacancy(item)

    def __call__(self) -> None:
        """Вызов объекта отправляет запрос к api и сохраняет ответ"""
        response = self.__get_api_response()
        self.__save_response(response)
