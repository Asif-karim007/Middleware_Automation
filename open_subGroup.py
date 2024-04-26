
#         # FINDING AND DELETING CONTENT
# # ONLY FINDING IN first PAGE
#         # other_element = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/ul/li[3]")
#         # other_element.click()






#         # WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit")))


#         # rows = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr")
#         # for row in rows:
#         #     cells = row.find_elements(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[1]")
#         #     for cell in cells:
#         #         if "Edited" in cell.text:
#         #             print("Succesfully edited a new Sub group-topic")
#         #             WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td[2]/div/div[2]/button/span[2]")))
#         #             edit_button = row.find_element(By.XPATH, "//*[@id='__next']/div/div/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/div[2]/button")
#         #             edit_button.click()
#         #             time.sleep(2)
#         #             WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div/div[2]/button[2]")))
#         #             self.driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div/div[2]/button[2]/span").click()
#         #             print("Succesfully deleted a new Sub group-topic")
#         #             found_edited = True
#         #             break 
#         #     if found_edited:
#         #         break
   



#         # time.sleep(5)







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
        except Exception:
            print("Failed to find or click the 'Sub Groups' menu item:")
    time.sleep(5)
    def create_new_content(self, text):
        try:
            try:
                create_button = WebDriverWait(self,50).until(EC.visibility_of_element_located(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[1]/span/div/div/a/button"))
                time.sleep(3)
                create_button.click()
                time.sleep(3)
            except Exception:
                print("can cot click on create button")
            WebDriverWait(self,50).until(EC.visibility_of_element_located(By.LINK_TEXT,"Create sub group"))
            input_field = self.driver.find_element(By.XPATH, "//*[@id='subGroup']")
            input_field.clear()
            input_field.send_keys(text)
            time.sleep(3)
            save_button = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save')]"))
            )
            save_button.click()

            success_message = WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div[2]"))
            )
            print("Successfully created a new Sub group-topic:", success_message.text)
        except Exception :
            print("Error while creating new Sub group-topic:")
    
    time.sleep(5)
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
                            break
                        except Exception:
                            print("Element found but did not edit")

                        

        except Exception:
            print("Failed to edit content:")



