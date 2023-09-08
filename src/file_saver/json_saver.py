import json
import os

from src.file_saver.file_saver import FileSaver
from src.vacansy import Vacancy
from src.file_saver.utils import put_to_dict, put_to_vacancy


class JsonSaver(FileSaver):
    """Класс для сохранения вакансий в json файл"""
    def __init__(self, file_name="vacancies.json"):
        self.file_name = file_name
        self.path = os.path.join(".", "data", self.file_name)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([], f)

    def add_vacancy(self, vacancy: Vacancy) -> Vacancy:
        """
        Добавляет 1 вакансию в файл
        :param vacancy: вакансия для добавления
        :return: добавленная вакансия
        """
        with open(self.path, "r", encoding="utf-8") as f:
            vacancies = json.load(f)

        vacancies.append(put_to_dict(vacancy))
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f)
        return vacancy

    def get_vacancies(self) -> list[Vacancy]:
        """
        Загружает все вакансии из файла
        :return: все вакансии из файла
        """
        with open(self.path, "r", encoding="utf-8") as f:
            answer = json.load(f)
            answer = list(map(put_to_vacancy, answer))

        return answer

    def delete_vacancies(self) -> None:
        """
        Удаляет указанную вакансию из файла
        :return:
        """
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([], f)
