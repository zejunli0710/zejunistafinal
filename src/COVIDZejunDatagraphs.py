import pandas as pd, numpy as np, matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import datetime as dt

def get_df():
    fname = "data_table_for_daily_death_trends__idaho.csv"
    df = pd.read_csv(fname,sep=',', skiprows = 2, engine='python')
    del df["State"]
    df["Dates"] = np.nan
    def date_convert(date_to_convert):
        return datetime.datetime.strptime(date_to_convert, '%b %d %Y').strftime('%m/%d/%Y')
    df['Dates'] = df['Date'].apply(date_convert)
    del df["Date"]
    return df

def get_date_lst():
    df = get_df()
    lst_dates = []
    for i in df['Dates']:
        lst_dates.append(i)
    return lst_dates

def fig1():
    df = get_df()
    lst_dates = get_date_lst()
    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in lst_dates]
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
    plt.plot(x,df['Current Hospitalized COVID-19 Patients'])
    plt.gcf().autofmt_xdate()
    plt.xlabel("Dates")
    plt.ylabel("Current Hospitalized COVID-19 Patients")
    

def fig2():
    df = get_df()
    lst_dates = get_date_lst()
    plt.figure(figsize=(10,10))
    plt.style.use('ggplot')
    lst_dates = []
    for i in df['Dates']:
        lst_dates.append(i)
    x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in lst_dates]
    lst = []
    for i in df['New Deaths']:
        lst.append(i)
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x,lst,width=0.8, color='darkviolet')
    plt.xlabel("Dates")
    plt.ylabel("New Deaths")
    
def fig3():
    df = get_df()
    plt.figure(figsize=(16,10), dpi= 80)
    lst_dates = get_date_lst()
    lst = []
    for i in df["7-Day Moving Avg"]:
        lst.append(i)
    x = np.array(lst_dates)
    y = np.array(lst)
    plt.scatter(x, y)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
    plt.xlabel("Dates")
    plt.ylabel("7-Day Moving Avg")
    
def main():
    fig1()
    fig2()
    fig3()
    plt.show()
main()