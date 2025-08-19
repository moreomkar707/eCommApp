import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_email_id = 'Email'
    textbox_password_id = 'Password'
    login_button_xpath = "//button[@type = 'submit']"
    logout_button_xpath = "//a[text()= 'Logout']"


    def __init__(self, driver):
        self.driver = driver


    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()


    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()





