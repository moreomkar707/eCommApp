import time

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.AddCustomerPage import AddCustomerClass
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomerClass
from utilities.readProperties import ReadConfig


class Test_SearchCustomerByName:

    baseURL = ReadConfig.getURL()
    path = ".//testData//LoginData.xlsx"
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.first
    def test_serachCustomerByName_006(self, setup):

        self.driver = setup

        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)

        self.driver.get(self.baseURL)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addcust = AddCustomerClass(self.driver)
        self.addcust.clickOnCustomersMenue()
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.visibility_of_element_located(self.addcust.lnkcustomers_option_xpath))
        time.sleep(4)
        self.addcust.clickOnCustomersMenueItem()

        self.searchName = SearchCustomerClass(self.driver)
        self.searchName.enterFirstName("Sam")
        self.searchName.enterLastName("Tarly")
        self.searchName.clickSerachBtn()


        time.sleep(4)
        status = self.searchName.searchCustomerByName("Sam Tarly")

        assert True == status

        self.driver.close()




