import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test002Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/TestLogin.xlsx"
    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******************************* test_login_ddt started *******************************  ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("total rows:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************* passed ************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("************* Fail ************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Fail":
                    self.logger.info("************* Fail ************")
                    lst_status.append("Pass")
                elif self.exp == "Pass":
                    self.logger.info("************* Pass ************")
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
