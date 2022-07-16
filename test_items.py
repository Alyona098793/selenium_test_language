
from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_is(browser):
    browser.get(link)
    time.sleep(5)
    button = len(browser.find_elements(By.CSS_SELECTOR, ".btn-primary"))
    assert button>0, "Нет кнопки"