import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from open_topics import Topics as TopicsInteraction
from open_group import GroupInteraction as GroupInteractionobj
from open_subGroup import SubGroupInteraction
from open_bodyRegion import BodyRegion


class MenuInteraction:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def login(self, username, password):
        try:
            self.driver.get("http://localhost:3000/login")
            self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys(username)
            self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
            self.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
            # Wait for login confirmation message
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/div/main/div/div/h1"))
            )
            expected_msg = "Congratulations, Middleware is successfully running!"
            msg = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/main/div/div/h1").text
            if expected_msg == msg:
                print(expected_msg)
        except Exception:
            print("Error occurred while login")

    
    def _click_menu_item(self):
        driver.find_element(By.XPATH,"//*[@id='__next']/div/aside/div[1]/ul/li[6]/div/span").click()


    

# Usage
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

menu_interaction = MenuInteraction(driver)
topics_interaction = TopicsInteraction(driver)
group_interaction = GroupInteractionobj(driver)
sub_group_interaction = SubGroupInteraction(driver)
body_region_interaction = BodyRegion(driver)



menu_interaction.login("admin", "1q2w3E*")
menu_interaction._click_menu_item()
# # topics_interaction.open_topics()



group_interaction.open_group()
group_interaction.create_new_content("Creating new content")
time.sleep(5)
group_interaction.edit_group_content("Creating new content", " Edited Content")
group_interaction.delete_group_content()


# SUBGROUPFUNCTIONS
sub_group_interaction.open_sub_group()
sub_group_interaction.create_new_content("Creating new content")
time.sleep(5)
sub_group_interaction.edit_sub_group_content("Creating new content", " Edited Content")
sub_group_interaction.delete_sub_group_content()


# BODYREGIONFUNCTIONS
body_region_interaction.open_sub_group()
body_region_interaction.create_new_content("Creating new content")
time.sleep(3)
body_region_interaction.edit_sub_group_content("Creating new content", " Edited Content")
body_region_interaction.delete_sub_group_content()


driver.quit()

