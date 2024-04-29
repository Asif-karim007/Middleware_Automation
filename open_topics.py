import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Topics:
    def __init__(self, driver):
        self.driver = driver
    
    def open_topics(self):
        try:
            topics_menu_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Topics")))
            topics_menu_item.click()
            print("Succesfully opened Topics TAB")
        except Exception as e:
            print("Failed to find or click the 'Topics' menu item:", e)

        WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/span")))
        self.driver.find_element(By.LINK_TEXT, "Create").click()
        self.driver.find_element(By.ID, "title").send_keys("Hello")
        # GROUP
        dropdown_locator = "//*[@id='rc-tabs-0-panel-1']/div[2]/div/div[2]/div/div/div"
        self.driver.find_element(By.XPATH, dropdown_locator).click()
        option_xpath = "//div[contains(@class, 'ant-select-item-option-content') and text() = 'Movement and Exercise']"
        option_to_click = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option_to_click.click()

        # SUB-GROUP
        dropdown_locator1 = "//*[@id='rc-tabs-0-panel-1']/div[3]/div/div[2]/div/div/div/div"
        self.driver.find_element(By.XPATH, dropdown_locator1).click()
        option_xpath1 = "//div[contains(@class, 'ant-select-item-option-content') and text() = 'Posture-Enhancing Workouts']"
        option_to_click1 = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, option_xpath1)))
        option_to_click1.click()

        time.sleep(10)

