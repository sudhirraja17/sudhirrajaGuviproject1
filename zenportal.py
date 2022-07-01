from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time



class Guvi:
    url = "https://www.zenclass.in/login"
    driver = webdriver.Firefox()
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')
    driver.maximize_window()
#This is a login page code


    def login(self):
        email = ""
        password = ""
        self.driver.get(self.url)
        time.sleep(5)

        email1 = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
        email1 = self.driver.find_element(by=By.XPATH, value=email1)
        email1.send_keys(email)
        time.sleep(3)

        password1 = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
        password1 = self.driver.find_element(by=By.XPATH, value=password1)
        password1.send_keys(password)
        time.sleep(3)

        login_button = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'
        login1 = self.driver.find_element(by=By.XPATH, value=login_button)
        login1.click()
        time.sleep(3)

    def queue(self):
        heading = "Guvi Python AT – 1 &2 Automation Project"
        body = "This is a Project Test Code Running for the Python Automation – 1&2 Project Given by mentor Mr. Suman Gangopadhyay."

        queue_button: str = '//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div/div[2]'
        queue_button1 = self.driver.find_element(by=By.XPATH, value=queue_button)
        queue_button1.click()
        time.sleep(3)

        normal: str = ' // *[ @ id = "root"] / nav'
        just1 = self.driver.find_element(by=By.XPATH, value=normal)
        just1.click()
        time.sleep(3)

        create_button: str = '//*[@id="root"]/div[2]/div/div[1]/div[1]/button'
        create_button_query = self.driver.find_element(by=By.XPATH, value=create_button)
        create_button_query.click()
        time.sleep(3)

        close_button: str = '/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]'
        close_button1 = self.driver.find_element(by=By.XPATH, value=close_button)
        close_button1.click()
        time.sleep(3)

        category: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
        category1 = self.driver.find_element(by=By.XPATH, value=category)
        category1.click()
        time.sleep(3)

        category_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select/option[4]'
        category_option1 = self.driver.find_element(by=By.XPATH, value=category_option)
        category_option1.click()
        time.sleep(3)

        subcategory: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
        subcategory1 = self.driver.find_element(by=By.XPATH, value=subcategory)
        subcategory1.click()
        time.sleep(3)

        subcategory_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select/option[2]'
        subcategory_option1 = self.driver.find_element(by=By.XPATH, value=subcategory_option)
        subcategory_option1.click()
        time.sleep(3)

        language: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select'
        language1 = self.driver.find_element(by=By.XPATH, value=language)
        language1.click()
        time.sleep(3)

        language_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select/option[4]'
        language_option1 = self.driver.find_element(by=By.XPATH, value=language_option)
        language_option1.click()
        time.sleep(3)

        query_title: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input'
        query_title1 = self.driver.find_element(by=By.XPATH, value=query_title)
        query_title1.send_keys(heading)
        time.sleep(3)

        query_description: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
        query_description1 = self.driver.find_element(by=By.XPATH, value=query_description)
        query_description1.send_keys(body)
        time.sleep(3)

        create_button1: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button'
        create_button_xpath = self.driver.find_element(by=By.XPATH, value=create_button1)
        create_button_xpath.click()
        time.sleep(3)









s = Guvi()

s.login()

s.queue()

s.queue()

s.queue()

s.queue()

s.queue()

