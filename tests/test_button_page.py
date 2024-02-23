import pytest
from selenium.webdriver.common.by import By
from pages.simple_button import SimpleButtonPage


# Проверим, что кнопка есть на странице
def test_button1_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button().is_displayed()


# Проверим, что кнопка успешно нажимается
def test_button1_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.button_click()
    assert 'Submitted' == simple_page.result_text
