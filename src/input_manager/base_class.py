from abc import ABC, abstractmethod


class InputManager(ABC):
    """Работа с входными данными от пользователя"""
    @abstractmethod
    def get_vacancies_by_keywords(self):
        pass

    @abstractmethod
    def choose_sort_type(self):
        pass

    @abstractmethod
    def choose_platforms(self):
        pass
