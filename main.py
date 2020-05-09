from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import openpyxl as xl
import time

wb = xl.load_workbook(r'replace with your excel workbook path') # put your excel workbook path here
sheet = wb.get_sheet_by_name('replace with sheet name (default Sheet1)') # sheet name goes here(default Sheet1)
nms = [] # an empty list to append names later
nums = [] # an empty list to append numbers later
for cell in sheet['A']: # replace A with the names column, starting with A1
    nms.append(cell.value)
for cell in sheet['B']: # replace B with the numbers column, starting with B1
    nums.append(cell.value)

al = dict(zip(nums, nms)) # zipping the two lists in a dictionary

url = 'https://web.whatsapp.com/send?phone='
driver = webdriver.Chrome("replace with your chromedriver path")

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

driver.get('https://web.whatsapp.com/')

time.sleep(10) # prepare your phone to scan the code in those 10 seconds

msg = 'replace with your some text'
def send(num,nm):
    driver.get(url+num)
    element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
    txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    txt_box.send_keys('Dear '+nm+', '+msg) # Customize this line to add the name to your message
    txt_box.send_keys("\n")
    time.sleep(10) # This is just to avoid bad connection problems

for num in al:
    send(num,al[num])
