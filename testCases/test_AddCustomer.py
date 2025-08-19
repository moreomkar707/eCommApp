import random
import string
import time

from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomerClass
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class TestAddCustomer:

    baseURL = ReadConfig.getURL()
    path = ".//testData//LoginData.xlsx"
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()


    def test_addCustomer(self, setup):
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
        self.addcust.clickOnAddNew()
        self.email = random_generator()
        self.addcust.enterEmail(self.email + "@gmail.com")
        self.addcust.enterPassword("add@123")
        self.addcust.enterFirstName("Sam")
        self.addcust.enterLastFName("Tarly")
        self.addcust.setGender("Male")
        self.addcust.enterCompanyName("GOT")
        self.addcust.enterNewsLetter("hi, i'am sam tarly")
        # self.addcust.setCustomerRole("Administrators")
        # time.sleep(5)
        self.addcust.setCustomerRole("Forum Moderators")
        self.addcust.setManagerOfVendor(1)
        self.addcust.enterAdminComment("this is sam tarly from GOT. thank you john snow.")
        self.addcust.clickOnSave()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True
        else:

            assert False
        self.driver.close()



def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))









