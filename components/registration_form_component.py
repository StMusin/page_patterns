import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    """
    Компонент формы регистрации. Содержит поля: Email, Username, Password.
    Предоставляет методы для заполнения и проверки отображения формы.
    """
    
    def __init__(self, page: Page):
        """
        Инициализирует элемент формы регистрации.

        :param page: Экземпляр Playwright Page
        """
      
        super().__init__(page)

        # Поле ввода email
        self.email_input = Input(page, "registration-form-email-input", "Email")
        # Поле ввода username
        self.username_input = Input(page, "registration-form-username-input", "Username")
        # Поле ввода password
        self.password_input = Input(page, "registration-form-password-input", "Password")

    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str):
        """
        Заполняет форму регистрации заданными значениями.

        :param email: Email пользователя
        :param username: Имя пользователя
        :param password: Пароль
        """
        # Заполнение email и проверка, что значение введено корректно
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

         # Заполнение username и проверка, что значение введено корректно
        self.username_input.fill(username)
        self.username_input.check_have_value(username)

        # Заполнение password и проверка, что значение введено корректно
        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step("Check that registration form is visible")
    def check_visible(self, email: str, username: str, password: str):
        """
        Проверяет, что форма регистрации отображается корректно и содержит указанные значения.

        :param email: Ожидаемое значение email
        :param username: Ожидаемое значение username
        :param password: Ожидаемое значение пароля
        """
        # Проверка email-поля
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        # Проверка username-поля
        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        # Проверка password-поля
        self.password_input.check_visible()
        self.password_input.check_have_value(password)



from dataclasses import dataclass

# @dataclass
# class RegistrationFormFillParams:
#     email: str
#     username: str
#     password: str

# def fill(self, params: RegistrationFormFillParams):
#     self.email_input.fill(params.email)
#     self.username_input.fill(params.username)
#     self.password_input.fill(params.password)
