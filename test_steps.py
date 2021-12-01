import pytest
from time import sleep
from data import *
# Для запуска перейти в директорию с тестами и ввести в командную строку: pytest -m for_all test_steps.py --browser firefox --project 1c_prod


class TestAuth:
    @pytest.mark.for_all
    def test_login(self, driver_and_project):
        """Корректная авторизация"""
        driver_and_project[0].open_page(driver_and_project[1])
        sleep(3)
        driver_and_project[0].find_and_click_close_coockies()
        driver_and_project[0].find_and_click_main_profile()
        driver_and_project[0].find_and_click_enter()
        driver_and_project[0].fill_login(user_login['correct_login'])
        driver_and_project[0].fill_password(user_password['correct_password'])
        driver_and_project[0].find_and_click_enter_in_profile()
        sleep(3)
        assert driver_and_project[0].driver.current_url == driver_and_project[1] + 'ru/'
