from datetime import datetime

import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium.webdriver.common.by import By

class Test004AddCustomerddt:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData/AddCustomer.xlsx"

    logger = LogGen.logGen()

    @pytest.mark.functional
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("***** Test Started *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login sucessfull *******")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(8)
        self.addCust.clickOnCustomerMenuitem()
        time.sleep(3)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("total rows:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.firstname = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.lastname = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.gender = XLUtils.readData(self.path, 'Sheet1', r, 4)

            self.addCust.clickOnAddNew()
            self.logger.info("***** Providing Info *******")

            self.email = random_generator() + "@gmail.com"
            self.addCust.setEmail(self.email)
            self.addCust.setPassword(self.password)
            self.addCust.setFname(self.firstname)
            self.addCust.setLname(self.lastname)
            self.addCust.setGender(self.gender)
            self.addCust.clickSave()
            self.logger.info("***** Saving Customer Info *******")
            self.logger.info("***** Validation started *******")
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text
            print(self.msg)
            XLUtils.writeData(self.path, 'Sheet1',r,5,self.msg)

            if 'The new customer has been added successfully.' in self.msg:
                lst_status.append("Pass")
            else:
                current_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
                self.driver.save_screenshot(".\\Screenshots\\test_homepageTitle_" + current_time_str + ".png")
                self.logger.error(
                    "******************************* Test failed *******************************  ")
                lst_status.append("Fail")

        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("************* full test pass************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************* full test Failed************")
            self.driver.close()
            assert False

        self.logger.error(
            "******************************* END That has changed *******************************  ")
def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





