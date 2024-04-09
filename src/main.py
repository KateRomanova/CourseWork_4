import requests

# url_get = "https://api.hh.ru/vacancies"
# response = requests.get(url_get)
# print(response)
# print(response.text)
# print(response.json())


class Parser:
    """Абстрактный класс для работы с API сервиса с вакансиями."""
    def __init__(self, file_worker):
        pass

    def load_vacancies(self, keyword):
        pass


class HeadHunterApi(Parser):
    """
    Класс для работы с API HeadHunter, умеет подключаться к API и получать вакансии.
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
            print(response.json())


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterApi('разработчик')

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.load_vacancies("Python")
