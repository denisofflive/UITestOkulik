from pages.like_a_button import LikeAButton


# Проверим, что кнопка есть на странице
def test_button2_exist(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    assert like_a_button.button_is_displayed


# Проверим, что кнопка успешно нажимается
def test_button2_clicked(browser):
    like_a_button = LikeAButton(browser)
    like_a_button.open()
    like_a_button.button_click()
    assert 'Submitted' == like_a_button.result_text
