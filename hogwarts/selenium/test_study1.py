# Generated by Selenium IDE
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

class TestStudy1():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_study1(self):
    self.driver.get("https://testerhome.com/")
    self.driver.set_window_size(1173, 694)
    self.driver.find_element(By.LINK_TEXT, "社团").click()
    self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".topic-21848 .title > a").click()
  
