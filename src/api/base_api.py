from abc import ABC, abstractmethod


class Api(ABC):
    """Абстрактный класс работы с api сайтов поиска вакансий"""
    @abstractmethod
    def get_vacancies(self, query):
        pass

    @staticmethod
    @abstractmethod
    def put_to_vacancy(item: dict):
        pass
