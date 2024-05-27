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
# login = driver.find_element_by_id("username")
# login.send_keys("qwerty@mail.com")
# passw = driver.find_element_by_id("password")
# passw.send_keys("Qaz123/*-!@#mjyGVBJIs5423")
# Log = driver.find_element_by_css_selector("login,[value='Login']")
# Log.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# Book = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product/html5-forms/']")
# Book.click()
# # element = driver.find_element_by_css_selector(".summary.entry-summary > h1") #нашли элемент по составному селектору
# # element_get_text = element.text#получили текст элемента с помощью.text
# # assert element_get_text == "HTML5 Forms"#
# element = driver.find_element_by_css_selector(".summary.entry-summary > h1") #нашли элемент по составному селектору
# element_get_text = element.text#добавили новую переменную и получили текст элемента с помощью.text
# assert "HTML5 Forms"in element_get_text

# 2222222222222222222

# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver,2)
# driver.get("https://practice.automationtesting.in/")
# Myacc = driver.find_element_by_id("menu-item-50")
# Myacc.click()
# login = driver.find_element_by_id("username")
# login.send_keys("qwerty@mail.com")
# passw = driver.find_element_by_id("password")
# passw.send_keys("Qaz123/*-!@#mjyGVBJIs5423")
# Log = driver.find_element_by_css_selector("login,[value='Login']")
# Log.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# html = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product-category/html/']")
# html.click()
# items_count = driver.find_element_by_css_selector(".products.masonry-done") #нашли элемент по составному селектору
# if len(items_count) == 3:# после 1-го урока можем теперь создать небольшую конструкцию для проверки кол-ва товаров
#     print("Отображается 3 товара")#

# 2222222222

# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver,2)
# driver.get("https://practice.automationtesting.in/")
# Myacc = driver.find_element_by_id("menu-item-50")
# Myacc.click()
# login = driver.find_element_by_id("username")
# login.send_keys("qwerty@mail.com")
# passw = driver.find_element_by_id("password")
# passw.send_keys("Qaz123/*-!@#mjyGVBJIs5423")
# Log = driver.find_element_by_css_selector("login,[value='Login']")
# Log.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# HTML = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product-category/html/']")
# HTML.click()
# element = driver.find_element_by_css_selector(".cat-item.cat-item-19.current-cat > span") #нашли элемент по составному селектору
# element_get_text = element.text#добавили новую переменную и получили текст элемента с помощью.text
# assert "(3)" in element_get_text

# 4444444444444444
# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver,2)
# driver.get("https://practice.automationtesting.in/")
# Myacc = driver.find_element_by_id("menu-item-50")
# Myacc.click()
# login = driver.find_element_by_id("username")
# login.send_keys("qwerty@mail.com")
# passw = driver.find_element_by_id("password")
# passw.send_keys("Qaz123/*-!@#mjyGVBJIs5423")
# Log = driver.find_element_by_css_selector("login,[value='Login']")
# Log.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# element = driver.find_element_by_css_selector('[value="menu_order"]')
# element2 = element.get_attribute("selected")
# # print("value of element: ", element2)
# if element2 is not None: #проверяем, если значение атрибута НЕ пустое, значит чекбокс отмечен
#     print("Сортировка по умолчанию")
# else:
#     print("Что-то пошло не так")
# High = driver.find_element_by_class_name("orderby").click()
# High = driver.find_element_by_css_selector("option:nth-child(6)").click()
# High2= driver.find_element_by_css_selector("option:nth-child(6)")
# if High2.is_selected(): #проверяем, если значение атрибута НЕ пустое, значит чекбокс отмечен
#     print("Сортировка по цене от большей к меньшей")
# else:
#     print("Что-то другое")

# 555555555555555

# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver,2)
# driver.get("https://practice.automationtesting.in/")
# Myacc = driver.find_element_by_id("menu-item-50")
# Myacc.click()
# login = driver.find_element_by_id("username")
# login.send_keys("qwerty@mail.com")
# passw = driver.find_element_by_id("password")
# passw.send_keys("Qaz123/*-!@#mjyGVBJIs5423")
# Log = driver.find_element_by_css_selector("login,[value='Login']")
# Log.click()
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# Android = driver.find_element_by_css_selector("a[href='https://practice.automationtesting.in/product/android-quick-start-guide/']")
# Android.click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# assert book_old_price_text == "₹600.00"
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_new_price_text == "₹450.00"
# Book = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# Book.click()
# Close = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# Close.click()

