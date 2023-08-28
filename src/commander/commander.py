from abc import ABC, abstractmethod
from src.query.query import Query
from src.input_manager.input_manager import InputManager


class Commander(ABC):
    """Базовый класс обработчика команд от пользователя для настройки запроса"""
    @abstractmethod
    def __init__(self, input_manager: InputManager, query: Query):
        pass

    @abstractmethod
    def run(self):
        pass
