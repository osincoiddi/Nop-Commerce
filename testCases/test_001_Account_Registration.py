#https://demo.nopcommerce.com/
# Note: site has CAPCHA and cannot automate.
import pytest
from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.firefox.service import Service as firefoxService
from PageObject.AccountPage import AccountPage
from Utilities.customLogger import LogGen as LogGen


class Test_001_Account_Registration:
    url="https://demo.nopcommerce.com/"
    # url=Readconfig.getApplicationurl()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_Account_Reg(self,setup):
            self.logger.info("Launching browser---")
            self.driver=setup
            self.logger.info("Launching nopCommercial")
            self.driver=webdriver.Firefox()
            self.driver.get("https://demo.nopcommerce.com/")
            # self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            self.ap=AccountPage(self.driver)
            self.logger.info("Navigating registration page---")
            self.ap.clickregister()
            self.ap.clickgender()
            self.ap.inputfirstname("Ama")
            self.ap.inputlastname("Alex")
            self.ap.inputemail("tiyumiddi@gmail.com")
            self.ap.inputcompanyname("Udemy")
            self.ap.setpassword("Amama@2014")
            self.ap.setconfirmpassword("Amama@2014")
            self.ap.clickregister()
            self.logger.info("Registration Successful")
            self.driver.quit()


