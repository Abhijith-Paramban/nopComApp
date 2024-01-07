from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer():
    lnkCustomer_menu_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]"
    lnkCustomer_menuitem_xpath = "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]"
    btnAddNew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFname_xpath = "//input[@id='FirstName']"
    txtLname_xpath = "//input[@id='LastName']"
    rbMale_xpath = "//input[@id='Gender_Male']"
    rbFemale_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompName_xpath = "//input[@id='Company']"
    chkTaxex_xpath = "//input[@id='IsTaxExempt']"
    txtNewsltr_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]"
    txtCustrole_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    drpMgrVnd_xpath = "//select[@id='VendorId']"
    lstVend1_xpath = "//option[contains(text(),'Vendor 1')]"
    lstVend2_xpath = "//option[contains(text(),'Vendor 2')]"
    txtAdmnCont_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]"

    def __init__(self, driver):
        self.driver = driver


    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnCustomerMenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menuitem_xpath).click()

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)


    def setFname(self,fname):
        self.driver.find_element(By.XPATH, self.txtFname_xpath).send_keys(fname)


    def setLname(self,lname):
        self.driver.find_element(By.XPATH, self.txtLname_xpath).send_keys(lname)


    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rbMale_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rbFemale_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rbMale_xpath).click()

    def setDob(self,dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element(By.XPATH, self.txtCompName_xpath).send_keys(cname)

    def setMgrVender(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpMgrVnd_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self,acomm):
        self.driver.find_element(By.XPATH, self.txtAdmnCont_xpath).send_keys(acomm)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()












