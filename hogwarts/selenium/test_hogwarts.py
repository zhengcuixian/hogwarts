#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/29 0029 上午 11:40
# @Author  : zhengcx
# @File    : test_hogwarts.py
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class TestHogwarts:

    def setup_method(self):
        browser = os.getenv("browser", "").lower()
        if browser == "headless":
            self.driver = webdriver.PhantomJS()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            options = webdriver.ChromeOptions()
            #使用headless模式，无浏览器
            #options.add_argument("--headless")
            #options.add_argument("--disable-gpu")
            #options.add_argument("--window-size=1280,1696")

            #使用已经存在的Chrome进程
            # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
            #options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)
        #self.wait = WebDriverWait(self.driver, 10)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(1)
        # 显示等待
        # 尽量使用css的定位方法集，link有可能会导致解析元素的时候出现异常
        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        self.wait.until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # 使用css比link更好用
        # 隐式等待
        # self.driver.find_element(By.CSS_SELECTOR, 'topic-21848 .title > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def test_jinshuju(self):
        self.driver.get("https://testerhome.com/topics/21495")
        submit = (By.CSS_SELECTOR, ".published-form_submit")

        self.driver.switch_to.frame(0)
        self.wait(10, expected_conditions.element_to_be_clickable(submit))
        self.driver.find_element(By.CSS_SELECTOR, ".published-form_submit").click()

    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/21805")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "第六届中国互联网测试开发大会").click()
        print(self.driver.window_handles)
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        element = (By.LINK_TEXT, '演讲申请')
        self.wait(10, expected_conditions.visibility_of_element_located(element))
        self.driver.find_element(*element).click()

    def test_js(self):
        for code in [
            "return document.title",
            'return document.querySelector(".active").className',
            'return JSON.stringify(performance.timing)'
        ]:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        self.driver.quit()
