
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import re
from alerts import Alerts
from yopmail import Yopmail
from config import TestData

      
def trust_signup():    
      driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
      driver.maximize_window()
      driver.implicitly_wait(10)
      driver.get(TestData.AKRU)
      window_before = driver.window_handles[0]
      driver.find_element(By.CLASS_NAME,'primary-btn').click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/div/label[1]/span[1]/span[1]/input').click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/div[1]/form/button').click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button').click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div/div/div[1]/button').click()
      driver.find_element(By.NAME,'firstName').send_keys(TestData.FIRST_NAME)
      driver.find_element(By.NAME,'lastName').send_keys(TestData.LAST_NAME)
      driver.find_element(By.NAME,'email').send_keys(TestData.EMAIL)
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/fieldset/div/label[3]/span[1]/span[1]/input').click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[1]/div[4]/label/span[1]/span[1]/input').click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/button').click()
      time.sleep(10)


      """HANDLING ALERT IF EMAIL IS ALREADY REGISTERED"""
      a = Alerts(driver)
      a.alert_email()


      """YOPMAIL"""
      y = Yopmail(driver)
      y.Yop_mail()


      """ CONTACT INFO"""

      contact_window=driver.switch_to.window(driver.window_handles[2])
      time.sleep(18)
      #WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[1]/div/div/div/input')).send_keys(TestData.TRUST)
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[1]/div/div/div/input').send_keys(TestData.TRUST)
      select=Select(driver.find_element(By.NAME,'trustClassification'))
      select.select_by_visible_text('Non-Grantor')

      select=Select(driver.find_element(By.NAME,'trustType'))
      select.select_by_visible_text('Irrevocable')

      select= Select(driver.find_element(By.NAME,'industry'))
      select.select_by_visible_text('Restaurant')

      """DATE PICKER"""

      datee = driver.find_element(By.XPATH," //input[contains(@value,'08/18/2004')]")
      datee.click()
      datee.send_keys(Keys.CONTROL, "a")   
      datee.send_keys("08/18/2002")  
      time.sleep(4)

      select = Select(driver.find_element(By.NAME,'juristdiction'))
      select.select_by_visible_text('Ohio')

      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[7]/div[2]/input').send_keys(TestData.EIN)


      """UPLOAD DOC"""
      driver.find_element(By.NAME,'file').send_keys("C://Users/jawad/Downloads/Performa wise.pdf")
      driver.find_element(By.NAME,'file').send_keys("C://Users/jawad/Downloads/test_summary_report.pdf")

      """TRUST ADDRESS"""
      driver.find_element(By.NAME,'address').send_keys(TestData.ADDRESS_LINE_1)
      driver.find_element(By.NAME,'city').send_keys(TestData.CITY)
      select=Select(driver.find_element(By.NAME,'stateName'))
      select.select_by_visible_text('Alabama')
      driver.find_element(By.NAME,'zipCode').send_keys(TestData.ZIP_CODE)



      """ REPESENTATIVE INFORMAION"""
      select=Select(driver.find_element(By.NAME,'title'))
      select.select_by_visible_text('CEO')
      driver.find_element(By.NAME,'firstName').send_keys(TestData.FIRST_NAME_REPRESENTATIVE)
      driver.find_element(By.NAME,'lastName').send_keys(TestData.LAST_NAME_REPRESENTATIVE)
      driver.find_element(By.NAME,'email').send_keys(TestData.EMAIL_REPRESENTATIVE)
      driver.find_element(By.NAME,'address1').send_keys(TestData.ADDRESS_REPRESENTATIVE)


      """UPLOAD REPRESENTATIVE PERSONAL INFORMATION"""
      select = Select(driver.find_element(By.NAME,'personalIdType'))
      select.select_by_visible_text('Passport')
      driver.find_element(By.NAME,'file').send_keys("C://Users/jawad/Downloads/Roofstock.png")
      driver.find_element(By.NAME,'city2').send_keys(TestData.CITY_REPRESENTATIVE)
      select=Select(driver.find_element(By.NAME,'state2'))
      select.select_by_visible_text('Alabama')
      driver.find_element(By.NAME,'postalCode').send_keys(TestData.ZIP_CODE)
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[23]/input').send_keys(TestData.SSN)
      driver.find_element(By.NAME,'number').send_keys(TestData.PHONE_NO)
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[1]/div[24]/div/div/div[2]/button').click()
      time.sleep(10)


      """ OTP"""
      driver.execute_script("window.open()")
      driver.switch_to.window(driver.window_handles[3])
      driver.get(TestData.OTP)

      otp_value= driver.find_element(By.XPATH,'/html/body/pre')

      """USING REGULAR EXPRESSION TO REMOVING TEXT FROM SENTENCE AND GETTING ONLY NUMBERS"""
      value = int(re.sub(r"[^\d.]", "", otp_value.text))

      """GETTING LAST 4 NUMBERS FROM WHOLE SENTENCE"""
      code=int(str(value)[-4:])
      print("value: %s" % code)
      driver.close()

      """SWICHING BACK TO CONTACT INFO AND ENTER OTP NUMBER"""
      driver.switch_to.window(driver.window_handles[2])
      driver.find_element(By.NAME,'otp').send_keys(code)
      time.sleep(2)

      """DATE PICKER"""
      datee = driver.find_element(By.XPATH,"//input[contains(@value,'02/10/2004')]")
      datee.click()
      datee.send_keys(Keys.CONTROL, "a")   
      datee.send_keys("08/18/2002")  
      time.sleep(4)

      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/section/div/div[2]/form/div[2]/div/button').click()
     
      """HANDLE ALERT"""
      a = Alerts(driver)
      a.alert_error()

      time.sleep(24)

      """SKIP STEP"""
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      #WebDriverWait(driver,20).until(EC.presence_of_element_located(By.XPATH,'/html/body/div[1]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button')).click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/div[3]/form/div[2]/div[2]/div/div/button').click()
      time.sleep(4)

      """VERIFY STEP"""
      driver.find_element(By.NAME,'point1').click()
      driver.find_element(By.NAME,'point2').click()
      driver.find_element(By.NAME,'point3').click()
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[2]/div[2]/div/div/button').click()
      time.sleep(4)

      """CONNECT WALLET STEP"""
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button').click()
      time.sleep(1)

      """HANDLE ALERT"""
      a = Alerts(driver)
      a.alert_verify()

      time.sleep(12)
      driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div/div/div/div/div/form/div[3]/div[2]/div/div/button').click()
     
      """HANDLE ALERT"""
      a = Alerts(driver)
      a.alert_error()

      time.sleep(4)
      driver.find_element(By.CLASS_NAME,'donwload-btn').click()
      
      """HANDLE ALERT"""
      a = Alerts(driver)
      a.alert_error()
      
      time.sleep(2)

      """YOPMAIL"""
      y = Yopmail(driver)
      y.Yopmail_login()

      time.sleep(4)

      driver.switch_to.window(driver.window_handles[2])
      time.sleep(40) 
      #driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/div[3]/button').click()

      """HANDLE ALERT"""
      a = Alerts(driver)
      a.alert_reg()


trust_signup()


