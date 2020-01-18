#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 0001 下午 10:08
# @Author  : zhengcx
# @File    : test_study3.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest


memberInfo = [
    ('testerhome001', 'tester001', '00001',
     '13688889999', '021-7859632', '13688889999@163.com', '00001员工地址',
     '系统架构师', '项目经理')]

class TestaddMember():

    def setup_method(self):

        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.vars = {}

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.parametrize('username, nickname, accountNum,'
                             'mobilphone,phone, email, addr,'
                             ' Position,sendinvite', memberInfo )
    def test_add_member(self, username, accountNum, nickname,
                        mobilphone, phone, email, addr,
                        Position, sendinvite):
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()  # 添加成员
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)  # 姓名
        # self.clear_send_keys(By.CSS_SELECTOR, '#username', "testerhome001")  # 姓名
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_english_name').send_keys(nickname)  # 别名
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(accountNum)  # 帐号
        self.driver.find_element(By.CSS_SELECTOR, 'label:nth-child(2) input').click()  # 性别单选框
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(mobilphone)  # 手机
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_telephone').send_keys(phone)  # 座机
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_mail').send_keys(email)  # 邮箱
        self.driver.find_element(By.CSS_SELECTOR, '#memberEdit_address').send_keys(addr)  # 地址
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_title').send_keys(Position)  # 职务
        self.driver.find_element(By.XPATH, '//div/label[2]/input[@name="identity_stat"]').click()  # 身份
        self.driver.find_element(By.XPATH, '//div/label[2]/input[@name="extern_position_set"]').click()  # 对外职务-选择自定义
        self.driver.find_element(By.CSS_SELECTOR, '[name = "extern_position"]').send_keys(sendinvite)  # 对外职务-自定义输入
        self.driver.find_element(By.CSS_SELECTOR, '[name="sendInvite"]').click()  # 通过邮件或短信发送企业邀请
        self.driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()
