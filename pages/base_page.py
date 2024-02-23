# Данный класс будет хранить в себе общие методы, которые будут доступны всем
class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

