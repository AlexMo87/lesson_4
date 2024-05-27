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
# driver.execute_script("window.scrollBy(0, 600);")
# Ruby = driver.find_element_by_css_selector('a[href="https://practice.automationtesting.in/product/selenium-ruby/"] > h3')
# Ruby.click()
# Revi = driver.find_element_by_css_selector('a[href="#tab-reviews"]')
# Revi.click()
# Star = driver.find_element_by_css_selector("a[class='star-5']")
# Star.click()
# Comment = driver.find_element_by_id("comment")
# Comment.send_keys("Nice book!")
# Name = driver.find_element_by_id("author")
# Name.send_keys("Alex Mo")
# Email = driver.find_element_by_id("email")
# Email.send_keys("qwerty@mail.com")
# Submit = driver.find_element_by_id("submit")
# Submit.click()