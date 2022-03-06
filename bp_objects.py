#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bp_selectors


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.locators = bp_selectors.BaseLocators()
        self.wait = WebDriverWait(self.driver, 60)

    def open_page(self, url):
        self.driver.get(url)

    def wait_element(self, *locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            print("\nELEMENT locatedWAIT %s" % str(locator))
            return True
        except Exception as ex:
            print("\nEXEPTION locatedWAIT: %s" % ex)
            raise Exception("locator %s dont found because it is very slow loading, or except: %s" % (str(locator), ex))

    def search_element(self, *locator):
        element_wait = self.wait_element(*locator)
        if element_wait:
            element = self.driver.find_element(*locator)
            return element

    def search_elements(self, *locator):
        element_wait = self.wait_element(*locator)
        if element_wait:
            elements = self.driver.find_elements(*locator)
            return elements

    def click_element(self, element, *locator):
        element_wait = self.wait_element(*locator)
        if element_wait:
            element.click()

    def clear_element(self, *locator):
        element = self.search_element(*locator)
        if element.is_displayed():
            element.clear()

    def find_and_click(self, *locator):
        element = self.search_element(*locator)
        self.click_element(element, *locator)

    def return_text_ele(self, *locator):
        element = self.search_element(*locator)
        return element.text

    def return_attrs_ele(self, attr, *locator):
        element = self.search_element(*locator)
        return element.get_attribute(attr)

    def fill_element(self, word, *locator):
        element = self.search_element(*locator)
        element.send_keys(word)
