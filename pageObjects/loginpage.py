from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def enter_user_email(self, email):
        try:
            email_field = self.driver.find_element(By.XPATH, "//input[@id='Email']")
            email_field.clear()
            email_field.send_keys(email)
        except:
            print("Something went wrong")


    def enter_user_password(self, password):
        try:
            password_field = self.driver.find_element(By.XPATH, "//input[@id='Password']")
            password_field.clear()
            password_field.send_keys(password)
        except:
            print("Something went wrong.")


    def click_login(self):
        try:
            login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
            login_button.click()
        except:
            print("Something went wrong")


    def click_logout(self):
        try:
            logout_link = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
            logout_link.click()
        except:
            print("Something went wrong.")



        