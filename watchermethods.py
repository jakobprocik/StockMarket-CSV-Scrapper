def datainserter(nasdaq):
    import csv
    import requests
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey="PutYourKey"".format(nasdaq)
    headerrow = ['date', 'open', 'high', 'low', 'close', 'volume']
    print(url)
    r = requests.get(url)
    r = r.json()
    outputFile = open('{}.csv'.format(nasdaq), 'w', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(headerrow)
    keyset = []
    for key in r['Time Series (Daily)'].keys():
        keyset.append(key)
    keyset.reverse()
    for i in keyset:
        dataset = []
        dataset.append(i.replace("-", "."))
        for data in r['Time Series (Daily)'][i].values():
            dataset.append(data)
        outputWriter.writerow(dataset)
    outputFile.close()



def addnewrow(nasdaq):
    from datetime import datetime
    import requests
    import csv
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=FZKUGWK1WOQ1A3RY".format(nasdaq)
    r = requests.get(url)
    r = r.json()
    date = datetime.today().strftime('%Y-%m-%d')
    newdataset = []
    newdataset.append(date)
    for i in  r['Time Series (Daily)'][date].values():
        newdataset.append(i)
    outputFile = open('{}.csv'.format(nasdaq), 'a', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(newdataset)
    outputFile.close()


def imagecreator(nasdaq):
    import csv
    from matplotlib import pyplot as plt
    stockfile = open('{}.csv'.format(nasdaq))
    stockreader = csv.reader(stockfile)
    stockset = []
    for row in stockreader:
        stockset.append(row)
    del stockset[0]
    days = []
    close = []

    for i in range(1, 29):
        days.append(i)

    for closevalue in stockset:
        close.append(closevalue[4])

    days = days[:10]
    close = close[:10]

    closes = [float(i) for i in close]
    print(type(closes[0]))
    plt.plot(days, closes, color='black', marker='o', linestyle='solid',)
    print(type(days[0]))
    print(type(close[0]))
    plt.title("{} Stock".format(nasdaq))
    plt.ylabel("Close Value")
    plt.xlabel("Day")

    plt.savefig('{}.png'.format(nasdaq))
