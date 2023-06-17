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
    alist = []
    for datedata in datelist:
        blist = []
        if datedata["name_jp"] == "福岡県":
            if cnt == 0:
                prenum = int(datedata["npatients"])
            print(datedata["date"] + ":" + str(int(datedata["npatients"])-prenum))
            gdatelist.append(datedata["date"])
            #1週間平均感染者数算出 start
            alist.append( int(datedata["npatients"])-prenum )
            index = 0
            sum = 0
            print("テスト1 len(alist):" + str(len(alist)))
            for a in alist:
                sum = sum + a
                index = index + 1
            gpatientsnumlist.append( sum/len(alist))
            if len(alist) == 7:
                print("テスト2 len(alist):" + str(len(alist)))
                for index in range(len(alist)):
                    if index != 0:
                        blist.append(alist[index])
                    #print("テスト index:" + str(index))
            else:
                blist = alist
            alist.clear
            alist = blist
            #print("テスト3 len(alist):" + str(len(alist)))
            #print("テスト3 len(blist):" + str(len(blist)))
            #1週間平均感染者数算出 end
            #1日の感染者数 start
            #gpatientsnumlist.append(int(datedata["npatients"])-prenum)
            #1日の感染者数 end
            prenum = int(datedata["npatients"])
            cnt = cnt+1
    plt.xlabel("date", fontsize=12)
    plt.ylabel("patients(7days-average)", fontsize=12)
    plt.xticks(np.arange(0, len(gdatelist), 50), rotation="vertical")
    plt.plot(gdatelist, gpatientsnumlist, 'b-')
    plt.show()


if __name__ == '__main__':
    main()