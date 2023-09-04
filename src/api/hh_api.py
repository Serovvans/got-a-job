import requests

from src.api.base_api import Api
from src.query.query import Query
from src.vacancy.vacansy import Vacancy


class HHApi(Api):
    """Реализация работы с API сайта hh.ru"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def __get_api_response(self, query: Query) -> list[dict]:
        response = requests.get(self.url, {"text": " ".join(query.key_words),
                                           "only_with_salary": True}).json()["items"]

        return response

    def __get_all_vacancies_with_ru_salary(self, vacancies: list[dict]) -> list[Vacancy]:
        answer = []
        for res in vacancies:
            if res["salary"]["currency"] == "RUR":
                answer.append(self.put_to_vacancy(res))

        return answer

    @staticmethod
    def __sort_response(vacancies: list[Vacancy]) -> list[Vacancy]:
        return sorted(vacancies, key=lambda x: x.min_salary if x.min_salary is not None else 0,
                      reverse=True)

    @staticmethod
    def put_to_vacancy(item: dict) -> Vacancy:
        min_salary = int(item["salary"]["from"]) if item["salary"]["from"] is not None else None
        max_salary = int(item["salary"]["to"]) if item["salary"]["to"] is not None else None
        new_vacancy = Vacancy(position=item.get("name"),
                              min_salary=min_salary,
                              max_salary=max_salary,
                              requirements=item.get("snippet").get("requirement"),
                              url=item.get("url"))

        return new_vacancy

    def get_vacancies(self, query: Query) -> list[Vacancy]:
        response = self.__get_api_response(query)

        answer = self.__get_all_vacancies_with_ru_salary(response)
        if query.need_sort:
            answer = self.__sort_response(answer)

        return answer
