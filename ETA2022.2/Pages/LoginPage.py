
from Pages.PageObject import PageObject
from selenium.webdriver.common.by import By


class LoginPage(PageObject):
    #Localizadores
    url_login = 'https://www.saucedemo.com/'
    id_login_bnt = 'login-button'
    class_error_message = 'error-message-container'
    text_error_message = 'Epic sadface: Username is required'
    id_username = 'user-name'
    id_password = 'password'

    #Métodos
    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.get(self.url_login)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_bnt).click()

    def is_url_login(self):
        return self.is_url(url=self.url_login)

    def has_login_message_error(self):
        error_message = self.driver.find_element(By.CLASS_NAME, self.class_error_message).text
        return error_message == self.text_error_message

    def efetuar_login(self, username='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_btn()
