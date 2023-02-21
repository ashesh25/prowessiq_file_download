from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class SearchPage(BasePage):

    search_txtbox = (By.ID, "compsrch")



    def __init__(self, browser):
        self.browser = browser

    def enter_company_name(self, company_name):
        BasePage(self.browser).clear_text_box(self.search_txtbox)
        BasePage(self.browser).input_element(self.search_txtbox,company_name)
        time.sleep(2)
        BasePage(self.browser).press_down_arrow_key()
        time.sleep(2)
        BasePage(self.browser).press_enter_key()


    def download_files(self):
        rows = self.browser.find_elements_by_xpath("//b[contains(text(),'Images of Rating Rationale')]/parent::th/parent::tr/parent::tbody/tr")
        rows.pop(0)
        print(len(rows))
        for i in range(len(rows)):
            j = i
            j = j + 2
            columns = self.browser.find_elements_by_xpath("//b[contains(text(),'Images of Rating Rationale')]/parent::th/parent::tr/parent::tbody/tr["+str(j)+"]/td")
            print(len(columns))
            for k in range(len(columns)):
                columns[k].click()
                time.sleep(1)
        #time.sleep(5)




