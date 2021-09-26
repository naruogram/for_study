# from typing import KeysView, Optional
# from selenium import webdriver   
# from selenium.webdriver import ChromeOptions 
# from selenium.webdriver.chrome.webdriver import WebDriver
# import os      # Webブラウザを自動操作する（python -m pip install selenium)
# import chromedriver_binary             # パスを通すためのコード
# import urllib.request
# from pathlib import Path 
# import time
# from flask_test import *

# @app.route('/send',methods =['POST','GET'])
# def getclass():
#   user_id = request.form.get("user_id")
#   password = request.form.get("password")
#   options = webdriver.ChromeOptions()
#   options.add_experimental_option("prefs", {
#     "download.default_directory": "〜\kwansei_file"
# });
#   chromedriver = 'chromedriver.exe'
#   options.add_argument('--kiosk-printing')
#   driver = webdriver.Chrome(options=options)  


#   driver.get('https://luna.kwansei.ac.jp//')  # Googleを開く
#   element = driver.find_element_by_name("login")
#   element.click()
#   search_bar_user= driver.find_element_by_name("username")
#   search_bar_user.send_keys(user_id)
#   search_bar_password = driver.find_element_by_name("password")
#   search_bar_password.send_keys(password)
#   element_log = driver.find_element_by_name("login")
#   element_log.click()
#   element_subject = driver.find_element_by_link_text("科目")
#   element_subject.click()
#   element_2021 = driver.find_element_by_link_text("2021")
#   element_2021.click()
#   element_subject = driver.find_element_by_xpath("//div[@class='collapsible']/th/*[@href]")
#   print(element_subject)
  