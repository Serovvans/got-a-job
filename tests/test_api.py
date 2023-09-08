from src.api.hh_api import HHApi


def test_hh_api(query):
    api = HHApi()

    response = api.get_vacancies(query)
    assert len(response) > 0
