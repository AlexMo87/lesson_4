# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver,10)
# driver.get("https://practice.automationtesting.in/")
# Myacc = driver.find_element_by_id("menu-item-50")
# Myacc.click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("qwerty@mail.com")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Qaz123/*-!@#mjyGVBJIs5423")
# reg = driver.find_element_by_css_selector('[class="woocommerce-Button button"],[name="register"]')
# reg.click()


import time
import click
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver # импортируем webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver,10)
# driver.get("https://practice.automationtesting.in/")
# Myacc = driver.find_element_by_id("menu-item-50")
# Myacc.click()
# login = driver.find_element_by_id("username")
# login.send_keys("qwerty@mail.com")
# passw = driver.find_element_by_id("password")
# passw.send_keys("Qaz123/*-!@#mjyGVBJIs5423")
# Log = driver.find_element_by_css_selector("login,[value='Login']")
# Log.click()
# ogout = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/my-account/customer-logout/']")
# Logout_get_text = Logout.text
# assert Logout_get_text == "Logout"