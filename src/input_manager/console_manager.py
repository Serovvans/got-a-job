from src.input_manager.base_class import InputManager
from src.query.query import Query
from src.api.base_api import Api


class ConsoleInputManager(InputManager):
    """Менеджер ввода данных из консоли"""
    def get_vacancies_by_keywords(self, query: Query) -> Query:
        """
        Выбор ключевых слов для поиска
        :param query: Настриваемый запрос
        :return: запрос с настроенным полем keywords
        """
        keywords: list[str] = list(input().split())
        query.keywords = keywords
        return query

    def choose_sort_type(self, query: Query) -> Query:
        """
        Включение/отключение сортировки
        :param query: Настриваемый запрос
        :return: запрос с настроенным полем need_sort
        """
        user_response: str = input("Нужно сортировать[yes/no]:").lower()
        query.need_sort = True if user_response == "yes" else False
        return query

    def choose_platforms(self, apis_names: dict[str:Api], query: Query) -> Query:
        """
        Выбор платформ для поиска
        :param apis_names: Соответствие строковых названий имеющимся объектам API
        :param query: Настриваемый запрос
        :return: запрос с настроенным полем api_list
        """
        user_response: str = input("Введите название сервиса или stop(для выхода):")
        while user_response != "stop":
            try:
                query.api_list.append(apis_names[user_response])
            except KeyError:
                print("Несуществующий сервис")
            finally:
                user_response = input("Введите название сервиса или stop(для выхода):")

        return query
