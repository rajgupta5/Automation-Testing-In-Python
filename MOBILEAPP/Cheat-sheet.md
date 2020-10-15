## Import Packages ##
- from selenium.webdriver.common.by import By
- from appium import webdriver
- from appium.webdriver.appium_service import AppiumService
- from selenium.webdriver.support.ui import WebDriverWait
- from selenium.webdriver.support import expected_conditions as EC





## Create webdriver instance ##
- dc = {}
- driver = None
- self.dc['app'] = "apk path"
- self.dc['appPackage'] = "package"
- self.dc['appActivity'] = "main activity"
- self.dc['platformName'] = 'platform'
- self.dc['deviceName'] = 'dcba4985'
- self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

## Find Element strategies ##
Documentation [https://selenium-python.readthedocs.io/locating-elements.html#]

- find_element
  - driver.find_element(By.XPATH, '//button[text()="Some text"]')
- find_elements
  - driver.find_elements(By.XPATH, '//button')
  
- Xpath
  - self.driver.find_element_by_xpath("//*[@text='Skip']").click()
- Accessebility Id
  - self.driver.find_element_by_accessibility_id("Navigate up").click()
- Id
  - login_form = driver.find_element_by_id('loginForm')
- name
  - username = driver.find_element_by_name('username')
- linktext
  - continue_link = driver.find_element_by_link_text('Continue')
  - continue_link = driver.find_element_by_partial_link_text('Conti')
- tagname
  - heading1 = driver.find_element_by_tag_name('h1')
- class name
  - content = driver.find_element_by_class_name('content')
- Css selector
  - content = driver.find_element_by_css_selector('p.content')

## Interaction ##
- element.send_keys(" and some", Keys.ARROW_DOWN)
- element.clear()
- 



## Start and Stop Appium Server ##
- appium_service = AppiumService()
- self.appium_service.start()
- self.appium_service.stop()

## Waits ##
- Implicit Wait
  - self.driver.implicitly_wait(10)
- Explicit Wait
  -  element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
  

## Sleep ##
time.sleep(10)

## Closing the session ##
self.driver.quit()


## Screenshot ##
- driver.save_screenshot('screenshot.png')

## Execute Script ##
- Ex: How to scroll down to the bottom of a page
  - driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


