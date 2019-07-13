from selenium import webdriver
import time
import pandas as pd
import re
import datetime
from dateutil.relativedelta import relativedelta


class BasketBall():

    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.browser = webdriver.Chrome("C:/Users/Administrator/PycharmProjects/PracticeDesinApi/chromedriver.exe",options = self.option)





    def getBasketData(self,url):
        self.browser.get(url)

        time.sleep(2)
        url_detail = []

        dict = {'date':[],'visitTeam':[],'homeTeam':[],'stageName':[],'visitScore':[],'homeScore':[],'volume':[]}


        lis = self.browser.find_element_by_class_name("calendar_list")
        tbody = lis.find_element_by_tag_name("tbody")
        trs = tbody.find_elements_by_tag_name("tr")
        for tr in trs[:] :
            a_s = tr.find_elements_by_tag_name('a')
            print(len(a_s))
            for a in a_s :
                url_detail.append(a.get_attribute('href'))
                browser2 = webdriver.Chrome("C:/Users/Administrator/PycharmProjects/PracticeDesinApi/chromedriver.exe",options=self.option)
                browser2.get(a.get_attribute('href'))

                date = browser2.find_element_by_class_name('txt_date').text
                extend_body = browser2.find_element_by_class_name('extend_body')
                game_top = extend_body.find_element_by_class_name('game_top_txt')
                stage = game_top.find_element_by_tag_name('p').text
                volume = re.split(' \[관중 : ', stage)[1][:-2]
                stageName = re.split(' \[관중 : ',stage)[0]
                dict['volume'].append(volume)
                dict['stageName'].append(stageName)
                print('volume : ',volume, ' stagename : ', stageName)

                tbl = extend_body.find_element_by_class_name('col_tbl')

                trs = tbl.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
                print("trs의 길이: ", len(trs))

                home = trs[0].find_elements_by_tag_name('td')[0].text
                home_score = trs[0].find_element_by_class_name('last').text
                dict['homeTeam'].append(home)
                dict['homeScore'].append(home_score)


                visit = trs[1].find_elements_by_tag_name('td')[0].text
                visit_score = trs[1].find_element_by_class_name('last').text
                dict['visitTeam'].append(visit)
                dict['visitScore'].append(visit_score)
                print(date)
                dict['date'].append(date)

                browser2.close()
                # print(a.text)
            print("----------")

        self.df = pd.DataFrame(dict)
        self.df.to_csv()

        print(self.df)



#
#
# dict = {'date': [], 'visitTeam': [], 'homeTeam': [], 'stageName': [], 'visitScore': [], 'homeScore': [],
#             'volume': []}
#
# dfs = pd.DataFrame(dict)
# dfs.to_csv('basket.csv', mode='w', index=False, encoding="euc-kr")
#
# startDate = "2016-10-01"
# dtDate = datetime.datetime.strptime(startDate,"%Y-%m-%d")
# for i in range(0,100) :
#     dtDate = dtDate - relativedelta(months=1)
#     url = "https://www.kbl.or.kr/schedule/today/calendar.asp?tdate=20190709&CalDate="+dtDate.strftime("%Y-%m-%d")
#
#
#     basket = BasketBall()
#
#     basket.getBasketData(url)
#     dfs = pd.concat([dfs, basket.df])
#     print(dtDate.strftime("%Y-%m-%d"))
#     print(dfs)
#
#     dfs.to_csv('C:/Users/Administrator/PycharmProjects/PracticeDesinApi/data/basketData/basketBall.csv', mode='a', header=False, index=False, encoding="euc-kr")






