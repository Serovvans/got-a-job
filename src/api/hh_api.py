import requests

from src.api.base_api import Api
from src.query.query import Query
from src.vacancy.vacansy import Vacancy


class HHApi(Api):
    """Реализация работы с API сайта hh.ru"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.__params = {
            "only_with_salary": True
        }

    def __get_response(self, query: Query) -> list[dict]:
        """
        Парсинг вакансий по запросу пользователя
        :param query: запрос
        :return: список с информацией о вакансиях
        """
        self.__params["text"] = " ".join(query.key_words)
        response = requests.get(self.url, self.__params).json()["items"]

        return response

    @staticmethod
    def __get_all_vacancies_with_ru_salary(vacancies: list[dict]) -> list[dict]:
        """
        Выбирает вакансии с зарплатой в рублях
        :param vacancies: список с информаций о вакансиях
        :return: вакансии с зарплатой в рублях
        """
        answer = []
        for res in vacancies:
            if res["salary"]["currency"] == "RUR":
                answer.append(res)

        return answer

    @staticmethod
    def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
        """
        Сортирует вакансии по зарплате в порядке убывания
        :param vacancies: список вакансий
        :return: отсортированный список вакансий
        """
        return sorted(vacancies, key=lambda x: x.min_salary if x.min_salary is not None else 0,
                      reverse=True)

    @staticmethod
    def put_to_vacancy(item: dict) -> Vacancy:
        """
        Преобразует словарь в объект вакансии
        :param item: словарь с информацией о вакансии
        :return: объект вакансии
        """
        min_salary = int(item["salary"]["from"]) if item["salary"]["from"] is not None else None
        max_salary = int(item["salary"]["to"]) if item["salary"]["to"] is not None else None
        new_vacancy = Vacancy(position=item.get("name"),
                              min_salary=min_salary,
                              max_salary=max_salary,
                              requirements=item.get("snippet").get("requirement"),
                              url=item.get("url"))

        return new_vacancy

    def get_vacancies(self, query: Query) -> list[Vacancy]:
        """
        Ответ на запрос пользователя
        :param query: запрос
        :return: ответ
        """
        response = self.__get_response(query)

        answer = self.__get_all_vacancies_with_ru_salary(response)
        answer = list(map(self.put_to_vacancy, answer))
        if query.need_sort:
            answer = self.sort_vacancies(answer)

        return answer
