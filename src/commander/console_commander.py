from src.query.query import Query
from src.input_manager.input_manager import InputManager

from src.commander.commander import Commander


class ConsoleCommander(Commander):
    """Обработка команд из консоли"""
    def __init__(self, input_manager: InputManager):
        self.input_manager = input_manager
        self.query = Query()

    def run(self) -> Query:
        """Запуск цикла работы обработки команд"""
        command = self.input_manager.get_base_command()
        while command != "exit":
            if command == "keywords":
                self.input_manager.get_vacancies_by_keywords(self.query)
            elif command == "sort":
                self.input_manager.choose_sort_type(self.query)
            elif command == "platforms":
                self.input_manager.choose_platforms(dict(), self.query)

            command = self.input_manager.get_base_command()

        return self.query
