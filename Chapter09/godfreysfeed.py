import re
import requests

def read_url(url):
    pageSource = requests.get(url).text
    return pageSource


if __name__ == "__main__":

    dataSet=list()
    sourceUrl = 'http://godfreysfeed.com/dealersandlocations.php'
    page = read_url(sourceUrl)

    pLatLng= r'var latLng = new google.maps.LatLng\((?P<lat>.*)\,\s*(?P<lng>.*)\)\;'
    latlngs = re.findall(pLatLng,page)
    print("Findall found total LatLngs: ", len(latlngs))

    pDealers = r'infoWindowContent = infoWindowContent\+\s*\"(.*?)\"\;'
    dealers = re.findall(pDealers, page)
    print("Findall found total Address: ", len(latlngs))

    d=0
    for dealer in dealers:
        dealerInfo = re.split(r'<br>',re.sub(r'<br><br>','',dealer))
        name = re.findall(r'\'>(.*?)</span',dealerInfo[0])[0]
        address = re.findall(r'>(.*)<',dealerInfo[1])[0]
        city = re.findall(r'>(.*),\s*(.*)<',dealerInfo[2])[0][0]
        state = re.findall(r'>(.*),\s*(.*)<',dealerInfo[2])[0][1]
        zip = re.findall(r'>(.*)<',dealerInfo[3])[0]
        lat = latlngs[d][0]
        lng = latlngs[d][1]
        d+=1
        dataSet.append([name,address,city,state,zip,lat,lng])

    print(dataSet) #[[name,address, city, state, zip, lat,lng],]


