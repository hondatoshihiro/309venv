import os

def main():
    CollectLog("d:\\work\\result")

def CollectLog(targetPath):
    print(targetPath)
    #targetPath探索
    targetList=os.listdir(targetPath)
    print(len(targetList))
    for targetFile in targetList:
        with open(targetFile, "r", encoding="utf_8") as tf:
            for line in tf:

if __name__ == '__main__':
    main()
