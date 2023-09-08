from abc import ABC, abstractmethod
from src.query.query import Query
from src.api.base_api import Api


class InputManager(ABC):
    """Работа с входными данными от пользователя"""
    @abstractmethod
    def get_base_command(self):
        """Читает и возвращает базовую команду"""
        pass


    @abstractmethod
    def get_vacancies_by_keywords(self, query: Query) -> Query:
        """
        Выбор ключевых слов для поиска
        :param query: Настриваемый запрос
        :return: запрос с настроенным полем keywords
        """
        pass

    @abstractmethod
    def choose_sort_type(self, query: Query) -> Query:
        """
        Включение/отключение сортировки
        :param query: Настриваемый запрос
        :return: запрос с настроенным полем need_sort
        """
        pass

    @abstractmethod
    def choose_platforms(self, apis_names: dict[str:Api], query: Query) -> Query:
        """
        Выбор платформ для поиска
        :param apis_names: Соответствие строковых названий имеющимся объектам API
        :param query: Настриваемый запрос
        :return: запрос с настроенным полем api_list
        """
        pass