#Findall found total LatLngs:  55
#Findall found total Address:  55
#[['Akins Feed & Seed', '206 N Hill Street', 'Griffin', 'GA', '30223', '33.2509855', '-84.2633946'], ['Alf&apos;s Farm and Garden', '101 East 1st Street', 'Donalsonville', 'GA', '39845', '31.0426107', '-84.8821949'], ['American Cowboy Shop', '513 D Murphy Hwy', 'Blairsville', 'GA', '30512', '34.8761989', '-83.9582412'], ['Anderson&apos;s General Store', '23736 US Hwy 80 E', 'Statesboro', 'GA', '30458', '32.43158', '-81.749293'], ['Bar G Horse & Cattle Supply', '1060 Astondale Road', 'Bishop', 'GA', '30621', '33.8192864', '-83.4387722'], ['Beggs Farm Supply', '5845 Royston Hwy', 'Canon', 'GA', '30520', '34.2959968', '-83.0062267'], ['Big Creek Feed', '218 Hwy 49 N', 'Byron', 'GA', '31025', '32.6537561', '-83.7596295'], ['Blue Ribbon Show Supply', '9416 Lucy Moore Road', 'Nichols', 'GA', '31554', '31.462497', '-82.5866503'], ['Burdette Mill', '216 Depot Street', 'Washington', 'GA', '30673', '33.7340136', '-82.7472304'], ['Burke Feed', '369 Hwy 56 N', 'Waynesboro', 'GA', '30830', '33.1064245', '-81.9852452'], ['Candler Feed and Seed', '1275 Smokey Park Hwy', 'Candler', 'NC', '28715', '35.5401542', '-82.7570303'], ['Cash & Carry Feed', '135 N McGriff St.', 'Whigham', 'GA', '39897', '30.8848506', '-84.3248931'], ['Cherokee Feed and Seed', '869 Grove St', 'Gainesville', 'GA', '30501', '34.289323', '-83.8219858'], ['Cherokee Feed and Seed', '2370 Hightower Rd', 'Ball Ground', 'GA', '30107', '34.3372664', '-84.3779515'], ['Claxton Family Cattle', '240 Old Douglas Road', 'Hazelhurst', 'GA', '31539', '31.836371', '-82.6232915'], ['D&D Irringation', '51 S Rentz St', 'Lenox', 'GA', '31637', '31.2713852', '-83.4629421'], ['Double D Stables and Tack', '4111 Logan Rd', 'Rocky Face', 'GA', '30740', '34.805079', '-85.0274471'], ['Eatonton Co-op', '504 S Jefferson Ave', 'Eatonton', 'GA', '31024', '33.3267997', '-83.3884961'], ['Edenfields Feed and Seed', '709 Hwy 25N', 'Millen', 'GA', '30442', '32.8088128', '-81.9491768'], ['Family Feed', '6424 COLUMBUS HWY 80', 'Box Springs', 'GA', '31801', '32.5580349', '-84.6513774'], ['Farm & Garden Inc.', '646 Clarksville Street', 'Cornelia', 'GA', '30531', '34.5114883', '-83.5271166'], ['Farmer Seed Company', '800 W Broad St', 'Doerun', 'GA', '31744', '31.3200669', '-83.9234872'], ['Farmers Feed', '204 N West St', 'Greensboro', 'GA', '30642', '33.5781281', '-83.1845358'], ['Feed South', '2623 Knight Avenue', 'Waycross', 'GA', '31503', '31.2028754', '-82.316785'], ['Forsyth Feed & Seed', '45 W Jefferson Street', 'Forsyth', 'GA', '31029', '33.035097', '-83.940067'], ['Georgia Deer Farm', '850 Hwy 27 N', 'Roopville', 'GA', '30170', '33.476202', '-85.1082285'], ['H&M Trailers and Feed', '6446 JFH Pkwy', 'Adairsville', 'GA', '30103', '34.3924623', '-84.9333769'], ['Hill Farm Supply', '12700 Augusta Hwy', 'Sparta', 'GA', '31087', '33.2791285', '-82.9646478'], ['Ijon Webb', '1130 Stillwell Rd', 'Springfield', 'GA', '31329', '32.369773', '-81.266672'], ['Jesup Milling', '601 SW Broad Street', 'Jesup', 'GA', '31545', '31.5990992', '-81.8905051'], ['Jump N Run Farm', '1569 Liberty Church Grove Rd', 'Wrightsville', 'GA', '31096', '32.6481899', '-82.6139868'], ['L & C Farm and Garden', '1143 East Fairplay Road', 'Fairplay', 'SC', '29643', '34.5101355', '-82.9602795'], ['Maddox Feed', '1915 Winder Hwy', 'Jefferson', 'GA', '30549', '34.1001367', '-83.5969643'], ['Miller Farm Supply', '2001 Bob Culvern Rd', 'Louisville', 'GA', '30434', '32.9859964', '-82.3913739'], ['North Fulton Feed', '12950 Hwy 9 N', 'Alpharetta', 'GA', '30004', '34.096767', '-84.2735144'], ['North Georgia Co-Op', '951 Progress Rd', 'Ellijay', 'GA', '30540', '34.6739981', '-84.4902665'], ['Oglethorpe Feed and Farm Supply', '900 Athens Road', 'Crawford', 'GA', '30648', '33.8898662', '-83.1358665'], ['Owens Farm Supply', '6414 Mize Road', 'Toccoa', 'GA', '30577', '34.4855944', '-83.3394454'], ['Patricks', '10285 Covington Bypass', 'Covington', 'GA', '30014', '33.5770654', '-83.8354943'], ['Perry Feed and Tack', '309 Kellwood Drive', 'Perry', 'GA', '31069', '32.4443895', '-83.7439432'], ['Pine Ridge Outdoor Supply', '4999 HWY 114', 'Lyerly', 'GA', '30730', '34.4166444', '-85.3925577'], ['Reeves Hardware', '95 BO James St', 'Clayton', 'GA', '30525', '34.8686254', '-83.4026817'], ['Roberts Milling Company', '116 West Albany Ave', 'Pearson', 'GA', '31642', '31.2987063', '-82.8577173'], ['Roche Farm and Garden', '803 E Jackson St', 'Dublin', 'GA', '31040', '32.5444125', '-82.8945945'], ['Roche Farm and Garden', '781 East Court Street', 'Wrightsville', 'GA', '31040', '32.7302168', '-82.7117232'], ['Rodgers Fertilizer', '409 N Main St', 'Saluda', 'SC', '29138', '34.0082425', '-81.7729772'], ['Rogers Feed', '1041 Easley Hwy', 'Pelzer', 'SC', '29669', '34.6639864', '-82.5126743'], ['Ronnie Spivey', '654 Mary Richardson Road', 'Wray', 'GA', '31796', '31.525261', '-83.06603'], ['Shirley Feed & Seed Inc', '2439 North Elm Street', 'Commerce', 'GA', '30529', '34.2068698', '-83.4689814'], ['Southern Home and Farm LLC', '3127 Hamilton Road', 'Lagrange', 'GA', '30241', '32.9765932', '-84.98978'], ['Southland Power Fence', '752 E 5th Ave', 'Colbert', 'GA', '30628', '34.0412765', '-83.2001394'], ['Town & Country General Store', '59 Hwy 212 West', 'Monticello', 'GA', '31064', '33.3066615', '-83.6976187'], ['Twisted Fitterz', '10329 Nashville Enigma Rd', 'Alapaha', 'GA', '31622', '31.3441482', '-83.3002373'], ['Westside Feed II', '230 SE 7th Avenue', 'Lake Butler', 'FL', '32054', '30.02116', '-82.329495'], ['White Co. Farmers Exchange', '951 S Main St', 'Cleveland', 'GA', '30528', '34.58403', '-83.760829']]
