class Vacancy:
    """Класс-представление вакансии"""
    def __init__(self, position: str, min_salary: int, max_salary: int, requirements: str, url: str):
        self.__position = position
        self.__min_salary = min_salary
        self.__max_salary = max_salary
        self.__requirements = requirements
        self.__url = url

    @property
    def position(self):
        return self.__position

    @property
    def min_salary(self):
        return self.__min_salary

    @property
    def max_salary(self):
        return self.__max_salary

    @property
    def requirements(self):
        return self.__requirements

    @property
    def url(self):
        return self.__url
