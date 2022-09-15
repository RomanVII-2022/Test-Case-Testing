from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from utilities.customlogger import LogGen

class AddCustomer:
    logger = LogGen.log_gen()

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def customer_menu_click(self):
        try:
            self.driver.find_element(By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]").click()
        except:
            self.logger.debug("Something went wrong")

    def customer_menu_item_click(self):
        try:
            self.driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()
        except:
            self.logger.debug("Something went wrong")


    def add_new_click(self):
        try:
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Add new']").click()
        except:
            self.logger.debug("Something went wrong")


    def enter_email(self, email):
        try:
            self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(email)
        except:
            self.logger.debug("Something went wrong")



    def enter_password(self,password):
        try:
            self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)
        except:
            self.logger.debug("Something went wrong")


    def enter_firstname(self,fname):
        try:
            self.driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys(fname)
        except:
            self.logger.debug("Something went wrong")


    def enter_lastname(self,lname):
        try:
            self.driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys(lname)
        except:
            self.logger.debug("Something went wrong")

    def click_gender(self, gender):
        try:
            if gender == "Male":
                self.driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()
            else:
                self.driver.find_element(By.XPATH, "//input[@id='Gender_Female']").click()
        except:
            self.logger.debug("Something went wrong")

    
    def enter_DOB(self,DOB):
        try:
            self.driver.find_element(By.XPATH, "//input[@id='DateOfBirth']").send_keys(DOB)
        except:
            self.logger.debug("Something went wrong")


    def enter_companyName(self,companyName):
        try:
            self.driver.find_element(By.XPATH, "//input[@id='Company']").send_keys(companyName)
        except:
            self.logger.debug("Something went wrong")


    def enter_customerRoles(self, role):
        try:
            self.driver.find_element(By.XPATH, "//div[@class='input-group-append input-group-required']//div[@role='listbox']").click()
            time.sleep(3)
            if role == 'Registered':
                self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Registered']")
            elif role == 'Administrators':
                self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Administrators']")
            elif role == 'Guests':
                time.sleep(3)
                self.driver.find_element(By.XPATH, "//body[1]/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[2]/span[1]").click()
                self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Guests']")
            elif role == 'Vendors':
                self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Vendors']")
            else:
                self.listitem = self.driver.find_element(By.XPATH, "//li[normalize-space()='Registered']")
            
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.listitem)
        except:
            self.logger.debug("Something went wrong")


    def manager_of_vendor(self, value):
        try:
            vendor = Select(self.driver.find_element(By.XPATH, "//select[@id='VendorId']"))
            vendor.select_by_visible_text(value)
        except:
            print("Something went wrong")


    def enter_admin_comment(self, comment):
        try:
            self.driver.find_element(By.XPATH, "//textarea[@id='AdminComment']").send_keys(comment)
        except:
            self.logger.debug("Something went wrong")


    def click_save(self):
        try:
            self.driver.find_element(By.XPATH, "//button[@name='save']").click()
        except:
            self.logger.debug("Something went wrong")

        
