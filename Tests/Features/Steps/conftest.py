import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then, parsers


@pytest.fixture(scope="session", autouse=True)
def browser():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(60)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--safebrowsing-disable-download-protection')
    chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
    yield driver
    driver.quit()


@given(parsers.parse("Close the browser"))
def close_browser():
    driver.close()
    browser()


@given(parsers.parse("Launch URL"))
def launch_url(browser):
    print("URL launched")
    browser.get("https://prowessiq.cmie.com/kommon/bin/sr.php?kall=wscandocs&srchcriteria=entity&cocode=100632&coname=INFOSYS+LTD.")


@given(parsers.parse("Verify the Login Page title"))
def verify_login_page_loaded(browser):
    print("entered")
    LoginPage(browser).validate_login_page_title()

@then(parsers.parse('user enters username as "{username}"'))
def user_enter_username(browser, username):
    LoginPage(browser).enter_username(username)


@then(parsers.parse('password as "{password}"'))
def user_enter_password(browser, password):
    LoginPage(browser).enter_pwd(password)

@then(parsers.parse('hits the login button'))
def click_login_button(browser):
    LoginPage(browser).click_login_btn()


@then(parsers.parse('Verify Login was successful'))
def verify_login(browser):
    LoginPage(browser).verify_login_successful()



