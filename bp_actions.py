#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bp_objects import Page
import bp_selectors


class MainPageActions(Page):
    def find_and_click_main_profile(self):
        self.find_and_click(*self.locators.MAIN_HEADER_PROFILE)

    def find_and_click_enter(self):
        self.find_and_click(*self.locators.MAIN_HEADER_ENTER)

    def find_and_click_close_coockies(self):
        self.find_and_click(*self.locators.MAIN_COOCKIE_CLOSE)

    def fill_login(self, user):
        self.fill_element(user, *self.locators.MAIN_AUTH_LOGIN)

    def fill_password(self, password):
        self.fill_element(password, *self.locators.MAIN_AUTH_PASS)

    def find_and_click_enter_in_profile(self):
        self.find_and_click(*self.locators.MAIN_ENTER)


class ProdactionSite(MainPageActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = bp_selectors.ProdactionLocators()
