import re

from playwright.sync_api import Page

from components.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    """
    Страница регистрации (Registration Page).

    Включает элементы:
    - Форма регистрации
    - Кнопка для перехода на страницу входа
    - Кнопка для отправки формы регистрации

    Наследуется от BasePage.
    """
  
    def __init__(self, page: Page):
        """
        Инициализация страницы регистрации.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)

        # Компоненты страницы
        self.registration_form = RegistrationFormComponent(page)  # Форма регистрации

        # Элементы страницы
        self.login_link = Link(page, "registration-page-login-link", "Login")  # Ссылка на страницу входа
        self.registration_button = Button(page, "registration-page-registration-button", "Registration")  # Кнопка отправки формы

    def click_registration_button(self):
        """
        Клик на кнопку "Зарегистрироваться" и проверка перехода на страницу панели управления.

        :raises AssertionError: Если URL не соответствует ожидаемому
        """
        # Нажатие на кнопку регистрации
        self.registration_button.click()
        # Проверка, что мы перенаправлены на страницу панели управления
        self.check_current_url(re.compile(".*/#/dashboard"))