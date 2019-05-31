import re

filename = 'sitemap.xml'

# collect Blog title information from URLs except not link to any  category
dataSetBlog = []
dataSetBlogURL = [] # collects Blog URLs
dataSetCategory = [] # collect Category title
dataSetCategoryURL = [] # collect Category URLs

page = open(filename, 'r').read()
pattern = r"loc>(.*)</loc"
urlPatterns = re.findall(pattern, page)
print(type(urlPatterns))


for url in urlPatterns:

    if re.match(r'.*blog', url): #Blog related
        dataSetBlogURL.append(url)
        if re.match(r'[\w\-]', url):
            blogTitle = re.findall(r'blog/([A-Za-z0-9\-]+)', url)
            if len(blogTitle) > 0 and not re.match('(category)', blogTitle[0]):
                dataSetBlog.append(blogTitle[0])

    if re.match(r'.*category', url): #Category Related
        dataSetCategoryURL.append(url)
        categoryTitle = re.findall(r'category/([\w\-\s]+)', url)
        dataSetCategory.append(categoryTitle[0])


print("Blogs URL: ", len(dataSetBlogURL))
print(dataSetBlogURL)

print("Blogs Title: ", len(dataSetBlog))
print(dataSetBlog)

print("Unique Blog Count: ", len(set(dataSetBlog)))
print(set(dataSetBlog))

print("Category URL  Count: ", len(dataSetCategoryURL))
print(dataSetCategoryURL)

print("Category Title  Count: ", len(dataSetCategory))
print(dataSetCategory)

print("Unique Category Count: ", len(set(dataSetCategory)))
print(set(dataSetCategory))


