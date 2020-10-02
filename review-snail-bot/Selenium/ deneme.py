from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()

# Load a Firefox selenium webdriver session
from selenium import webdriver
browser = webdriver.Firefox()

# Visit our front page
browser.get("http://www.pythonanywhere.com")
print (browser.page_source)
browser.close()