from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True,
    "dontStopAppOnReset":True,  #不退出App
    "skipDeviceInitialization":True  #权限
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
el1 = driver.find_element(By.ID, "com.xueqiu.android:id/home_search").click()
el2 = driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
driver.back()
# el3 = driver.find_element(By.XPATH,
#                           "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]").click()

driver.quit()