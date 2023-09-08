from src.vacansy import Vacancy


def put_to_dict(vacancy: Vacancy) -> dict:
    """
    Преобразует объект вакансии в словарь
    :param vacancy: объект вакансии
    :return: словарь с информацией по вакансии
    """
    info = {"position": vacancy.position, "min_salary": vacancy.min_salary,
            "max_salary": vacancy.max_salary, "requirements": vacancy.requirements, "url": vacancy.url
            }

    return info


def put_to_vacancy(info: dict) -> Vacancy:
    """
    Преобразует словарь с информацией по вакансии в объект вакансии
    :param info: словарь с информацией по вакансии
    :return: объект вакансии
    """
    vacancy = Vacancy(
        position=info["position"],
        min_salary=info["min_salary"],
        max_salary=info["max_salary"],
        requirements=info["requirements"],
        url=info["url"]
    )

    return vacancy
