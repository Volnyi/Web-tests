#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from data import *
import bp_actions
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", type=str, help="Выбор браузера")
    parser.addoption("--project", action="store", default="1c_prod", type=str, help="Выбор класса для проекта")


def pytest_configure(config):
    config.addinivalue_line("markers", "for_all")


@pytest.fixture(scope='class')
def get_driver(request):
    browser = request.config.getoption("--browser")
    driver = None
    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path=driver_firefox)
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path=driver_chrome)

    def driver_quit():
        driver.quit()
    request.addfinalizer(driver_quit)

    return driver


@pytest.fixture(scope='class')
def driver_and_project(request, get_driver):
    project = request.config.getoption("--project")
    test_page = None
    test_ulrs = None
    if project == '1c_prod':
        test_page = bp_actions.ProdactionSite(get_driver)
        test_ulrs = urls['1c_prod']
    return test_page, test_ulrs
