import allure
import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:
    @allure.title("Successful registration")
    def test_successful_registration(
            self,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        # 1. Переход на страницу регистрации
        registration_page.visit(AppRoute.REGISTRATION)
        
        # 2. Проверка, что форма регистрации отображается
        registration_page.registration_form.check_visible(email="", username="", password="")
        
        # 3. Заполнение формы регистрации
        registration_page.registration_form.fill(
            email="user@example.com",
            username="Playwright",
            password="qwerty"
        )

        # 4. Клик по кнопке регистрации
        registration_page.click_registration_button()

        # 5. Проверка отображения элементов на Dashboard
        dashboard_page.navbar.check_visible("Playwright")  # Navbar с именем пользователя
        dashboard_page.dashboard_toolbar_view.check_visible()  # Toolbar на дашборде
        dashboard_page.check_visible_scores_chart()  # График оценок
        dashboard_page.check_visible_courses_chart()  # График курсов
        dashboard_page.check_visible_students_chart()  # График студентов
        dashboard_page.check_visible_activities_chart()  # График активности