from selenium.webdriver.common.by import By


class BaseLocators:
    """Class with universal locators"""
    MAIN_HEADER_PROFILE = (By.XPATH, '//*[@id="login-menu"]')
    MAIN_HEADER_ENTER = (By.XPATH, '//*[@id="navbarText"]/ul[2]/li[2]/div/div[1]/a')
    MAIN_COOCKIE_CLOSE = (By.XPATH, '//*[@id="alert-portal_use_cookie"]/div/div/div/a[1]')
    MAIN_AUTH_LOGIN = (By.XPATH, '//*[@id="popup_login_email"]')
    MAIN_AUTH_PASS = (By.XPATH, '//*[@id="popup_login_password"]')
    MAIN_ENTER = (By.XPATH, '//*[@id="login-popup"]/div/div/div/form/div[4]/div[2]/div/button')


class ProdactionLocators(BaseLocators):
    """Class with prod locators"""
    pass
