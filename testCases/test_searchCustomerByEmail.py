import time

import pytest

from pageObjects.AddCustomerPage import AddCustomerClass
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerClass
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByEmail:

    baseURL = ReadConfig.getURL()
    path = ".//testData//LoginData.xlsx"
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.first
    def test_serachCustomerByEmail_005(self, setup):

        self.driver = setup

        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust = AddCustomerClass(self.driver)
        self.addcust.clickOnCustomersMenue()
        self.addcust.clickOnCustomersMenueItem()

        self.searchEmail = SearchCustomerClass(self.driver)
        self.searchEmail.enterEmail("u8jzbau0@gmail.com")
        self.searchEmail.clickSerachBtn()

        time.sleep(4)
        status = self.searchEmail.searchCustomerByEmail("u8jzbau0@gmail.com")

        assert True == status

        self.driver.close()




