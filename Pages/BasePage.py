from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def get_page_title(self):
        try:
            return self.browser.title
            #WebDriverWait(self.browser, 10).until(EC.title_contains("HackerEarth"))
            print(self.browser.title)

        except TimeoutException:
            return False

    def input_element(self, by_locator, text):
        try:
            element = WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except TimeoutException:
            return false

    def click_element(self, by_locator):
        try:
            element = WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException:
            return false

    def is_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except TimeoutException:
            return false

    def clear_text_box(self, by_locator):
        try:
            element = WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located(by_locator)).clear()
        except TimeoutException:
            return false


    def press_enter_key(self):
        try:
            actions = ActionChains(self.browser)
            actions.send_keys(Keys.ENTER).perform()
        except TimeoutException:
            return false


    def press_down_arrow_key(self):
        try:
            actions = ActionChains(self.browser)
            actions.send_keys(Keys.DOWN).perform()
        except TimeoutException:
            return false

