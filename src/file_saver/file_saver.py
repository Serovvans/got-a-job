from abc import ABC, abstractmethod


class FileSaver(ABC):
    """Класс для сохранения данных о вакансиях в файл"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
