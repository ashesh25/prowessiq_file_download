from pytest_bdd import given, when, then, parsers, scenarios
from Pages.LoginPage import LoginPage
from Pages.SearchPage import SearchPage
from Utility.FolderUtil import FolderUtil



scenarios('../login.feature')


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


@then(parsers.parse('user search with company "{company_name}"'))
def search_with_company_name(browser, company_name):
    SearchPage(browser).enter_company_name(company_name)


@then(parsers.parse('user creates local folder with name "{folder_name}"'))
def create_folder_with_company_name(folder_name):
    FolderUtil.create_new_folder(folder_name)


@then(parsers.parse('user downloads all the documents'))
def user_download_doc(browser):
    SearchPage(browser).download_files()


@then(parsers.parse('user clear all the previous file from "{folder_name}"'))
def clear_folder(folder_name):
    FolderUtil.clear_folder(folder_name)

@then(parsers.parse('Moves all files from download to "{folder_name}"'))
def move_files(folder_name):
    FolderUtil.move_docs_from_download_to_folder(folder_name)


@then(parsers.parse('user logs out of the application'))
def logout(browser):
    LoginPage(browser).logout()




