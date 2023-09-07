from src.api.hh_api import HHApi
from src.api.superjob_api import SuperJobApi
from src.query.query import Query


if __name__ == "__main__":
    query = Query()
    query.key_words = ["python", "ML"]
    query.need_sort = True

    api = SuperJobApi()
    for item in api.get_vacancies(query):
        print(item.min_salary)
