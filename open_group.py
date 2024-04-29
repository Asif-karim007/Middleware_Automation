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
# CREATE
        text= "Creating new content"
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
# SEARCHING FOR NEW CREATED CONTENT
        created_content = False
        rows = WebDriverWait(self.driver, 50).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody.ant-table-tbody > tr.ant-table-row.ant-table-row-level-0")))
        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, "ant-table-cell")
            for cell in cells:
                if text in cell.text:
                    edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/group/edit')]")
                    edit_button.click()
                    created_content = True
                    break
            if created_content:
                break

        if not created_content:
            try:
                other_element = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/ul/li[3]")
                other_element.click()
                WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tbody.ant-table-tbody > tr.ant-table-row.ant-table-row-level-0")))

                rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody.ant-table-tbody > tr.ant-table-row.ant-table-row-level-0")
                for row in rows:
                    cells = row.find_elements(By.CLASS_NAME, "ant-table-cell")
                    for cell in cells:
                        if text in cell.text:
                            edit_button = row.find_element(By.XPATH, ".//a[contains(@href, '/group/edit')]")
                            edit_button.click()
                            break
            except Exception:
                print("EDITING content does not exist.")

        
# EDITING THE CREATED CONTENT
        try:
            input_element = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[datatype="edit-group"]'))
            )
            input_element.click()
            time.sleep(3)
            input_element.clear()
            input_element.send_keys(" Edited")
            time.sleep(3)
            WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/button[2]/span")))
            try:
                self.driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/button[2]/span").click()
            except Exception:
                print("Can not edit")
        except Exception as e:
            print(f"Error while editing: {e}")




        time.sleep(3)

# FINDING AND DELETING CONTENT
        Edited_content = False
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody.ant-table-tbody > tr.ant-table-row.ant-table-row-level-0")
        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, "ant-table-cell")
            for cell in cells:
                if "Edited" in cell.text:
                    print("Succesfully edited a new group-topic")
                    WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td[2]/div/div[2]/button/span[2]")))
                    edit_button = row.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td[2]/div/div[2]/button/span[2]")
                    edit_button.click()
                    WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div/div[2]/button[2]")))
                    self.driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div/div[2]/button[2]").click()
                    print("Succesfully deleted a new group-topic")
                    Edited_content = True
                    break
                 
            if Edited_content:
                break

        if not Edited_content:
            try:
                other_element = self.driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/ul/li[3]")
                other_element.click()
                WebDriverWait(self.driver, 40).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit")))

                rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody.ant-table-tbody > tr.ant-table-row.ant-table-row-level-0")
                for row in rows:
                    cells = row.find_elements(By.CLASS_NAME, "ant-table-cell")
                    for cell in cells:
                        if "Edited" in cell.text:
                            print("Succesfully edited a new group-topic")
                            WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td[2]/div/div[2]/button/span[2]")))
                            edit_button = row.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[8]/td[2]/div/div[2]/button/span[2]")
                            edit_button.click()
                            WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div[2]/div/div/div/div[2]/button[2]/span")))
                            self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div[2]/button[2]/span").click()
                            print("Succesfully deleted a new group-topic")
                            break
                            # WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div[2]"))        
            except Exception:
                print("DELETING Content does not exist.")


        time.sleep(5)