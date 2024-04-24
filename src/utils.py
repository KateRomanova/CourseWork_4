def filter_by_keyword(vacancies, filter_words):
    """ Фильтрует вакансии по ключевым словам"""

    filtered_vacancies = set()

    for item in filter_words:
        for vacancy in vacancies:
            if vacancy.description and (item in vacancy.name or item in vacancy.description):
                filtered_vacancies.add(vacancy)
    return filtered_vacancies


def filter_by_salary(filtered_vacancies, salary_range):
    """Фильтрует вакансии по диапазону зарплат"""

    salary_list = salary_range.split()
    salary_from_wish = int(salary_list[0])
    salary_to_wish = int(salary_list[2])
    ranged_vacancies = []

    for vacancy in filtered_vacancies:
        if vacancy.salary_from >= salary_from_wish and vacancy.salary_from <= salary_to_wish:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies
