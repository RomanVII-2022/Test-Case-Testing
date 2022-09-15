import pytest
from pageObjects.loginpage import Login
from pageObjects.customeradd import AddCustomer
from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
import string
import random
from selenium.webdriver.common.by import By

class Test_003_AddCustomer:
    baseURL = ReadConfig.get_app_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.log_gen()  

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.debug("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.click_login()
        self.logger.debug("************* Login succesful **********")

        self.logger.debug("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.customer_menu_click()
        self.addcust.customer_menu_item_click()

        self.addcust.add_new_click()

        self.logger.debug("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.enter_email(self.email)
        self.addcust.enter_password("test123")
        self.addcust.enter_customerRoles("Registered")
        self.addcust.manager_of_vendor("Vendor 2")
        self.addcust.click_gender("Male")
        self.addcust.enter_firstname("Pavan")
        self.addcust.enter_lastname("Kumar")
        self.addcust.enter_DOB("7/05/1985")
        self.addcust.enter_companyName("busyQA")
        self.addcust.enter_admin_comment("This is for testing.........")
        self.addcust.click_save()

        self.logger.debug("************* Saving customer info **********")

        self.logger.debug("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.debug("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot("C:\\highbridselenium\\ecommerceApp\\screenshots\\test_addCustomer.png")
            self.logger.debug("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.debug("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))