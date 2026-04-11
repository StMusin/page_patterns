import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):
    """
    Компонент графика (чарта), который может отображаться на дашборде или в аналитике.

    :param identifier: Базовый ID виджета (например, "students", "scores", "courses")
    :param chart_type: Тип графика (например, "bar", "line", "pie")
    """
  
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        # Элемент заголовка графика
        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        # Элемент изображения самого графика
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible chart view "{title}"')
    def check_visible(self, title: str):
        """
        Проверяет, что чарт отображается корректно:
        - Заголовок виден и содержит переданный текст
        - График (image) виден на странице

        :param title: Ожидаемый заголовок графика
        """
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()