from selenium.webdriver import FirefoxOptions,Firefox
from selenium.webdriver.common.by import By

browser = Firefox()
browser.get("https://railway.raja.ir/login?UserName=1619160716101600154215971626")
browser.find_element(By.ID,"password").send_keys("Bb1515750")
browser.find_element(By.ID,"btnlogin").click()
#pass Bb1515750
# browser.find_element(By.XPATH,"")
