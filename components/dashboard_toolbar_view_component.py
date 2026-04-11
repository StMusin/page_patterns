import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    """
    Компонент панели инструментов на дашборде.
    Используется для проверки отображения заголовка 'Dashboard'.
    """
  
    def __init__(self, page: Page):
        """
        Инициализация компонента панели инструментов.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)

        # Элемент, отображающий заголовок панели инструментов
        self.title = Text(page, 'dashboard-toolbar-title-text', 'Dashboard')

    @allure.step("Check visible dashboard toolbar view")
    def check_visible(self):
        """
        Проверяет, что панель инструментов отображается корректно:
        - Заголовок панели виден
        - Заголовок содержит текст 'Dashboard'
        """
        # Проверка, что заголовок виден на экране
        self.title.check_visible()
        # Проверка, что заголовок содержит правильный текст
        self.title.check_have_text('Dashboard')