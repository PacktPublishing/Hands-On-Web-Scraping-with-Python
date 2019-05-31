from pyquery import PyQuery as pq
import re

sourceUrl = 'http://www.flyershistory.com/cgi-bin/ml-poffs.cgi'
dataSet = list()
keys = ['year','month','day','game_date','team1', 'team1_score', 'team2', 'team2_score', 'game_status']

def read_url(url):
    """Read given Url , Returns pyquery object for page content"""
    pageSource = pq(url)
    return pq(pageSource)


if __name__ == '__main__':
    page = read_url(sourceUrl)

    tableRows = page.find("h1:contains('AHL Playoff Results') + table tr")
    print("\nTotal rows found :", tableRows.__len__())

    for tr in tableRows.items():
        team1 = tr.find('td').eq(1).text()
        if team1 != '':
            game_date = tr.find('td').eq(0).text()
            dates = re.search(r'(.*)-(.*)-(.*)',game_date)

            team1_score = tr.find('td').eq(2).text()
            team2 = tr.find('td').eq(4).text()
            team2_score = tr.find('td').eq(5).text()

            #check Game Status should be either 'W' or 'L'
            game_status = tr.find('td').eq(6).text()
            if not re.match(r'[WL]',game_status):
                game_status = tr.find('td').eq(7).text()

            #breaking down date in year,month and day
            year = dates.group(3)
            month = dates.group(2)
            day = dates.group(1)
            if len(year)==2 and int(year)>=68:
                year = '19'+year
            elif len(year)==2 and int(year) <68:
                year = '20'+year
            else:
                pass

            #appending individual data list to the dataSet
            dataSet.append([year,month,day,game_date,team1,team1_score,team2,team2_score,game_status])

    print("\nTotal Game Status, found :", len(dataSet))
    print(dataSet)
