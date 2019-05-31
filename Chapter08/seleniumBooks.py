from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_path = 'chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get('http://books.toscrape.com/index.html')

dataSet = []
# select: Food and Drink
driver.find_element_by_link_text("Food and Drink").click()
print("Current Page URL: ", driver.current_url)
totalBooks = driver.find_element_by_xpath("//*[@id='default']//form/strong[1]")
print("Found: ", totalBooks.text)

page = True
while page:
    listings = driver.find_elements_by_xpath("//*[@id='default']//ol/li[position()>0]")
    for listing in listings:
        url = listing.find_element_by_xpath(".//article[contains(@class,'product_pod')]/h3/a").get_attribute('href')
        title = listing.find_element_by_xpath(".//article[contains(@class,'product_pod')]/h3/a").text
        titleLarge = listing.find_element_by_xpath(".//article[contains(@class,'product_pod')]/h3/a").get_attribute(
            'title')
        price = listing.find_element_by_xpath(".//article/div[2]/p[contains(@class,'price_color')]").text
        stock = listing.find_element_by_xpath(".//article/div[2]/p[2][contains(@class,'availability')]").text
        image = listing.find_element_by_xpath(
            ".//article/div[1][contains(@class,'image_container')]/a/img").get_attribute('src')
        starRating = listing.find_element_by_xpath(".//article/p[contains(@class,'star-rating')]").get_attribute(
            'class')
        dataSet.append([titleLarge, title, price, stock, image, starRating.replace('star-rating ', ''), url])

    try:
        #Check for Pagination with text 'next'
        driver.find_element_by_link_text('next').click()
        continue
    except NoSuchElementException:
        page = False

print("Completed")

print(dataSet)

driver.close()
driver.quit()
