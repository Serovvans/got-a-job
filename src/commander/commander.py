from abc import ABC, abstractmethod


class Commander(ABC):
    """Базовый класс обработчика команд от пользователя для настройки запроса"""
    @abstractmethod
    def run(self):
        pass
