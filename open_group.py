import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GroupInteraction:
    def __init__(self, driver):
        self.driver = driver
    
    def open_group(self):
        try:
            topics_menu_item = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Group")))
            topics_menu_item.click()
            print("Succesfully opened Groups TAB")
            try:
                WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit")))
                print("Succesfully loaded content of group")
            except Exception as e:
                print("Groups page is taking too much time", e)
        except Exception as e:
            print("Failed to find or click the 'Groups' menu item:", e)

    def create_new_content(self, text):
        try:
            self.driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/main/div/div/div/div[1]/span/div/div/a/button").click()
            self.driver.find_element(By.XPATH,"//*[@id='group']").send_keys(text)
            time.sleep(3)
            save_button = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Save')]")))
            save_button.click()
            success_message = WebDriverWait(self.driver, 50).until(
                    EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div[2]"))
                )
            print("Successfully created app/topic-group:", success_message.text)
            time.sleep(3)
        except Exception :
            print("Error while creating new group-topic:")

    def edit_group_content(self,old_text, new_text):
        try:
            created_content = False
            rows = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr")
            for row in rows:
                cells = row.find_elements(By.XPATH, ".//td[1]")
                for cell in cells:
                    if old_text in cell.text:
                        edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/group/edit')]")
                        edit_button.click()
                        input_field = WebDriverWait(self.driver, 50).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[datatype="edit-group"]'))
                        )
                        input_field.clear()
                        input_field.send_keys(new_text)
                        save_button = WebDriverWait(self.driver, 50).until(
                            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/button[2]/span"))
                        )
                        save_button.click()
                        time.sleep(3)
                        print("Successfully edited the group content.")
                        created_content = True
                        return
                if created_content:
                    break

            if not created_content:
                try:
                    other_element = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/ul/li[3]")
                    other_element.click()
                    time.sleep(3)
                    rows = self.driver.find_elements(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr")
                    for row in rows:
                        cells = row.find_elements(By.XPATH, ".//td[1]")
                        for cell in cells:
                            if old_text in cell.text:
                                edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/group/edit')]")
                                edit_button.click()
                                input_field = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[datatype="edit-group"]')))
                                input_field.clear()
                                input_field.send_keys(new_text)
                                save_button = WebDriverWait(self.driver, 50).until(
                                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/button[2]/span"))
                                )
                                save_button.click()
                                time.sleep(3)
                                print("Successfully edited the group content.")
                                return
                except Exception:
                    print("EDITING content does not exist.")
        except Exception:
            print("Failed to edit content:")  
        
    def delete_group_content(self):
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
