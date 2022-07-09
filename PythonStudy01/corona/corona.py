import requests
import matplotlib.pyplot as plt
import numpy as np

LOCATION = "福岡県"

def main():
    r = requests.get('https://opendata.corona.go.jp/api/Covid19JapanAll')
    print(r.status_code)
    print(r.encoding)
    #corona dictionary data
    dicdata = r.json()
    #print(type(dicdata))
    datelist = dicdata["itemList"]
    #print(type(datelist))
    gdatelist = []
    gpatientsnumlist = []
    cnt = 0
    prenum = 0
    datelist.reverse()
    for datedata in datelist:
        if datedata["name_jp"] == "福岡県":
            if cnt == 0:
                prenum = int(datedata["npatients"])
            print(datedata["date"] + ":" + str(int(datedata["npatients"])-prenum))
            gdatelist.append(datedata["date"])
            gpatientsnumlist.append(int(datedata["npatients"])-prenum)
            prenum = int(datedata["npatients"])
            cnt = cnt+1
    plt.xlabel("date", fontsize=12)
    plt.ylabel("patients", fontsize=12)
    plt.xticks(np.arange(0, len(gdatelist), 50), rotation="vertical")
    plt.plot(gdatelist, gpatientsnumlist, 'b-')
    plt.show()


if __name__ == '__main__':
    main()