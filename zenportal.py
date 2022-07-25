from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time


#Class name is Guvi
#In this Class define a function(login,main_menu,query)
class Guvi:
    url = "https://www.zenclass.in/login"
    driver = webdriver.Firefox()
    driver.maximize_window()

    # This is a function for login page code
    def login(self):
        email = "sudhirraja1996@gmail.com"
        password = "17031996Sr@"
        self.driver.get(self.url)
        # timer For 5 seconds  to load all elements
        time.sleep(5)

        #This code is use for executing the email id by xpath
        email1 = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
        email1 = self.driver.find_element(by=By.XPATH, value=email1)
        email1.send_keys(email)
        # timer For 2 seconds  to load all elements
        time.sleep(2)

        # This code is use for executing the password by xpath
        password1 = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
        password1 = self.driver.find_element(by=By.XPATH, value=password1)
        password1.send_keys(password)
        # timer For 2 seconds  to load all elements
        time.sleep(2)

        # This code is use for executing to submit by xpath
        login_button = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'
        login1 = self.driver.find_element(by=By.XPATH, value=login_button)
        login1.click()
        # timer For 2 seconds  to load all elements
        time.sleep(2)



    """This is a function for list out and document
     all the information and left-hand side ribbon 
     of the Zen portal.
     """
    def main_menu(self):

       # Accessing Zen portal items on the left-hand side of the page

        time.sleep(5)
        l_menu = self.driver.execute_script(
            " l_menu_items=document.getElementsByClassName"
            '("list-scroll py-3 color-area");'
            " l_menu_logo= document.getElementsByClassName"
            '("ml-3 d-inline-block mt-3 font-weight-bold")[0].innerText;'
            "l_menu_head=document.getElementsByClassName"
            '("list-scroll py-3 active-area active-left-bar")[0].innerText;'
            " l_menu=[];"
            """for (let index = 0; index < l_menu_items.length; index++)
                   {
                   l_menu[index]=l_menu_items.item(index).innerText;
                   }
                   l_menu.splice(0,0,l_menu_logo,l_menu_head);
                   return l_menu ;"""
        )
        # convert list to dataframe
        df_fm = pd.DataFrame(l_menu, columns=["Main-menu"])

        writer = pd.ExcelWriter("ZenClass.xlsx", engine="xlsxwriter")

        # Convert the dataframe to an XlsxWriter Excel object.
        df_fm.to_excel(writer, sheet_name="Main-menu", index=False)

        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = workbook.add_worksheet("Class")
        # Take screenshot of the page
        self.driver.get_full_page_screenshot_as_file("Class.png")

        # Insert an image.
        worksheet.insert_image("A1", "Class.png")

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        return df_fm

    # This is a function is created a query
    @property
    def query(self):
        #This variable is declared a title 'heading' and description 'body' of the query
        heading = "Guvi Python AT – 1 &2 Automation Project"
        body = "This is a Project Test Code Running for the Python Automation – 1&2 Project Given by mentor Mr. Suman Gangopadhyay."

        # This code is use for Click the query button by xpath
        query_button: str = '//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div/div[2]'
        query_button1 = self.driver.find_element(by=By.XPATH, value=query_button)
        query_button1.click()
        time.sleep(3)

        # This code is use for Click normal in webpage by xpath
        normal: str = ' // *[ @ id = "root"] / nav'
        just1 = self.driver.find_element(by=By.XPATH, value=normal)
        just1.click()
        time.sleep(3)

        # This code is use for Click the create button by xpath
        create_button: str = '//*[@id="root"]/div[2]/div/div[1]/div[1]/button'
        create_button_query = self.driver.find_element(by=By.XPATH, value=create_button)
        create_button_query.click()
        time.sleep(3)
        # This code is use for Click for close a quick query box by xpath
        close_button: str = '/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]'
        close_button1 = self.driver.find_element(by=By.XPATH, value=close_button)
        close_button1.click()
        time.sleep(3)

        # This code is use for Click the category by xpath
        category: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
        category1 = self.driver.find_element(by=By.XPATH, value=category)
        category1.click()
        time.sleep(3)

        #This code is use for Click for what we choose a category option by xpath
        category_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select/option[4]'
        category_option1 = self.driver.find_element(by=By.XPATH, value=category_option)
        category_option1.click()
        time.sleep(3)

        # This code is use for Click for subcategory by xpath
        subcategory: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
        subcategory1 = self.driver.find_element(by=By.XPATH, value=subcategory)
        subcategory1.click()
        time.sleep(3)

        # This code is use for Click for what we choose a subcategory option by xpath
        subcategory_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select/option[2]'
        subcategory_option1 = self.driver.find_element(by=By.XPATH, value=subcategory_option)
        subcategory_option1.click()
        time.sleep(3)

        # This code is use for Click for language by xpath
        language: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select'
        language1 = self.driver.find_element(by=By.XPATH, value=language)
        language1.click()
        time.sleep(3)

        # This code is use for Click for what we choose a language option by xpath
        language_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select/option[4]'
        language_option1 = self.driver.find_element(by=By.XPATH, value=language_option)
        language_option1.click()
        time.sleep(3)

        # This code is use for execute the query title the heading by xpath
        query_title: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input'
        query_title1 = self.driver.find_element(by=By.XPATH, value=query_title)
        query_title1.send_keys(heading)
        time.sleep(3)

        # This code is use for execute the query description the body by xpath
        query_description: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
        query_description1 = self.driver.find_element(by=By.XPATH, value=query_description)
        query_description1.send_keys(body)
        time.sleep(3)

        # This code is use for click the submit button by xpath
        create_button1: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button'
        create_button_xpath = self.driver.find_element(by=By.XPATH, value=create_button1)
        create_button_xpath.click()
        time.sleep(3)

        # return the query header
        self.driver.get("https://www.zenclass.in/queries")
        time.sleep(5)
        query_result = self.driver.execute_script(
            'return document.getElementsByClassName'
            '("Queries_sq__tile__title__I0aWK")[0].innerText')
        time.sleep(5)
        self.driver.close()
        return query_result



g = Guvi()

