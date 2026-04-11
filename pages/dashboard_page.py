from playwright.sync_api import Page

from components.chart_view_component import ChartViewComponent
from components.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navbar_component import NavbarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    """
    Страница панели управления (Dashboard Page).

    Включает компоненты:
    - Панель навигации (Navbar)
    - Графики по оценкам, курсам, студентам и активностям
    - Панель инструментов для управления

    Наследуется от BasePage.
    """
  
    def __init__(self, page: Page):
        """
        Инициализация страницы панели управления.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)

        # Компоненты страницы
        self.navbar = NavbarComponent(page)  # Панель навигации
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")  # График по оценкам
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")  # График по курсам
        self.students_chart_view = ChartViewComponent(page, "students", "bar")  # График по студентам
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")  # График по активностям
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)  # Панель инструментов

    def check_visible_students_chart(self):
        """
        Проверка видимости графика по студентам.

        :raises AssertionError: Если график не виден или не имеет правильного текста
        """
        self.students_chart_view.check_visible('Students')

    def check_visible_courses_chart(self):
        """
        Проверка видимости графика по курсам.

        :raises AssertionError: Если график не виден или не имеет правильного текста
        """
        self.courses_chart_view.check_visible('Courses')

    def check_visible_activities_chart(self):
        """
        Проверка видимости графика по активностям.

        :raises AssertionError: Если график не виден или не имеет правильного текста
        """
        self.activities_chart_view.check_visible('Activities')

    def check_visible_scores_chart(self):
        """
        Проверка видимости графика по оценкам.

        :raises AssertionError: Если график не виден или не имеет правильного текста
        """
        self.scores_chart_view.check_visible('Scores')