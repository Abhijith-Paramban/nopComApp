from datetime import datetime

import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium.webdriver.common.by import By

class Test003AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    @pytest.mark.functional
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
        self.addCust.clickOnAddNew()

        self.logger.info("***** Providing Info *******")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFname("Test Fname")
        self.addCust.setLname("test Lname")
        self.addCust.setDob("07/07/1997")
        self.addCust.setGender("Female")
        self.addCust.clickSave()
        self.logger.info("***** Saving Customer Info *******")
        self.logger.info("***** Validation started *******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("******** test Passed")
        else:
            current_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
            self.driver.save_screenshot(".\\Screenshots\\test_homepageTitle_" + current_time_str + ".png")
            self.logger.error(
                "******************************* Test failed *******************************  ")
            assert True == False

        self.driver.close()
        self.logger.error(
            "******************************* END *******************************  ")



def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





