from selenium import webdriver
from getpass import getpass

username = input("Enter Student ID: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("C:\\Dev\\WebDrivers\\chromedriver.exe")
driver.get("https://vulms.vu.edu.pk/LMS_LandingPage.aspx")

username_textbox = driver.find_element_by_id("txtStudentID")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("txtPassword")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("ibtnLogin")
login_button.submit()
