
import basketBall
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta


if __name__ == "__main__" :

    dict = {'date': [], 'visitTeam': [], 'homeTeam': [], 'stageName': [], 'visitScore': [], 'homeScore': [],
            'volume': []}

    dfs = pd.DataFrame(dict)
    dfs.to_csv('basket.csv', mode='w', index=False, encoding="euc-kr")

    startDate = "2010-03-01"
    dtDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")
    for i in range(0, 50):
        dtDate = dtDate - relativedelta(months=1)
        url = "https://www.kbl.or.kr/schedule/today/calendar.asp?tdate=20190709&CalDate=" + dtDate.strftime("%Y-%m-%d")

        basket = basketBall.BasketBall()

        basket.getBasketData(url)
        dfs = pd.concat([dfs, basket.df])
        print(dtDate.strftime("%Y-%m-%d"))
        print(dfs)

        dfs.to_csv('C:/Users/Administrator/PycharmProjects/PracticeDesinApi/data/basketData/basketBall.csv', mode='a',
                   header=False, index=False, encoding="euc-kr")

    dfs.to_csv('C:/Users/Administrator/PycharmProjects/PracticeDesinApi/data/basketData/result.csv', mode='w',
                   header=True, index=False, encoding="euc-kr")
