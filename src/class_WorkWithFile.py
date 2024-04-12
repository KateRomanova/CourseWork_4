from abc import ABC, abstractmethod
import json


class WorkWithFile(ABC):
    """Абстрактный класс для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления
    информации о вакансиях."""
    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_vacancy(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class SaveJson(WorkWithFile):
    """Класс для сохранения информации о вакансиях в json file"""
    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancy_data):
        """Добавляет вакансии в файл json."""
        with open(self.file_name, 'a') as file:
            json.dump(vacancy_data, file)
            file.write('\n')

    def get_vacancy(self):
        """Получает данные по вакансиям из файла."""
        with open(self.file_name, 'r') as file:
            vacancies = json.load(file)
            return vacancies

    def del_vacancy(self):
        """Удаляет информацию о вакансиях."""
        pass
