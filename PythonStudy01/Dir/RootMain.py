#import SubMain
from SubMain import SubMain
from SubDir.Dir01 import Dir01
from SubDir.SubSubDir.Dir02 import Dir02

class RootMain:
    """This is the module for studying Packaging of Python"""
    #Constructer
    def __init__(self):
        self.name = ""
    #
    def getName(self):
        return "RootMain:" + self.name
    #
    def setName(self, name):
        self.name = name

#実行
if __name__ == '__main__':
    rootMainObj = RootMain()
    rootMainObj.setName("Test")
    print(rootMainObj.getName())

    #import SubMainとした場合
    #subMainObj = SubMain.SubMain()
    #from SubMain import SubMainとした場合
    subMainObj = SubMain()
    subMainObj.setName("SubTest")
    print(subMainObj.getName())

    dir01Obj = Dir01()
    dir01Obj.setName("Dir01Test")
    print(dir01Obj.getName())

    dir02Obj = Dir02()
    dir02Obj.setName("Dir02Test")
    print(dir02Obj.getName())
