
from lib2to3.pgen2 import driver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Alerts(object):
    

    def __init__(self,driver):
        self.driver = driver

    """EMAIL ALREADY REGISTERED ALERT"""
    def alert_email(self):
        alert = " Email is already registered"
        try:
        #switch to alert and print pop up text
          element_alert = self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body')
          #time.sleep(3)
          alert1 = element_alert.get_attribute('textContent')
          print(alert1)
          if alert1 == alert:
              print("can't proceed")
              self.driver.close()

        except NoSuchElementException:

         print("exception handled")


    """REGISTERED SUCCESSFULL ALERT"""
    def alert_reg(self):
        alert3 = " Registered successfully!" 
        try:
        #switch to alert and print pop up text
          element_alert = self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body')
          #time.sleep(3)
          alert2 = element_alert.get_attribute('textContent')
          #print(alert2)
          if alert2!= " Registered successfully!":
              print(alert2)
              self.driver.close()
          elif alert2 == alert3:
              print(alert2)   
              print("workss") 
     
        except NoSuchElementException:

         print("exception handled")  


    """VERIFY ALERT"""
    def alert_verify(self):
        verify = " Your info is verified"
        try:
        #switch to alert and print pop up text
          element_alert = self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body')
          #time.sleep(3)
          alert2 = element_alert.get_attribute('textContent')
          #print(alert2)
          if alert2!= " Your info is verified":
              print(alert2) 
              print("works")
              self.driver.close()
          elif alert2 == verify:
              print("congrats: " + alert2)
 
        except NoSuchElementException:

         print("exception handled")

    
    """CONNECT WALLET ALERT"""
    def alert_error(self):
        try:
        #switch to alert and print pop up text
          element_alert = self.driver.find_element(By.CLASS_NAME, 'Toastify__toast-body').get_attribute('textContent')
          time.sleep(3)
          print(element_alert)
          self.driver.close()    
     
        except NoSuchElementException:

         print("No popup message")      

