#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/29 0029 上午 11:40
# @Author  : zhengcx
# @File    : test_search.py
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestsearch():
    def setup_method(self, method):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testsearch(self):
        self.driver.get("https://testerhome.com/")
        self.driver.set_window_size(1382, 744)
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("appuim")
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)