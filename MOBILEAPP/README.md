# Mobile-Test-Automation

## APPIUM ##
[http://appium.io/docs/en/about-appium/intro/]
- Appium is an Open Source, Cross-platform utility for testing Native, Web and Hybrid applications on iOS, and Android Mobile Operating System platforms
- Appium is based on Client-Server Architecture, where Appium testing Clients send automation commands to the Appium Server which translates it to platform-specific commands and executes on the devices.
- Appium Clients are basically libraries exposed by the Appium framework for Mobile Automation which can be used by test engineers. It supports various languages such as Java, Python, and Ruby.


![Appium Architecture](https://miro.medium.com/max/1400/1*l0yBxGN1gX2P4fMtUyTW6A.png)

## Appium Desktop ##
[https://github.com/appium/appium-desktop]
- Appium Desktop is an app for Mac, Windows, and Linux which gives you the power of the Appium automation server in a beautiful and flexible UI.
  - A graphical interface for the Appium Server
  - An Inspector that you can use to look at your app's elements
- Download from [https://github.com/appium/appium-desktop/releases/tag/v1.18.2]
  
## Desired Capabilities ##
- Desired capabilities are how you configure your Appium session  
- tell the Appium server what kind of platform and app you want to automate
- In order to start the app we would need the app Package and Activity name
   - We can get these details from the apk file of the app. Instead of downloading the apk file and looking into app manifest file for this detail, 
   - we can also download some really cool apps which can get you these details. Apk Info/ AppInfo is one such app which you can download from Play Store and get the app Package and Activity details. 
   - Just download the app and click on Apk Info Icon which will list all the apps on your device. Click on your app to get the details required as shown below
	   - dumpsys window windows | grep -E 'mCurrentFocus'
	   - adb shell dumpsys package | grep -i " + (enter package name)  + " |grep Activity
	   - adb shell dumpsys package | grep -Eo "^[[:space:]]+[0-9a-f]+[[:space:]]+com.whatsapp/[^[:space:]]+" | grep -oE "[^[:space:]]+$"
	   - adb shell dumpsys package | grep $packagename | grep Activity

### Appium Server Installation on Macos ###
- Install node for macos from [https://nodejs.org/en/]
- npm install -g appium
- npm install -g appium-doctor
- appium-doctor --android/--ios
- To run Appium Server execute, appium
- Finding the running appium process
	- lsof -nP -iTCP:4723 -sTCP:LISTEN
	- kill -9 <pid>
- Launching programattically
  - from appium.webdriver.appium_service import AppiumService
  - appium_service = AppiumService()
  - self.appium_service.start() and self.appium_service.stop()


### Appium Python Client ###
[https://github.com/appium/python-client]
- pip install Appium-Python-Client
- Documentation [https://appium.github.io/python-client-sphinx/webdriver.html]
- Selenium Python Bindings Documentation [https://selenium-python.readthedocs.io/installation.html#introduction]

### Inspecting elements ###
- Launch Uiautomatorviewer - Used for finding elements
- On macos go to /Users/rajkgupta/Library/Android/sdk/tools/bin
- ./uiautomatorviewer
- chrome://inspect/#devices for inspecting webapp elements

### Check Device Connection ###
- Use "adb devices" to see connected devices

### Mirroring Android Device on Mac ###
- Install Teamviewer on Mac
- Install Teamviewer Quick Support on Android Device
- Another App: Airdroid

### Test Apks ###
- Download selendroid test app from http://selendroid.io/

### Visual Testing using Applitools ###
- pip install eyes-selenium

### Selenium/Appium Grid ###
- [https://www.selenium.dev/documentation/en/grid/]

- Start Selenium Grid3 and Register Nodes
	- Download Selenium-standalone-server jar from https://www.selenium.dev/downloads/
	- Start the hub with this command "java -jar selenium-server-standalone-3.141.59.jar -role hub -host localhost"
	- Now you can access the hub console with this url — http://ip_hub_machine:4444/grid/console
	- Register node using command "java -DWebdriver.chrome.driver='/Users/rajkgupta/Documents/Testing-Projects/Selenium-Testing-Project/chromedriver' -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444/grid/register/"
	- Register Appium node 1 using command "appium -p 4725 --udid 520082c3cad586a7 -bp 5556 --chromedriver-port 5645 --nodeconfig "/Users/rajkgupta/PycharmProjects/Appium-Test-Project/config/all.json" -g "/Users/rajkgupta/PycharmProjects/Appium-Test-Project/logs/appium_1.log" --session-override"
	- Register Appium node 2 using command "appium -p 4726 --udid dcba4985 -bp 5556 --chromedriver-port 5645 --nodeconfig "/Users/rajkgupta/PycharmProjects/Appium-Test-Project/config/all.json" -g "/Users/rajkgupta/PycharmProjects/Appium-Test-Project/logs/appium_2.log" --session-override"

- Selenium Grid4
![Grid 4](https://www.selenium.dev/documentation/images/grid_4.png)


### Design Pattern ###
- POM (Page Object Model)

![POM](https://miro.medium.com/max/1400/0*U-AyhQqLOsc78O7y)

- Problems
	- Test scalability
	- Code redundancy
	- Difficult to maintain

- Solution (Add Intermediate Layer - Controllers)

![Solution](https://miro.medium.com/max/1400/0*B_8ku5i52B1h15Si)




###  Tutorial Links ###
- https://experitest.com/appium-testing/the-complete-guide-appium-testing-using-python/
- https://applitools.com/tutorials/appium-native-python.html#install-the-sdk
- https://qxf2.com/blog/appium-tutorial-python-physical-device/
- https://medium.com/onefootball-locker-room/distributed-parallel-execution-of-appium-tests-with-selenium-grid-4c29b8600baf
- https://medium.com/keeptruckin-eng/simplifying-ui-test-automation-with-page-object-model-and-controllers-8115657908b9

