from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# url - Pixieset gallery url
# psw - Password to check
# driver - Selenium broser to use
def tryPass(url, psw, driver):
	driver.delete_all_cookies()
	driver.get(url)
	
	passField = driver.find_element_by_id("GuestLoginForm_password")
	passField.send_keys(psw)

	submitBtn = driver.find_element_by_xpath("//input[@type='submit' and @value='ENTER']")
	submitBtn.click()
	
	old_url = driver.current_url
	
	while True:
		if driver.current_url != old_url:
			return True
		try:
			pswIsInc = driver.find_element_by_xpath("//div[text()='Password is incorrect.']")
		except:
			pswIsInc = []
		if pswIsInc:
			return False
		time.sleep(0.1)
	
	return url1 != url2
	
def main():
	options = Options()
	options.add_argument("--headless")
	driver = webdriver.Firefox(firefox_options=options)
	print(tryPass("[something].pixieset.com/guestlogin/[something]", "theCakeIsALie", driver))
	
if __name__ == "__main__":
	main()