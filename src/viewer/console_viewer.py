from src.viewer.viewer import Viewer
from src.vacansy import Vacancy


class ConsoleViewer(Viewer):
    def show_message(self, message: str) -> None:
        """
        Выводит сообщение для пользователя
        :param message: сообщение
        :return: None
        """
        print(message)

    def show_response(self, response: list[Vacancy]) -> None:
        """
        Выводит ответ приложения
        :param response: ответ приложения
        :return: None
        """
        for item in response:
            print(f"{item.position} - {item.url}\n{item.min_salary} руб. - {item.max_salary} руб.\n{item.requirements}")
            print()
