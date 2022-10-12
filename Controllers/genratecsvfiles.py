from datetime import timedelta, date
from Controllers import datefuctions as df
from nsepy.history import get_price_list

def genratezips():
    #day
    try:
        ptoday = get_price_list(df.today())
        ptoday.to_csv(r'./Prices/today.csv')
    except Exception as e:
        pass
    #week
    try:
        pweek = get_price_list(df.week())
        pweek.to_csv(r'./Prices/week.csv')
    except Exception as e:
        pass
    #month
    try:
        pmonth = get_price_list(df.month())
        pmonth.to_csv(r'./Prices/month.csv')
    except Exception as e:
        pass
    #3month
    try:
        pthreemonth = get_price_list(df.threemonth())
        pthreemonth.to_csv(r'./Prices/threemonth.csv')
    except Exception as e:
        pass
    #6month
    try:
        psixmonth = get_price_list(df.sixmonth())
        psixmonth.to_csv(r'./Prices/sixmonth.csv')
    except Exception as e:
        pass
    #year
    try:
        pyear = get_price_list(df.year())
        pyear.to_csv(r'./Prices/year.csv')
    except Exception as e:
        pass