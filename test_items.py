from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_basket(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button"), "Отсутствует кнопка: добавить в корзину товар"
    # таймаут чтобы убедится в правильности выбора языка страницы
    time.sleep(5)
