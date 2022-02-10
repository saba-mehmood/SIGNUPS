
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

from config import TestData

#EMAIL='avax123@yopmail.com'

# driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.get("https://yopmail.com/en/")
# print(driver.title)

# driver.find_element(By.CLASS_NAME,'ycptinput').send_keys('avax-06@yopmail.com')
# driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
# driver.switch_to.frame(driver.find_element(By.ID,'ifmail'))
# driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]').click()
# #driver.find_element_by_xpath('//*[@id="mail"]/div/div/div/table[1]/tbody/tr/td/table/tbody/tr/td/table').click()

# time.sleep(3)


class Yopmail(object):

      def __init__(self,driver):
         self.driver = driver
     
      def Yop_mail(self):
         """YOPMAIL"""
         self.driver.execute_script("window.open()")
         self.driver.switch_to.window(self.driver.window_handles[1])
         self.driver.get("https://yopmail.com/en/")
         time.sleep(20)
         mail_field = self.driver.find_element(By.CLASS_NAME,'ycptinput')
         mail_field.send_keys(Keys.CONTROL, "a")
         mail_field.send_keys(Keys.BACKSPACE)
         mail_field.send_keys(TestData.EMAIL)
         self.driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
         time.sleep(8)
         frame_login = self.driver.switch_to.frame(self.driver.find_element(By.ID,'ifmail'))
         try:
            login_btn= self.driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
            login_link=self.driver.find_element(By.LINK_TEXT,'Click here')
            signup_link= self.driver.find_element(By.LINK_TEXT,'Verify Email')
            if login_btn.is_displayed() and login_btn.is_enabled():
               login_btn.click() 
            elif login_link.is_displayed():
                  login_link.click()
            elif signup_link.is_displayed():
                  signup_link.click()     
            else:
                        print("Login Handle")

         except:
               continue_signup = self.driver.find_element(By.XPATH,'/html/body/main/div/div/div/div/div/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/a/b')
      
               if continue_signup.is_displayed():
                   continue_signup.click()      
         
               else:
                 print("No Login link Found")
         #self.driver.close()

      def Yopmail_login(self):
         self.driver.execute_script("window.open()")
         self.driver.switch_to.window(self.driver.window_handles[1])
         self.driver.get("https://yopmail.com/en/")
         time.sleep(20)
         mail_field = self.driver.find_element(By.CLASS_NAME,'ycptinput')
         mail_field.send_keys(Keys.CONTROL, "a")
         mail_field.send_keys(Keys.BACKSPACE)
         mail_field.send_keys(TestData.EMAIL)
         self.driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
         time.sleep(8)
         frame_login = self.driver.switch_to.frame(self.driver.find_element(By.ID,'ifmail'))

                 
         try:
             login_btn=self.driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
             if login_btn.is_displayed() and login_btn.is_enabled():
              login_btn.click()
            
         except:
               login_link=self.driver.find_element(By.LINK_TEXT,'Click here')
               if login_link.is_displayed():
                login_link.click()

