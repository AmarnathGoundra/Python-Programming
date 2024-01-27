""" Browser Automation
first install selenium library using command
pip install selenium """

""" next download webdriver for automation"""

""" Execute step by step to see changes in chrome """



from selenium import webdriver

browser=webdriver.Chrome("D:\Python\chromedriver")

browser.get("https://www.google.com")

elem=browser.find_element_by_link_text("Images")

elem.click()


#unable to search using nptel commannd
