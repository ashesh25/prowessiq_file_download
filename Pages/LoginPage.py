from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    txt_username = (By.NAME, "username")
    txt_password = (By.NAME, "password")
    btn_login = (By.NAME, "Submit")
    logout_link = (By.XPATH, "//a[text()='Logout']")


    def __init__(self, browser):
        self.browser = browser

    def validate_login_page_title(self):
        title = BasePage(self.browser).get_page_title()
        if title.__contains__("ProwessIQ"):
            print(self.browser.title)
            assert True
        else:
            assert False


    def enter_username(self, user):
        BasePage(self.browser).input_element(self.txt_username, user)


    def enter_pwd(self, pwd):
        BasePage(self.browser).input_element(self.txt_password, pwd)


    def click_login_btn(self):
        BasePage(self.browser).click_element(self.btn_login)


    def verify_login_successful(self):
        BasePage(self.browser).is_element_displayed(self.logout_link)

    def logout(self):
        BasePage(self.browser).click_element(self.logout_link)
