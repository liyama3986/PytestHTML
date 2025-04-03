from selenium.webdriver.common.by import By

# for test
class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def enter_username(self, username):
        self.browser.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.browser.find_element(By.ID, "submit").click()

    def get_error_message(self):
        return self.browser.find_element(By.XPATH, "//section[@id='login']//div[@id='error']").text

    def get_success_message(self):
        return self.browser.find_element(By.CLASS_NAME, "has-text-align-center").text
