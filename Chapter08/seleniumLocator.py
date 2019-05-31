from selenium import webdriver
chrome_path='chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get('http://automationpractice.com')
print("Current Page URL: ",driver.current_url)

searchBox = driver.find_element_by_id('search_query_top')
print("Type :",type(searchBox))
print("Attribute Value :",searchBox.get_attribute("value"))
print("Attribute Class :",searchBox.get_attribute("class"))
print("Tag Name :",searchBox.tag_name)

searchBox.clear()
searchBox.send_keys("Dress")

submitButton = driver.find_element_by_name("submit_search")
submitButton.click()

resultsShowing = driver.find_element_by_class_name("product-count")
print("Results Showing: ",resultsShowing.text)

resultsFound = driver.find_element_by_xpath('//*[@id="center_column"]//span[@class="heading-counter"]')
print("Results Found: ",resultsFound.text)

products = driver.find_elements_by_xpath('//*[@id="center_column"]//a[@class="product-name"]')
#products = driver.find_elements_by_css_selector('ul.product_list li.ajax_block_product a.product-name')

foundProducts=[]
for product in products:
    foundProducts.append([product.text,product.get_attribute("href")])

print(foundProducts)    

driver.close()
driver.quit()
