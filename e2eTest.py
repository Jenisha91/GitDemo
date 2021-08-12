from selenium import webdriver
# tagname is optional!
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="c:\\chromedriver_win32\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()

# //div[@class='card h-100']/div/h4/a
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text  # don't put "s" if you are using loop
    if product_name == "Blackberry":
        # click add button
        product.find_element_by_xpath("div[2]/button").click()

driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()

driver.find_element_by_id("country").send_keys("Ind")


wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()


print("Hello this is my first change")
print("This is my second line of change")
print("This one is a last one!")
print("Created new branch")
print("newwwwwwwwwww branch")

