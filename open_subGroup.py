import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

class SubGroupInteraction:
    def __init__(self, driver):
        self.driver = driver

    def open_sub_group(self):
        try:
            topics_menu_item = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sub Group"))
            )
            topics_menu_item.click()
            print("Successfully opened SubGroups TAB")
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit")))
            print("Successfully loaded content of Sub group")
            time.sleep(3)
        except Exception:
            print("Failed to find or click the 'Sub Groups' menu item:")
    
    def create_new_content(self, text):
        try:
            create_button = self.driver.find_element(By.XPATH, "//button[@class='ant-btn css-dev-only-do-not-override-w8172h ant-btn-primary refine-create-button']")
            self.driver.execute_script("arguments[0].click();", create_button)
            time.sleep(3)
            input_field = self.driver.find_element(By.XPATH, "//*[@id='subGroup']")
            
            input_field.send_keys(text)
            # save_button = self.driver.find_element((By.XPATH, "//button[contains(., 'Save')]"))      

            save_button = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Save')]")))
            self.driver.execute_script("arguments[0].click();", save_button)      
            # save_button.click()
            time.sleep(3)
            print("Succesfully created new Sub group-topic")
        except Exception :
            print("Error while creating new Sub group-topic:")
    
    def edit_sub_group_content(self, old_text, new_text):
        try:
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit")))
            rows = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr")
            found = False
            for row in rows:
                cells = row.find_elements(By.XPATH, ".//td[1]")
                for cell in cells:
                    if old_text in cell.text:
                        try:
                            edit_button = WebDriverWait(row, 50).until(
                                EC.element_to_be_clickable((By.XPATH, ".//button[.//span[text()='Edit']]"))
                            )
                            edit_button.click()

                            input_field = WebDriverWait(self.driver, 50).until(
                                EC.element_to_be_clickable((By.XPATH, "//input[@id='subGroup' and @datatype='edit-subgroup']"))
                            )
                            input_field.clear()
                            input_field.send_keys(new_text)
                            time.sleep(3)

                            save_button = WebDriverWait(self.driver, 50).until(
                                EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/button[2]/span"))
                            )
                            save_button.click()
                            
                            WebDriverWait(self.driver, 50).until(
                                EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div[2]"))
                            )
                            print("Successfully edited the content.")
                            return
                        except Exception:
                            print("Element found but did not edit")

                        

        except Exception:
            print("Failed to edit content:")


    def delete_sub_group_content(self):
        try:
            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit")))
            rows = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr")
            found = False
            for row in rows:
                cells = row.find_elements(By.XPATH, ".//td[1]")
                for cell in cells:
                    if "Edited Content" in cell.text:
                        print("Succesfully edited a new Sub group-topic")
                        try:
                            time.sleep(3)
                            delete_button = row.find_element(By.XPATH, f".//button[.//span[text()='Delete']]")  
                            self.driver.execute_script("arguments[0].click();", delete_button)
                            time.sleep(3)
                            self.driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div/div[2]/button[2]/span").click()
                            print("Succesfully deleted a new Sub group-topic")
                            time.sleep(3)
                            return
                        except Exception:
                            print("Element found but did not delete")

        except Exception:
            print("Failed to delete content:")

    