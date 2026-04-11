import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    """
    Компонент верхнего меню (navbar), где отображаются:
    - Название приложения
    - Приветствие пользователя
    """
  
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок с названием приложения
        self.app_title = Text(page, 'navigation-navbar-app-title-text', 'App title')
        # Заголовок приветствия
        self.welcome_title = Text(page, 'navigation-navbar-welcome-title-text', 'Welcome title')

    @allure.step("Check visible navbar")
    def check_visible(self, username: str):
        """
        Проверяет, что navbar отображается корректно:
        - Название приложения видно и соответствует 'UI Course'
        - Приветствие содержит имя пользователя

        :param username: Имя пользователя, которое ожидается в приветствии
        """
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')