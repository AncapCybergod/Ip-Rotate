from selenium import webdriver
import stem
from stem.control import Controller
from time import sleep 

myProxy = '127.0.0.1:8118'



controller = Controller.from_port(port=9051)
controller.authenticate('authtoken')


proxies = {
    'http': "127.0.0.1:8118"
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://%s' % myProxy)
# chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 2})
chrome_options.set_headless()

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))

for i in range(0,  100):
    
    driver.get("url")
    sleep(.5)

    # bytes_read = controller.get_info("traffic/read")
    # bytes_written = controller.get_info("traffic/written")
    # print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))
    controller.signal(stem.Signal.NEWNYM)
driver.quit()


