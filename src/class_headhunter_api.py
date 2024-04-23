import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HeadHunterApi(Parser):
    """
    Класс для работы с API HeadHunter.
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        # self.headers = {'User-Agent': 'HH-User-Agent'}
        # self.params = {'text': '', 'page': 0, 'per_page': 100}
        # self.vacancies = []
        # super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """Подключается к API и получает вакансии по ключевому слову"""
        params = {'text': keyword, 'page': 0, 'per_page': 100}
        response = requests.get(self.url, params=params).json()
        return response

        # self.params['text'] = keyword
        # while self.params.get('page') != 20:
        #     response = requests.get(self.url, headers=self.headers, params=self.params)
        #     vacancies = response.json()['items']
        #     self.vacancies.extend(vacancies)
        #     self.params['page'] += 1
        #     print(response.json())


if __name__ == '__main__':

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterApi()
    print(hh_api)

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies("разработчик Python")
    print(hh_vacancies)
