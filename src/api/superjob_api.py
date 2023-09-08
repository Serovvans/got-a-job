import requests
import os

from src.api.base_api import Api
from src.query.query import Query
from src.vacancy.vacansy import Vacancy
from src.errors.parsing_error import ParsingError


class SuperJobApi(Api):
    """Реализация работы с API сайта superjob.ru"""
    def __init__(self):
        self.__key = os.getenv("SUPERJOB_KEY").strip()
        self.__url = f'https://api.superjob.ru/2.0/vacancies'
        self.__params = {
            "archive": False
        }
        self.__headers = {
            "X-Api-App-Id": self.__key
        }

    @staticmethod
    def put_to_vacancy(item: dict):
        """
        Преобразует словарь в объект вакансии
        :param item: словарь с информацией о вакансии
        :return: объект вакансии
        """
        vacancy = Vacancy(position=item["profession"],
                          min_salary=item["payment_from"],
                          max_salary=item["payment_to"],
                          requirements=item["candidat"],
                          url=item["link"])

        return vacancy

    def __get_response(self, query: Query) -> list[dict]:
        """
        Парсит вакансии по 1 ключевому слову
        :param query: запрос пользователя
        :return: список словарей с информаций о вакансиях
        """
        if query.key_words:
            self.__params["keyword"] = query.key_words[0]

        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий с сайта superjob! Статус {response.status_code}")

        return response.json()["objects"]

    @staticmethod
    def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
        """
        Сортирует вакансии в порядке убывания минимальных зарплат
        :param vacancies: список вакансий
        :return: отсортированный список вакансий
        """
        answer = sorted(vacancies, key=lambda x: x.min_salary, reverse=True)
        return answer

    def get_vacancies(self, query: Query) -> list[Vacancy]:
        """
        Получение списка вакансий по ключевому слову
        :param query: Запрос пользователя
        :return: ответ на запрос с сайта SuperJob
        """
        response = self.__get_response(query)

        answer = list(map(self.put_to_vacancy, response))
        if query.need_sort:
            answer = self.sort_vacancies(answer)

        return answer
