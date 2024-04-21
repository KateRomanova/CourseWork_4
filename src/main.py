from src.class_HeadHunterAPI import HeadHunterApi
from src.class_VacanciesHH import VacanciesHH
from src.class_WorkWithFile import SaveJson


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ").lower()
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh = HeadHunterApi()

    # Подключаемся к API и получаем вакансии по ключевому слову
    hh_vacancies = hh.load_vacancies(search_query)

    file_worker = SaveJson('data.json')  # название файла, куда будут сохраняться вакансии
    file_worker.add_vacancy(hh_vacancies)

    vacancies = [
        VacanciesHH(
            name=vacancy['name'],
            link=vacancy['url'],
            salary_from=vacancy['salary'].get('from') if vacancy['salary'] else "не указана",
            salary_to=vacancy['salary'].get('to') if vacancy['salary'] else '',
            currency=vacancy['salary'].get('currency') if vacancy['salary'] else '',
            description=vacancy['snippet']['responsibility'],
            requirements=vacancy['snippet']['requirement'])
        for vacancy in file_worker.get_vacancy()['items']]

    # Фильтруем вакансии по ключевым словам

    filtered_vacancies = set()

    for item in filter_words:
        for vacancy in vacancies:
            if vacancy.description and (item in vacancy.name or item in vacancy.description):
                filtered_vacancies.add(vacancy)

    # Фильтруем вакансии по диапазону зарплат

    salary_list = salary_range.split()
    salary_from_wish = int(salary_list[0])
    salary_to_wish = int(salary_list[2])
    ranged_vacancies = []

    for vacancy in filtered_vacancies:
        if (not vacancy.salary_from or not vacancy.salary_to or vacancy.salary_from <= salary_from_wish
                <= vacancy.salary_to and vacancy.salary_from <= salary_to_wish <= vacancy.salary_to):
            ranged_vacancies.append(vacancy)

    top_ranged_vacancies = ranged_vacancies[:top_n]
    print(top_ranged_vacancies)


if __name__ == "__main__":
    user_interaction()
