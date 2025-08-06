from selenium import webdriver
from selenium.webdriver.common.by import By


class AccountPage:
    #locators
    reg_button1_xpath= "//a[normalize-space()='Register']"
    gender_button_xpath="//input[@id='gender-male']"
    input_first_name= "//input[@id='FirstName']"
    input_last_name_xpath="//input[@id='LastName']"
    input_email_xpath="//input[@id='Email']"
    input_company_name_xpath="//input[@id='Company']"
    input_password_xpath="//input[@id='Password']"
    input_confirm_password_xpath="//input[@id='ConfirmPassword']"
    reg_button2_xpath="//button[@id='register-button']"

    #constrator
    def __init__(self,driver):
        self.driver=driver

        #action method

    def clickregister(self):
            self.driver.find_element(By.XPATH,self.reg_button1_xpath).click()

    def clickgender(self):
        self.driver.find_element(By.XPATH,self.gender_button_xpath).click()

    def inputfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.input_first_name).send_keys(fname)

    def inputlastname(self,lname):
        self.driver.find_element(By.XPATH,self.input_last_name_xpath).send_keys(lname)


    def inputemail(self,email):
        self.driver.find_element(By.XPATH,self.input_email_xpath).send_keys(email)


    def inputcompanyname(self,cname):
        self.driver.find_element(By.XPATH,self.input_company_name_xpath).send_keys(cname)

    def setpassword(self,pwd):
        self.driver.find_element(By.XPATH,self.input_password_xpath).send_keys(pwd)

    def setconfirmpassword(self,cpwd):
        self.driver.find_element(By.XPATH,self.input_confirm_password_xpath).send_keys(cpwd)

    def clickregisterbtn(self):
        self.driver.find_element(By.XPATH,self.reg_button2_xpath).click()