# # 6666666666666
# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver,2)
# driver.get("https://practice.automationtesting.in/")
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# Addboock = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]').click()
# time.sleep(3)
# # Oneitem = driver.find_element_by_class_name("cartcontents")
# # Oneitem_text = Oneitem.text
# # assert Oneitem_text == "1 item"
# element = driver.find_element_by_css_selector(".main-nav > #wpmenucartli > a")
# assert "₹180.00" in element.text
# Trash = driver.find_element_by_class_name('wpmenucart-contents').click()
# some_element= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td"), "180.00"))
# some_element2= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong > span"), "183.60"))

# 77777777777777777
# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver,2)
# driver.get("https://practice.automationtesting.in/")
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# Addboock = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]').click()
# time.sleep(2)
# Addboock2 = driver.find_element_by_css_selector("a[href='/shop/?add-to-cart=180']").click()
# time.sleep(2)
# Trash = driver.find_element_by_class_name('wpmenucart-contents').click()
# time.sleep(2)
# dell = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a").click()
# time.sleep(2)
# nodell = driver.find_element_by_css_selector("div.woocommerce-message > a").click()
# element3 = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
# element3.clear()
# element3.send_keys('3')
# apd = driver.find_element_by_css_selector("tr:nth-child(3) > td > input.button").click()
# element4 = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input") #нашли элемент по составному селектору
# element4_value = element4.get_attribute("value")
# assert element4_value == '3'
# time.sleep(2)
# apply = driver.find_element_by_css_selector(".coupon > .button").click()
# text1 = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > ul > li")
# text = text1.text
# assert text == "Please enter a coupon code."

# 8888888888888
# import time
# import click
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.expected_conditions import url_to_be
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(2)
# wait = WebDriverWait(driver,2)
# driver.get("https://practice.automationtesting.in/")
# Shop = driver.find_element_by_id("menu-item-40")
# Shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# Addboock = driver.find_element_by_css_selector('a[href="/shop/?add-to-cart=182"]').click()
# time.sleep(2)
# Trash = driver.find_element_by_class_name('wpmenucart-contents').click()
# time.sleep(2)
# CHECKOUT = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
# proceed = driver.find_element_by_css_selector(".checkout-button.button.alt.wc-forward").click()
# first = driver.find_element_by_css_selector("#billing_first_name")
# first.send_keys("Alex")
# last = driver.find_element_by_css_selector("#billing_last_name")
# last.send_keys("Mo")
# email = driver.find_element_by_css_selector("#billing_email")
# email.send_keys("qwert@mali.com")
# phone = driver.find_element_by_css_selector("#billing_phone")
# phone.send_keys("987654321")
# Country = driver.find_element_by_css_selector("#s2id_billing_country").click()
# time.sleep(2)
# Country2 = driver.find_element_by_css_selector("#s2id_autogen1_search")
# Country2.send_keys("Russia")
# Country3 = driver.find_element_by_css_selector("#select2-results-1 > li").click()
# Street = driver.find_element_by_css_selector("#billing_address_1")
# Street.send_keys("1 Kutuzovsky Prospekt")
# Citi = driver.find_element_by_css_selector("#billing_city")
# Citi.send_keys("Moscow")
# State = driver.find_element_by_css_selector("#billing_state")
# State.send_keys("Moscow")
# Postcode = driver.find_element_by_css_selector("#billing_postcode")
# Postcode.send_keys("666666")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# Payments = driver.find_element_by_css_selector("[value='cheque']").click()
# Order = driver.find_element_by_css_selector("#place_order").click()
# Title1 = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received")))
# Title = driver.find_element_by_css_selector("#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received")
# Title_get = Title.text
# assert Title_get == "Thank you. Your order has been received."
# time.sleep(3)
# Method = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td"), "Check Payments"))