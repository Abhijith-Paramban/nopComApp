import pytest

from pageObjects.LoginPage import LoginPage
from datetime import datetime
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    @pytest.mark.functional
    def test_homepageTitle(self, setup):
        self.logger.info("******************************* test_homepageTitle started *******************************  ")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******************************* test_login started *******************************  ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info(
                "******************************* test_login passed *******************************  ")
            self.driver.close()

        else:
            current_time_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
            self.driver.save_screenshot(".\\Screenshots\\test_homepageTitle_" + current_time_str + ".png")
            self.logger.error(
                "******************************* test_homepageTitle failed *******************************  ")
            self.driver.close()
            assert False
