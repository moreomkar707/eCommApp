import time

from  selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

from utilities import ExcelRead
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class TestLoginPage:

    baseURL = ReadConfig.getURL()
    path = ".//testData//LoginData.xlsx"
    log = LogGen.loggen()

    def test_homePageTilte_001(self, setup):

        self.log.info("==== test_homePageTilte_001 is Started ======")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        # self.driver.close()

        if actual_title == "nopCommerce demo store. Login":
            self.driver.close()
            self.log.info("test_homePageTilte_001 is Passed.")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTilte_001_fail.png")
            self.driver.close()
            self.log.info("test_homePageTilte_001 is Failed.")
            assert False


    def test_login_002(self, setup):
        self.log.info("==== test_login_002 is Started.====.")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)




        if self.driver.title == "Dashboard / nopCommerce administration":
            assert True
            self.log.info("test_login_002 is Passed.")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login_002_fail.png")
            self.driver.close()
            self.log.info("test_login_002 is Failed.")
            assert False

    @pytest.mark.smoke
    def test_login_ddt_003(self, setup):
        self.log.info("==== test_login_ddt_003 is Started.====.")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.row = ExcelRead.readRowCount(self.path, 'Sheet1')

        loginStatus = []

        for r in range(2, self.row + 1):
            self.username = ExcelRead.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelRead.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelRead.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    loginStatus.append('Pass')
                    self.lp.clickLogout()
                elif self.exp == "Fail":
                    self.lp.clickLogout()
                    loginStatus.append("Fail")

            elif exp_title != act_title:
                if self.exp == "Fail":
                    loginStatus.append('Pass')
                elif self.exp == "Pass":
                    loginStatus.append("Fail")

        if "Fail" not in loginStatus:
            self.log.info("test_login_ddt_003 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_003 is Failed")
            assert False






        # if act_title == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.log.info("test_login is Passed.")
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\test_login_fail.png")
        #     self.driver.close()
        #     self.log.info("test_login is Failed.")
        #     assert False
















