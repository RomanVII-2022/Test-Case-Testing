from pageObjects.loginpage import Login
from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
import pytest


class Test_001_Login:
    base_url = ReadConfig.get_app_url()
    email = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.logger.debug("****** Test_001_Login ******")
        self.logger.debug("****** Veryfing ******")
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.quit()
            self.logger.debug("****** Home page test passed ******")
        else:
            self.driver.save_screenshot("C:\\highbridselenium\\ecommerceApp\\screenshots\\test_homepage_title.png")
            self.driver.quit()
            self.logger.debug("****** Home page test failed ******")
            assert False


    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.debug("****** Veryfing Login ******")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp=Login(self.driver)
        self.lp.enter_user_email(self.email)
        self.lp.enter_user_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.quit()
            self.logger.debug("****** Login Test Passed ******")
        else:
            self.driver.save_screenshot("C:\\highbridselenium\\ecommerceApp\\screenshots\\test_login.png")
            self.driver.quit()
            self.logger.debug("****** Login Test Failed ******")
            assert False





