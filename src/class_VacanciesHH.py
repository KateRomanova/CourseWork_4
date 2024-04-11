class VacanciesHH:
    """Класс для работы с вакансиями."""
    def __init__(self, name, link, salary_from, salary_to, currency, description, requirements):
        self.name = name
        self.link = link
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.requirements = requirements

    def __repr__(self):
        """Строковое представление объекта класса VacanciesHH"""
        return f"""
        Название вакансии: {self.name}
        Описание вакансии: {self.description}
        Зарплата: {self.salary_from} - {self.salary_to} {self.currency}
        Требования: {self.requirements}
        Ссылка на вакансию: {self.link}
        """

    def __gt__(self, other):
        """Сравнивает вакансии между собой."""
        return self.salary_from > other.salary_from

    def validate_data(self):
        """Валидирует данные, которыми инициализируются атрибуты"""
        if not self.salary_from and not self.salary_to:
            self.salary_from = "Зарплата не указана"
