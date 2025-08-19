import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerClass:

    lnkcustomers_menu_xpath = "//i[@class='nav-icon far fa-user']"
    lnkcustomers_option_xpath = "//a[@class='nav-link']/p[text()=' Customers']"
    btnadd_new_xpath = "//a[@class='btn btn-primary']"
    txtbox_email_name = "Email"
    txtbox_password_name = "Password"
    txtbox_firstname_name = "FirstName"
    txtbox_lastname_name = "LastName"
    rdbtn_male_id = "Gender_Male"
    rdbtn_female_id = "Gender_Female"
    txtbox_company_name = "Company"
    checkbox_is_tax_exempt_name = "IsTaxExempt"
    txtbox_newsletter_classname = "select2-search__field"
    lstcustomer_role_xpath = "//span[@class='selection']/following::ul"
    lstitem_Administrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitem_Forum_Moderators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    lstitem_Registered_xpath = "//li[contains(text(), 'Registered')]"
    lstitem_Guests_xpath = "//li[contains(text(), 'Guests')]"
    lstitem_Vendors_xpath = "//li[contains(text(), 'Vendors')]"
    drp_manager_of_vendor_id = "VendorId"
    checkbox_active_id = "Active"
    checkbox_MustChangePassword_name = "MustChangePassword"
    txtbox_AdminComment_name = "AdminComment"
    btn_save_name = "save"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenue(self):
        self.driver.find_element(By.XPATH, self.lnkcustomers_menu_xpath).click()

    def clickOnCustomersMenueItem(self):
        self.driver.find_element(By.XPATH, self.lnkcustomers_option_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnadd_new_xpath).click()

    def enterEmail(self, email):
        self.driver.find_element(By.NAME, self.txtbox_email_name).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.NAME, self.txtbox_password_name).send_keys(password)

    def enterFirstName(self, firstname):
        self.driver.find_element(By.NAME, self.txtbox_firstname_name).send_keys(firstname)

    def enterLastFName(self, lastname):
        self.driver.find_element(By.NAME, self.txtbox_lastname_name).send_keys(lastname)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdbtn_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdbtn_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdbtn_male_id).click()

    def enterCompanyName(self, company):
        self.driver.find_element(By.NAME, self.txtbox_company_name).send_keys(company)

    def enterNewsLetter(self, newsletter):
        self.driver.find_element(By.CLASS_NAME, self.txtbox_newsletter_classname).send_keys(newsletter)

    def setCustomerRole(self, role):
        self.driver.find_element(By.XPATH, self.lstcustomer_role_xpath).click()
        time.sleep(3)

        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Registered_xpath)

        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Administrators_xpath)

        elif role == "Guest":
            time.sleep(3)
            self.driver.find_element(By.XPATH, "// li[ @class ='select2-selection__choice' and @ title='Registered'] / span[text()='×']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Vendors_xpath)

        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Forum_Moderators_xpath)

        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_Guests_xpath)
        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, ind):
        drp = Select(self.driver.find_element(By.ID, self.drp_manager_of_vendor_id))
        drp.select_by_index(ind)

    def enterAdminComment(self, comment):
        self.driver.find_element(By.NAME, self.txtbox_AdminComment_name).send_keys(comment)


    def clickOnSave(self):
        self.driver.find_element(By.NAME, self.btn_save_name).click()