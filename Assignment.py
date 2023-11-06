from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Setting up the Firefox web driver
driver = webdriver.Firefox()

# Step 1: Navigate to the URL
url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"
driver.get(url)

driver.maximize_window()
driver.implicitly_wait(5)

# Step 2 : Finding and clicking the button with the text "Table Data"
button = driver.find_element(By.XPATH, "//*[text() = 'Table Data']")
button.click()

inputBox = driver.find_element(By.XPATH, "//textarea[@id='jsondata']")
inputBox.clear()

# Step 3: JSON data insertion
with open("data.json", "r") as json_file:
    json_data = json.load(json_file)
    # Convert the JSON data to a string
    json_string = json.dumps(json_data)

# Enter the JSON data into the input box
inputBox.send_keys(json_string)

# Step 4 : Refreshing table with updated data
refreshButton = driver.find_element(By.XPATH, "//button[@id='refreshtable']")
refreshButton.click()

# Step 5 : Comparing table and JSON data
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dynamictable"]')))
table_data = []
items = len(json_data)

list1 = []
list2 = []

for i in table.find_elements(By.XPATH, '//*[@id="dynamictable"]//td'):
    list1.append(i.text)
    # print(i.text)

for y in range(0, items):
    for z in json_data[y]:
        list2.append(str(json_data[y][z]))

if list1 == list2:
    print('Pass')
else:
    print('Fail')

time.sleep(5)

# Close the web driver
driver.quit()
