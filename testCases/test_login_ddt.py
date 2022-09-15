from pageObjects.loginpage import Login
from utilities.readproperty import ReadConfig
from utilities.customlogger import LogGen
from utilities import xlutils
import time
import pytest


@pytest.mark.regression
class Test_002_Login_DDT:
    base_url = ReadConfig.get_app_url()
    path = "C://highbridselenium//ecommerceApp//testData//login.xlsx"
    logger = LogGen.log_gen()

    
    def test_login_ddt(self, setup):
        self.logger.debug("****** Test_002_Login_DDT ******")
        self.logger.debug("****** Veryfing Login ******")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp=Login(self.driver)

        self.rows=xlutils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in Excel:",self.rows)

        list_status = []

        for r in range(2,self.rows+1):
            self.user = xlutils.readData(self.path,'Sheet1',r,1)
            self.password = xlutils.readData(self.path,'Sheet1',r,2)
            self.exp = xlutils.readData(self.path,'Sheet1',r,3)

            self.lp.enter_user_email(self.user)
            self.lp.enter_user_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
        
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.debug("***** Test passed successfully *****")
                    self.lp.click_logout()
                    list_status.append("Pass")
                
                elif self.exp == "Fail":
                    self.logger.debug("***** Test failed *****")
                    self.lp.click_logout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.debug("***** Test failed *****")
                    list_status.append("Fail")
                
                elif self.exp == "Fail":
                    self.logger.debug("***** Test Passed *****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.debug("Login DDT Passed...")
            self.driver.close()
            assert True
        else:
            self.logger.debug("Login DDT Failed...")
            self.driver.close()
            assert False


        self.logger.debug("****** End of Login DDT Test ****")
        self.logger.debug("****** Completed Login DDT Test ****")







