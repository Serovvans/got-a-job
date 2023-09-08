from src.query.query import Query
from src.input_manager.input_manager import InputManager
from src.api.list_apis import apis
from src.viewer.viewer import Viewer

from src.commander.commander import Commander


class ConsoleCommander(Commander):
    """Обработка команд из консоли"""
    def __init__(self, input_manager: InputManager, viewer: Viewer):
        self.input_manager = input_manager
        self.query = Query()
        self.viewer = viewer

    def run(self) -> None:
        """Запуск цикла работы обработки команд"""
        command = self.input_manager.get_base_command()
        while command != "exit":
            if command == "keywords":
                self.input_manager.get_vacancies_by_keywords(self.query)
            elif command == "sort":
                self.input_manager.choose_sort_type(self.query)
            elif command == "platforms":
                self.input_manager.choose_platforms(apis, self.query)

            command = self.input_manager.get_base_command()

        self.query()
        self.viewer.show_response(self.query.file_saver.get_vacancies())
