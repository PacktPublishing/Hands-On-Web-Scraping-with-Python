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
dataSet=[]
for product in products:
    foundProducts.append([product.text,product.get_attribute("href")])

print(foundProducts)

dataSet=[]
if len(foundProducts)>0:
   for foundProduct in foundProducts:
       driver.get(foundProduct[1])
       product_url = driver.current_url
       product_name = driver.find_element_by_xpath('//*[@id="center_column"]//h1[@itemprop="name"]').text
       short_description = driver.find_element_by_xpath('//*[@id="short_description_content"]').text
       product_price = driver.find_element_by_xpath('//*[@id="our_price_display"]').text
       image_url = driver.find_element_by_xpath('//*[@id="bigpic"]').get_attribute('src')
       condition = driver.find_element_by_xpath('//*[@id="product_condition"]/span').text
       dataSet.append([product_name,product_price,condition,short_description,image_url,product_url])

   
print(dataSet)

driver.close()
driver.quit()
