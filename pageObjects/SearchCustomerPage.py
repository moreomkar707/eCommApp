from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchCustomerClass:

    txtbox_SearchEmail_id = "SearchEmail"
    txtbox_SearchFirstName_id = "SearchFirstName"
    txt_SearchLastName_id = "SearchLastName"
    btn_searchCustomers_id = "search-customers"

    table_xpath = "//div[@class='dt-scroll-body']"
    tblRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tblColums_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enterEmail(self, email):
        self.driver.find_element(By.ID, self.txtbox_SearchEmail_id).clear()
        self.driver.find_element(By.ID, self.txtbox_SearchEmail_id).send_keys(email)

    def enterFirstName(self, Fname):
        self.driver.find_element(By.ID, self.txtbox_SearchFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtbox_SearchFirstName_id).send_keys(Fname)

    def enterLastName(self, Lname):
        self.driver.find_element(By.ID, self.txt_SearchLastName_id).clear()
        self.driver.find_element(By.ID, self.txt_SearchLastName_id).send_keys(Lname)

    def clickSerachBtn(self):
        self.driver.find_element(By.ID, self.btn_searchCustomers_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tblRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tblColums_xpath))


    def searchCustomerByEmail(self, email):
        flag = False


        for r in range(1,self.getNoOfRows()+1):
          table = self.driver.find_element(By.XPATH, self.table_xpath)
          emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          if emailid == email:
              flag = True
              break
        return flag

    def searchCustomerByName(self, name):
        flag = False

        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            # wait = WebDriverWait(self.driver, 10)
            # wait.until(expected_conditions.visibility_of_element_located(table))
            Name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if Name == name:
                flag = True
                break
        return flag
